import os

# Lista de caminhos esperados (adicione ou remova conforme seu projeto)
ARQUIVOS_REQUERIDOS = {
    "DADOS DO DÓLAR": os.path.join("logs", "dados_dolar.csv"),
    "MEMÓRIA NEURAL": os.path.join("logs", "memoria_neural.csv"),
    "REPLAY IA": os.path.join("logs", "execucoes_replay_ia.csv"),
    "REPLAY PROFIT": os.path.join("replay", "replay_profit.csv"),
    "PROTÓTIPO ROBO": os.path.join("logs", "ciborna_ntx_prototipo.csv"),
    "ESTRATÉGIA PROFIT": os.path.join("logs", "estrategia_profit_tecnica.csv")
}

def validar_arquivos(base_dir):
    print("🚦 Verificando arquivos essenciais para inicialização...\n")

    for nome, caminho_relativo in ARQUIVOS_REQUERIDOS.items():
        caminho_absoluto = os.path.join(base_dir, caminho_relativo)
        if os.path.exists(caminho_absoluto):
            print(f"✅ {nome}: localizado com sucesso em {caminho_absoluto}")
        else:
            print(f"⚠️ {nome}: ARQUIVO NÃO ENCONTRADO em {caminho_absoluto}")

    print("\n📋 Validação concluída.\n")

# Exemplo de uso no script principal
if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    validar_arquivos(BASE_DIR)
