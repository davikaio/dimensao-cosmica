
def run(candle=None, silent=False):
    if not candle:
        return {"acao": None, "detalhe": "Sem candle fornecido"}
    acao = "comprar" if candle["close"] > candle["open"] else "vender"
    return {"acao": acao, "detalhe": f"Fechamento: {candle['close']}, Abertura: {candle['open']}"}
