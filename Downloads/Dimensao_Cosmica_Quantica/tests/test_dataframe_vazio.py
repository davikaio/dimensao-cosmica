import pandas as pd
import sys
import os

# ✅ Garante que o diretório 'utils/' seja visível no PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.validador_dados import verificar_dataframe_vazio

print("▶️ Iniciando verificação de DataFrames...\n")

# 🔎 Caso 1: df = None
df1 = None
resultado1 = verificar_dataframe_vazio(df1)
print(f"🧪 Caso 1 (None) → Resultado: {resultado1}")
assert resultado1 == "NULO", "❌ Falha ao detectar df=None como NULO"

# 🔎 Caso 2: DataFrame vazio
df2 = pd.DataFrame()
resultado2 = verificar_dataframe_vazio(df2)
print(f"🧪 Caso 2 (DataFrame vazio) → Resultado: {resultado2}")
assert resultado2 == "VAZIO", "❌ Falha ao detectar DataFrame vazio como VAZIO"

# 🔎 Caso 3: DataFrame com dados
df3 = pd.DataFrame({"a": [1, 2, 3]})
resultado3 = verificar_dataframe_vazio(df3)
print(f"🧪 Caso 3 (DataFrame preenchido) → Resultado: {resultado3}")
assert resultado3 == "OK", "❌ Falha ao detectar DataFrame preenchido como OK"

print("\n✅ Todos os testes passaram com sucesso!\n")
