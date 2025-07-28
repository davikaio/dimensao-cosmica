import os
import time
import webbrowser
from datetime import datetime
from pathlib import Path

# Caminho base do projeto
CAMINHO_PROJETO = Path(__file__).resolve().parents[1]
CAMINHO_ENV = CAMINHO_PROJETO / "ciborna_env2" / "Scripts" / "activate"

# Saudação no terminal
print("=" * 50)
print("🚀 CIBORNA SYSTEM LAUNCHER v1.0")
print(f"🧠 Comandante: Wiliam")
print(f"🕐 Horário de lançamento: {datetime.now().strftime('%H:%M:%S')}")
print("=" * 50)

# Ativa o ambiente virtual e roda o cockpit
print("⏳ Ativando o ambiente virtual...")
time.sleep(1)

os.system(f'start powershell -NoExit -Command "& {CAMINHO_ENV}.ps1; streamlit run cosmos.py"')

# Abre o navegador no endereço certo após 3s
time.sleep(3)
webbrowser.open("http://localhost:8501")
