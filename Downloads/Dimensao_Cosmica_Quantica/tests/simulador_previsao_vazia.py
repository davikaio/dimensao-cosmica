"""
Simula a chamada da função prever() com um DataFrame vazio.
"""

import pandas as pd
from utils.validador_dados import check_colunas

# Simula DataFrame vazio
df_vazio = pd.DataFrame()

print("▶️ Simulando prever() com DataFrame vazio...")
try:
    if not check_colunas(df_vazio):
        print("✅ A função corretamente identificou um DataFrame vazio.")
    else:
        print("⚠️ Algo inesperado: passou um DataFrame vazio como válido.")
except Exception as e:
    print(f"❌ Erro durante a simulação: {e}")
