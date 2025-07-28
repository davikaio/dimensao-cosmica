"""
Executa todos os arquivos de teste/simulação na pasta /tests
"""

import os
import sys

# Adiciona o diretório raiz do projeto ao path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

print("=" * 50)
print("🧪 Iniciando execução de TODOS os testes da pasta /tests")
print("=" * 50)

testes = [
    "simulador_execucao_estrategia.py",
    "simulador_previsao_vazia.py",
    "test_colunas_desalinhadas.py",
    "test_dataframe_erro_len.py",
    "test_dataframe_ok.py",
    "verifica_dataframe_integridade.py"
]

falhas = []

for nome in testes:
    print(f"\n▶️ Executando: {nome}")
    try:
        caminho = os.path.join(os.path.dirname(__file__), nome)
        with open(caminho, encoding="utf-8") as f:
            exec(f.read(), {})
    except Exception as e:
        print(f"❌ Erro durante a execução:\n{e}")
        falhas.append(nome)

# Resumo final
print("\n" + "=" * 50)
if falhas:
    print(f"❌ {len(falhas)} teste(s) apresentaram erro:")
    for nome in falhas:
        print(f"  - {nome}")
else:
    print("✅ Todos os testes foram executados com sucesso!")
print("=" * 50)
