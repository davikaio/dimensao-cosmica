import MetaTrader5 as mt5
import pandas as pd
import time
from datetime import datetime

# Parâmetros
ativo = "PETR4"  # Ativo da B3
volume = 100     # Número de ações
ma_curta = 5     # Média móvel curta
ma_longa = 20    # Média móvel longa

# Inicializar conexão
if not mt5.initialize():
    print("Erro ao conectar ao MetaTrader 5")
    mt5.shutdown()
    exit()

# Função para buscar dados históricos
def get_data(symbol, n=100):
    rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M1, 0, n)
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df

# Função para calcular médias móveis e sinal
def gerar_sinal(df):
    df['ma_curta'] = df['close'].rolling(ma_curta).mean()
    df['ma_longa'] = df['close'].rolling(ma_longa).mean()

    if df['ma_curta'].iloc[-2] < df['ma_longa'].iloc[-2] and df['ma_curta'].iloc[-1] > df['ma_longa'].iloc[-1]:
        return 'compra'
    elif df['ma_curta'].iloc[-2] > df['ma_longa'].iloc[-2] and df['ma_curta'].iloc[-1] < df['ma_longa'].iloc[-1]:
        return 'venda'
    else:
        return 'neutro'

# Função para enviar ordem
def enviar_ordem(tipo):
    preco = mt5.symbol_info_tick(ativo).ask if tipo == 'compra' else mt5.symbol_info_tick(ativo).bid
    tipo_ordem = mt5.ORDER_TYPE_BUY if tipo == 'compra' else mt5.ORDER_TYPE_SELL

    ordem = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": ativo,
        "volume": volume,
        "type": tipo_ordem,
        "price": preco,
        "deviation": 5,
        "magic": 10032025,
        "comment": "bot_autonomo_ma",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    resultado = mt5.order_send(ordem)
    print(f"[{datetime.now()}] Ordem {tipo.upper()} enviada: ", resultado)
    return resultado

# Loop principal
try:
    while True:
        df = get_data(ativo)
        sinal = gerar_sinal(df)
        print(f"[{datetime.now()}] Sinal gerado: {sinal}")

        if sinal == 'compra':
            enviar_ordem('compra')
        elif sinal == 'venda':
            enviar_ordem('venda')

        time.sleep(60)  # Espera 1 minuto para nova análise

except KeyboardInterrupt:
    print("Encerrando o bot.")
    mt5.shutdown()
