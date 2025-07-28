import os

# Caminho base
base_path = "C:/Dimensao_Cosmica_Quantica/ciborna/core"

# Criar pasta core
os.makedirs(base_path, exist_ok=True)

# Criar arquivos internos
arquivos = ['StrategyEngine.py', 'Executor.py', 'DataBridge.py', 'RiskManager.py', '__init__.py']
for nome in arquivos:
    with open(os.path.join(base_path, nome), 'w') as f:
        f.write("# " + nome + " - módulo da Ciborna\n")

print("✅ Subpasta 'core' criada com sucesso!")
