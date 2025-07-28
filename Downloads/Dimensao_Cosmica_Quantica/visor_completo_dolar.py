
# # =================== BLOCO A — Leitura do CSV com tabulação ===================
import pandas as pd

CAMINHO_DADOS = "dados_dolar.csv"

try:
    # 🔄 Leitura com separador de tabulação
    df = pd.read_csv(CAMINHO_DADOS, sep="\t", on_bad_lines="skip")

    print("\n📊 Prévia dos dados:")
    print(df.head())

    print("\n🧪 Tipos de cada coluna:")
    print(df.dtypes)

    # ✅ Conversão das colunas numéricas
    df["close"] = pd.to_numeric(df.get("close", 0), errors="coerce")
    df["volume"] = pd.to_numeric(df.get("volume", 0), errors="coerce")

    print("\n🩺 Valores ausentes por coluna:")
    print(df.isnull().sum())

# =================== BLOCO B — Estatísticas dos Dados ===================
    print("\n📈 ESTATÍSTICAS DE COTAÇÃO:\n")
    print(f"🌡️ Média do dólar: R$ {df['close'].mean():.2f}")
    print(f"📈 Cotação máxima: R$ {df['close'].max():.2f}")
    print(f"📉 Cotação mínima: R$ {df['close'].min():.2f}")

    print("\n📦 ESTATÍSTICAS DE VOLUME NEGOCIADO:\n")
    print(f"🔢 Total: {df['volume'].sum():,}")
    print(f"📊 Média por tick: {df['volume'].mean():,.0f}")
    print(f"📈 Pico de volume: {df['volume'].max():,}")

    print("\n🧠 CONTAGEM DE SINAIS OPERACIONAIS:\n")
    sinais = df["sinal"].value_counts()
    for tipo, contagem in sinais.items():
        print(f"🔹 {tipo}: {contagem} operações")

# =================== BLOCO C — Análise de Reversões de Sinal ===================
    reversoes = 0
    for i in range(1, len(df)):
        if df["sinal"].iloc[i] != df["sinal"].iloc[i - 1]:
            reversoes += 1

    print(f"\n🔄 Reversões de sinal detectadas: {reversoes}")
    print("📌 Exemplo de sequência:")
    print(df["sinal"].head(10).tolist())

except FileNotFoundError:
    print("⚠️ Arquivo 'dados_dolar.csv' não encontrado.")
except Exception as e:
    print("❌ Erro ao processar os dados:")
    print(f"Detalhes: {e}")
=================== BLOCO D — Gráfico da Cotação Temporal ===================
import matplotlib.pyplot as plt

try:
    # 🔄 Verifica se 'data' e 'close' existem e estão prontos
    if "data" in df.columns and "close" in df.columns:
        # Converte coluna de datas se necessário
        df["data"] = pd.to_datetime(df["data"], errors="coerce")

        # Remove linhas inválidas
        df_plot = df.dropna(subset=["data", "close"])

        # 🎨 Criação do gráfico
        plt.figure(figsize=(10, 4))
        plt.plot(df_plot["data"], df_plot["close"], marker="o", color="teal")
        plt.title("📈 Variação da Cotação do Dólar")
        plt.xlabel("Data")
        plt.ylabel("Valor (R$)")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()

        # 🚀 Exibe gráfico
        plt.show()
    else:
        print("⚠️ Colunas 'data' ou 'close' não disponíveis para gráfico.")

except Exception as e:
    print("❌ Erro ao gerar o gráfico:")
    print(f"Detalhes: {e}")
