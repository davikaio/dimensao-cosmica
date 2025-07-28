import os
import glob
import datetime
import subprocess
import shutil

# 🗂️ Garante que a pasta logs/ exista
os.makedirs("logs", exist_ok=True)

# 🕒 Gera nome único pro relatório com data/hora
agora = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
html_report = f"logs/relatorio_{agora}.html"

# 🧪 Comando de execução do Pytest + relatório HTML autônomo
comando = [
    "pytest",
    "tests/",
    f"--html={html_report}",
    "--self-contained-html"
]

# ▶️ Executando testes...
print(f"🧪 Executando testes... HTML salvo em:\n   📄 {html_report}\n")
subprocess.run(comando)

# ✅ Mensagem final
print("\n✅ Testes concluídos!")

# 🧹 Mantém apenas os 3 relatórios mais recentes
relatorios = sorted(glob.glob("logs/relatorio_*.html"), reverse=True)
for old in relatorios[3:]:
    os.remove(old)
    print(f"🗑️ Removido relatório antigo: {old}")

# 📦 Compacta o relatório mais recente (opcional)
zip_name = "relatorio_teste.zip"
if os.path.exists(html_report):
    shutil.make_archive("relatorio_teste", "zip", "logs", os.path.basename(html_report))
    print(f"📦 Relatório compactado: {zip_name}")
