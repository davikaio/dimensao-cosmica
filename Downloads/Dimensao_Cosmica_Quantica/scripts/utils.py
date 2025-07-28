# ======================================
# 📦 utils.py — Funções auxiliares da Cabine Ciborna
# ======================================
import pandas as pd

def check_colunas(df: pd.DataFrame, colunas_esperadas: list):
    faltando = [col for col in colunas_esperadas if col not in df.columns]
    if faltando:
        raise ValueError(f"🛑 Colunas faltando no DataFrame: {faltando}")
    return True
