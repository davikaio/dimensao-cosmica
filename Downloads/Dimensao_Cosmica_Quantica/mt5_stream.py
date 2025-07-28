import MetaTrader5 as mt5
import pandas as pd

def obter_candle_e_book(ativo="PETR4"):
    if not mt5.initialize():
        raise RuntimeError("❌ Não foi possível inicializar o MetaTrader 5.")

    if not mt5.symbol_select(ativo, True):
        raise RuntimeError(f"❌ Ativo '{ativo}' não foi encontrado ou não pôde ser selecionado.")

    rates = mt5.copy_rates_from_pos(ativo, mt5.TIMEFRAME_M1, 0, 1)
    book = mt5.market_book_get(ativo)

    df = pd.DataFrame(rates) if rates is not None else pd.DataFrame()
    return df, book
