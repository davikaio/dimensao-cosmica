import subprocess
import os
import platform

# Caminho do ambiente virtual
env_path = r"ciborna_env2\Scripts\activate.bat" if platform.system() == "Windows" else "source ciborna_env2/bin/activate"

# Mensagem visual de boas-vindas
print("\n🛸 Iniciando cockpit neural da Ciborna...")
print("🔁 Ativando ambiente virtual...\n")

# Ativa o ambiente e roda o Streamlit
try:
    if platform.system() == "Windows":
        comando = f'{env_path} && streamlit run cosmos.py'
        subprocess.run(["cmd.exe", "/k", comando])
    else:
        # Linux/macOS
        subprocess.run(f'source {env_path} && streamlit run cosmos.py', shell=True, executable="/bin/bash")

except Exception as e:
    print(f"❌ Erro ao iniciar a Ciborna: {e}")
