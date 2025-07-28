import pandas as pd
import talib

class EstrategiaDolarInteligente:
    def __init__(self):
        self.dentro_compra = False
        self.dentro_venda = False
        self.preco_entrada_venda = None
        self.preco_entrada_compra = None
        self.stop_compra = None
        self.stop_venda = None

    def executar(self, df: pd.DataFrame):
        sinais = []

        # 🔎 Verifica se o DataFrame é válido
        if df is None or df.empty:
            print("⚠️ DataFrame está vazio ou não carregado.")
            return df

        # ✅ Verifica colunas obrigatórias
        colunas_necessarias = ['close', 'high', 'low']
        for coluna in colunas_necessarias:
            if coluna not in df.columns:
                raise ValueError(f"🚫 A coluna obrigatória '{coluna}' não foi encontrada no DataFrame.")

        # 🧪 Detecta volume com nome alternativo
        if 'volume' in df.columns:
            volume = df['volume']
        elif 'tick_volume' in df.columns:
            volume = df['tick_volume']
        else:
            raise ValueError("🚫 Nenhuma coluna de volume encontrada ('volume' ou 'tick_volume').")

        close = df['close']
        high = df['high']
        low = df['low']

        ema = close.ewm(span=20, adjust=False).mean()
        vwap = ((high + low + close) / 3 * volume).cumsum() / volume.cumsum()
        sar = talib.SAR(high, low, acceleration=0.01, maximum=0.15)
        adx = talib.ADX(high, low, close, timeperiod=14)

        for i in range(20, len(df)):
            vol_atual = volume.iloc[i]
            vol_media = volume.iloc[i-20:i].mean()

            if vol_atual <= vol_media or volume[i] <= volume[i-1] or volume[i] <= volume[i-2]:
                sinais.append('NEUTRO')
                continue

            adx_atual = adx.iloc[i]
            preco_atual = close.iloc[i]
            sar_atual = sar.iloc[i]

            if adx_atual > 20:
                if (preco_atual < sar_atual) and (not self.dentro_venda):
                    self.preco_entrada_venda = preco_atual
                    self.stop_venda = self.preco_entrada_venda + 12
                    self.dentro_venda = True
                    self.dentro_compra = False
                    sinais.append('VENDA')
                elif (preco_atual > sar_atual) and (not self.dentro_compra):
                    self.preco_entrada_compra = preco_atual
                    self.stop_compra = self.preco_entrada_compra - 12
                    self.dentro_compra = True
                    self.dentro_venda = False
                    sinais.append('COMPRA')
                else:
                    sinais.append('MANTER')
            elif self.dentro_venda:
                if preco_atual <= self.preco_entrada_venda - 12:
                    self.stop_venda -= 5
                sinais.append('SAIR_VENDA' if self.stop_venda > preco_atual else 'VENDA_ATIVA')
            elif self.dentro_compra:
                if preco_atual >= self.preco_entrada_compra + 12:
                    self.stop_compra += 5
                sinais.append('SAIR_COMPRA' if self.stop_compra < preco_atual else 'COMPRA_ATIVA')
            else:
                sinais.append('NEUTRO')

        df.loc[df.index[-len(sinais):], 'sinal'] = sinais
        return df
