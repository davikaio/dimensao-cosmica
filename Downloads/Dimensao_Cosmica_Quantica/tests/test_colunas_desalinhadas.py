import pandas as pd

# Detecta automaticamente colunas com tamanhos diferentes
dados = {
    "col1": [1, 2, 3],
    "col2": [4, 5],
    "col3": [6, 7, 8]
}

for nome, coluna in dados.items():
    print(f"{nome} → tamanho: {len(coluna)}")

tamanhos = [len(coluna) for coluna in dados.values()]
if len(set(tamanhos)) != 1:
    print("⚠️ Colunas desalinhadas detectadas.")
else:
    print("✅ Todas as colunas têm o mesmo tamanho.")
