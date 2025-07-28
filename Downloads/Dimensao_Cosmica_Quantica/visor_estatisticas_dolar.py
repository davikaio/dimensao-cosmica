# ======================== BLOCO B — Estatísticas dos Dados ========================
import pandas as pd

CAMINHO_DADOS = "dados_dolar.csv"

try:
    df = pd.read_csv(CAMINHO_DADOS, sep=",", on_bad_lines="skip")
    df["close"] = pd.to_numeric(df["close"], errors="coerce")
    df["volume"] = pd.to_numeric(df["volume"], errors="coerce")

    print("\n📊 DADOS DO CSV — TABELA COMPLETA:\n")
    print(df)

    # 📈 Estatísticas básicas
    media_dolar = df["close"].mean()
    max_dolar = df["close"].max()
    min_dolar = df["close"].min()
    total_volume = df["volume"].sum()

    # 📊 Contagem de sinais
    sinais = df["sinal"].value_counts()

    print("\n📊 ESTATÍSTICAS DO DÓLAR:\n")
    print(f"🌡️ Média de cotação: R$ {media_dolar:.2f}")
    print(f"🚀 Cotação máxima: R$ {max_dolar:.2f}")
    print(f"🧲 Cotação mínima: R$ {min_dolar:.2f}")
    print(f"📦 Volume total negociado: {total_volume:,}")

    print("\n📊 CONTAGEM DE SINAIS:")
    for tipo, contagem in sinais.items():
        print(f"🔹 {tipo}: {contagem}")

except FileNotFoundError:
    print("⚠️ Arquivo 'dados_dolar.csv' não encontrado.")
