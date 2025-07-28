import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime
import time

# 📌 Ativo que deseja monitorar
SYMBOL = "PETR4"

# 🔧 Inicializar conexão com MT5
if not mt5.initialize():
    print("❌ Não foi possível iniciar conexão com o MetaTrader 5")
    mt5.shutdown()
    exit()

# 🧩 Selecionar o ativo
if not mt5.symbol_select(SYMBOL, True):
    print(f"❌ Não foi possível selecionar o ativo {SYMBOL}")
    mt5.shutdown()
    exit()

print(f"🚀 Monitoramento iniciado para {SYMBOL}...\n")

# 🔄 Loop de observação
while True:
    # 1. 📊 Candle mais recente (M1)
    rates = mt5.copy_rates_from_pos(SYMBOL, mt5.TIMEFRAME_M1, 0, 1)
    if rates is None or len(rates) == 0:
        print("⚠️ Candle não recebido.")
    else:
        candle = pd.DataFrame(rates)
        print(f"\n📅 {datetime.now().strftime('%H:%M:%S')} — Ativo: {SYMBOL}")
        print("📈 Último Candle:")
        print(candle[['open', 'high', 'low', 'close', 'tick_volume']])

    # 2. 📘 Book de ofertas (Nível 2)
    book = mt5.market_book_get(SYMBOL)
    if book is None:
        print("⚠️ Book de ofertas não disponível.")
    else:
        print("📘 Book de Ofertas:")
        for entry in book:
            tipo = "🟢 Compra" if entry.type == mt5.BOOK_TYPE_BUY else "🔴 Venda"
            print(f"{tipo} | Preço: R${entry.price:.2f} | Volume: {entry.volume}")

    time.sleep(2)
