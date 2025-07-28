import pandas as pd

class AnaliseFluxoOrdens:
    def __init__(self, stop_gain=0.30, stop_loss=0.30, lote=100):
        self.stop_gain_valor = stop_gain
        self.stop_loss_valor = stop_loss
        self.lote = lote

    def executar(self, df: pd.DataFrame):
        sinais = []
        for i in range(1, len(df)):
            bid = df['bid_price'].iloc[i]
            ask = df['ask_price'].iloc[i]
            spread = df['spread'].iloc[i]
            vol_comp = df['vol_agressiva_compra'].iloc[i]
            vol_vend = df['vol_agressiva_venda'].iloc[i]
            of_comp = df['ofertas_compra'].iloc[i]
            of_vend = df['ofertas_venda'].iloc[i]
            min_tick = df['min_price_increment'].iloc[i]

            stop_gain = bid + self.stop_gain_valor
            stop_loss = ask - self.stop_loss_valor

            if of_comp > of_vend and vol_comp > vol_vend and spread < min_tick * 2:
                if bid >= stop_gain:
                    sinais.append('SAIR_COMPRA')
                elif ask <= stop_loss:
                    sinais.append('STOP_COMPRA')
                else:
                    sinais.append('COMPRA')
            elif of_vend > of_comp and vol_vend > vol_comp and spread < min_tick * 2:
                if ask <= stop_gain:
                    sinais.append('SAIR_VENDA')
                elif bid >= stop_loss:
                    sinais.append('STOP_VENDA')
                else:
                    sinais.append('VENDA')
            else:
                sinais.append('NEUTRO')

        df = df.iloc[-len(sinais):].copy()
        df['sinal_fluxo_ordem'] = sinais
        return df
