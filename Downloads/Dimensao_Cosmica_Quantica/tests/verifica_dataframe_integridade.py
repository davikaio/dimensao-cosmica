import pandas as pd

# Simula DataFrame e verifica se todas colunas têm mesmo número de linhas
df = pd.DataFrame({
    "a": [1, 2, 3],
    "b": [4, 5, 6],
    "c": [7, 8, 9]
})

linhas = len(df)
colunas_ok = all(len(df[col]) == linhas for col in df.columns)

if colunas_ok:
    print("✅ DataFrame íntegro.")
else:
    print("❌ Falha: colunas com tamanhos diferentes.")
