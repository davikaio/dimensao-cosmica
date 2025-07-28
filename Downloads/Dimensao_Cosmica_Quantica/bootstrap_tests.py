import os
import glob
import datetime
import subprocess
import shutil

# 🗂️ Cria pastas necessárias
os.makedirs("logs", exist_ok=True)
os.makedirs("exports", exist_ok=True)

# 🕒 Gera timestamp
agora = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
html_nome = f"relatorio_{agora}.html"
html_caminho = os.path.join("logs", html_nome)

# 🧪 Executa os testes com geração de HTML
comando = [
    "pytest",
    "tests/",
    f"--html={html_caminho}",
    "--self-contained-html"
]

print(f"🧪 Executando testes... HTML salvo em:\n   📄 {html_caminho}\n")
subprocess.run(comando)
print("\n✅ Testes concluídos!")

# 🧹 Remove relatórios antigos (mantém só os 3 mais recentes)
relatorios = sorted(glob.glob("logs/relatorio_*.html"), reverse=True)
for antigo in relatorios[3:]:
    os.remove(antigo)
    print(f"🗑️ Removido: {antigo}")

# 📦 Compacta o relatório mais recente para exports/
zip_base = f"relatorio_ciborna_{agora}"
zip_destino = os.path.join("exports", f"{zip_base}.zip")

shutil.make_archive(zip_base, "zip", "logs", html_nome)
shutil.move(f"{zip_base}.zip", zip_destino)
print(f"📦 Compactado em: {zip_destino}")
