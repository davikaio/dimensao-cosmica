import MetaTrader5 as mt5
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import time
import csv
import os
import winsound

# 📌 Configurações
SYMBOL = "PETR4"
VOLUME_ALERTA = 30000  # dispara som quando entrar lote maior
CAMINHO_LOG = "logs/fluxo_log.csv"

# 📁 Garante pasta de log
os.makedirs("logs", exist_ok=True)

# 📡 Inicializa conexão com MT5
if not mt5.initialize():
    print("❌ Não foi possível iniciar o MetaTrader 5.")
    exit()

if not mt5.symbol_select(SYMBOL, True):
    print(f"❌ Não foi possível selecionar o ativo {SYMBOL}")
    mt5.shutdown()
    exit()

print(f"🚀 Iniciando leitura do fluxo para {SYMBOL}...\n")

# 💾 Abre arquivo de log CSV
with open(CAMINHO_LOG, mode="a", newline="") as f:
    writer = csv.writer(f)
    if os.stat(CAMINHO_LOG).st_size == 0:
        writer.writerow(["timestamp", "open", "high", "low", "close", "tick_volume", "book_snapshot"])

    # 🔄 Loop infinito
    while True:
        rates = mt5.copy_rates_from_pos(SYMBOL, mt5.TIMEFRAME_M1, 0, 1)
        book = mt5.market_book_get(SYMBOL)
        timestamp = datetime.now().strftime('%H:%M:%S')

        if rates is None or len(rates) == 0:
            print("⚠️ Candle não disponível.")
            time.sleep(2)
            continue

        # 🧾 Candle atual
        df = pd.DataFrame(rates)
        candle = df.iloc[0]
        print(f"\n📅 {timestamp} — {SYMBOL}")
        print("📈 Último Candle:")
        print(candle[['open', 'high', 'low', 'close', 'tick_volume']])

        # 📘 Book
        if book:
            snapshot = []
            compra_total = 0
            venda_total = 0

            print("📘 Book de Ofertas:")
            for entry in book:
                lado = "🟢 Compra" if entry.type == mt5.BOOK_TYPE_BUY else "🔴 Venda"
                print(f"{lado} | R$ {entry.price:.2f} | Vol: {entry.volume}")
                snapshot.append(f"{'B' if entry.type == 1 else 'A'}:{entry.price:.2f}:{entry.volume}")

                if entry.type == 1:
                    compra_total += entry.volume
                else:
                    venda_total += entry.volume

            # 🧠 Tape Reading simples
            delta = compra_total - venda_total
            if delta > 20000:
                print(f"🔥 Pressão de compra detectada (+{delta} lotes)")
            elif delta < -20000:
                print(f"🔻 Pressão de venda detectada ({delta} lotes)")
            else:
                print(f"⚖️ Mercado relativamente equilibrado (∆ {delta})")

            # 🔊 Alerta sonoro se houver grande lote
            if any(entry.volume > VOLUME_ALERTA for entry in book):
                winsound.Beep(750, 400)
                print("🔔 Volume institucional detectado!")

            # 💾 Salva no CSV
            writer.writerow([
                timestamp,
                candle["open"],
                candle["high"],
                candle["low"],
                candle["close"],
                candle["tick_volume"],
                "|".join(snapshot)
            ])
            f.flush()

        else:
            print("⚠️ Livro de ofertas indisponível.")

        time.sleep(2)
