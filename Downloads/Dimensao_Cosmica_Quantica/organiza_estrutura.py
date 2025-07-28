"""
organiza_estrutura.py · Script para reorganizar arquivos da raiz para subpastas.
Por: Comandante Wiliam · Ciborna Systems
"""

import os
import shutil

# Mapeamento por extensão → pasta
mapa_pastas = {
    ".csv": "data",
    ".xlsx": "data",
    ".txt": "docs",
    ".md": "docs",
    ".exe": "instaladores",
    ".whl": "instaladores",
    ".bat": "scripts",
    ".sh": "scripts",
    ".ipynb": "notebooks"
}

# Cria as pastas se não existirem
for pasta in set(mapa_pastas.values()):
    os.makedirs(pasta, exist_ok=True)

# Move os arquivos
for arquivo in os.listdir():
    if os.path.isfile(arquivo):
        _, ext = os.path.splitext(arquivo)
        destino = mapa_pastas.get(ext.lower())
        if destino:
            print(f"📦 Movendo {arquivo} → {destino}/")
            shutil.move(arquivo, os.path.join(destino, arquivo))

print("✅ Reorganização concluída com sucesso!")
