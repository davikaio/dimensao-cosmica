from flask import Flask, jsonify
import MetaTrader5 as mt5
import pandas as pd

app = Flask(__name__)

@app.route("/dados")
def dados_mt5():
    if not mt5.initialize():
        return jsonify({"erro": "Não foi possível iniciar o MetaTrader 5"})

    symbol = "WIN$N"  # Altere aqui se quiser outro ativo
    if not mt5.symbol_select(symbol, True):
        mt5.shutdown()
        return jsonify({"erro": f"Não foi possível selecionar o ativo {symbol}"})

    ticks = mt5.copy_ticks_from(symbol, pd.Timestamp.now() - pd.Timedelta("1m"), 500, mt5.COPY_TICKS_ALL)
    df = pd.DataFrame(ticks)
    mt5.shutdown()

    if df.empty:
        return jsonify({"erro": "Sem dados disponíveis"})

    return jsonify(df.tail(10).to_dict(orient="records"))

if __name__ == "__main__":
    app.run(port=5000)
