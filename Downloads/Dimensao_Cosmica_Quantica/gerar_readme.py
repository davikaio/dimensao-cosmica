"""
gerar_readme.py · Monta automaticamente o README.md com base na estrutura do projeto

Por: Comandante Wiliam 🛸
"""

import os

titulo = "# 🧠 Ciborna v1.0 · Plataforma Modular de Inteligência Financeira\n"
autor = "\n> Desenvolvido por: **Comandante Wiliam · Ciborna Systems 🛸**\n"

estrutura_header = "\n## 📁 Estrutura do Projeto (atual)\n\n```\n"
estrutura_footer = "```\n"

pastas_ignorar = {'.git', '.github', '__pycache__', 'venv', 'env', '.env'}

def montar_estrutura(diretorio, prefixo=""):
    linhas = []
    for item in sorted(os.listdir(diretorio)):
        if item in pastas_ignorar or item.startswith("."):
            continue
        caminho = os.path.join(diretorio, item)
        if os.path.isdir(caminho):
            linhas.append(f"{prefixo}├── {item}/")
            linhas.extend(montar_estrutura(caminho, prefixo + "│   "))
        else:
            linhas.append(f"{prefixo}├── {item}")
    return linhas

def gerar_readme():
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(titulo)
        f.write(autor)

        f.write("\n## 🚀 Como rodar os testes\n")
        f.write("```bash\npython bootstrap_tests.py\n```\n")

        f.write("\nRelatórios gerados automaticamente em `/logs/`\n")

        f.write("\n## 📦 Instalar dependências\n")
        f.write("```bash\npip install -r requirements.txt\n```\n")

        f.write(estrutura_header)
        estrutura = montar_estrutura(".")
        for linha in estrutura:
            f.write(linha + "\n")
        f.write(estrutura_footer)

        f.write("\n## 🧠 Diagnóstico de Dados\n")
        f.write("- `resumo_estatistico(df)`\n")
        f.write("- `relatorio_nulos(df)`\n")
        f.write("- `verificar_constantes(df)`\n")

        f.write("\n---\n")
        f.write("**Ciborna** · Sistema supervisionado por astúcia, código e café ☕🛸")

    print("✅ README.md gerado com sucesso!")

if __name__ == "__main__":
    gerar_readme()
