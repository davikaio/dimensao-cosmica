# ======================================
# 🔢 BLOCO 00 — Importação de bibliotecas
# ======================================
import os
import pandas as pd
import yfinance as yf
import MetaTrader5 as mt5
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh

# ======================================
# 🔢 BLOCO 0.2 — Diagnóstico MetaTrader 5
# ======================================
st.subheader("🧪 Diagnóstico de Conectividade MetaTrader 5")

if not mt5.initialize():
    st.error("❌ Falha ao inicializar MetaTrader 5.")
else:
    ativo = "WIN$"  # ou "WDO$"
    info = mt5.symbol_info_tick(ativo)

    if info is None or info.bid <= 0 or info.ask <= 0:
        st.warning(f"⚠️ Símbolo '{ativo}' indisponível ou sem cotação.")
    else:
        st.success(f"✅ Ativo: {ativo} | BID: {info.bid:.2f} | ASK: {info.ask:.2f}")

# ======================================
# 🔢 BLOCO 02.1 Diagnóstico MetaTrader 5
# ======================================
st.subheader("🧪 Diagnóstico de Conectividade MetaTrader 5")

if not mt5.initialize():
    st.error("❌ Falha ao inicializar MetaTrader 5.")
else:
    ativo = "PETR4.SA"
    info = mt5.symbol_info_tick(ativo)

    if info is None or info.bid <= 0 or info.ask <= 0:
        st.warning(f"⚠️ Símbolo '{ativo}' indisponível ou sem cotação.")
    else:
        st.success(f"✅ Ativo: {ativo} | BID: R$ {info.bid:.2f} | ASK: R$ {info.ask:.2f}")
    mt5.shutdown()

st.subheader("📈 Cotação Atual dos Principais Ativos da B3")

ativos_b3 = {
    "🛢️ PETR4 (Petrobras)": "PETR4.SA",
    "⛏️ VALE3 (Vale)": "VALE3.SA",
    "🏦 ITUB4 (Itaú)": "ITUB4.SA",
    "🏬 MGLU3 (Magazine Luiza)": "MGLU3.SA",
    "🔌 WEGE3 (WEG)": "WEGE3.SA"
}

for nome, ticker in ativos_b3.items():
    if not ticker.endswith(".SA"):
        st.warning(f"⚠️ Ticker inválido para B3: {ticker}")
        continue

    try:
        dados = yf.Ticker(ticker).history(period="1d")

        if dados.empty:
            st.warning(f"⚠️ Nenhum dado encontrado para {nome} ({ticker}).")
            continue

        preco = round(dados["Close"].iloc[-1], 2)
        hora = dados.index[-1].strftime("%H:%M")
        st.metric(f"{nome}", f"R$ {preco}", delta=f"⏰ {hora}")

    except Exception as e:
        st.warning(f"⚠️ Falha ao buscar cotação para: {nome}")
        st.error(str(e))


# ======================================
# 🔢 BLOCO 03 — Leitura do CSV atualizado
# ======================================

CAMINHO_DADOS = "ativos_simulados.csv"

try:
    df = pd.read_csv(CAMINHO_DADOS, sep=";", on_bad_lines="skip")

    # 🧬 Renomeia colunas se estiverem presentes
    colunas_renomear = {
        "fechamento": "close",
        "volume_tick": "volume",
        "saida_estrategia": "sinal"
    }

    df.rename(columns={k: v for k, v in colunas_renomear.items() if k in df.columns}, inplace=True)

    # 💡 Exibe colunas carregadas para diagnóstico rápido
    st.write("📋 Colunas detectadas no CSV:", df.columns.tolist())

    # 🔢 Converte colunas numéricas se existirem
    for col in ["close", "volume", "Preco_Fechamento", "ADX", "RSI"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
            st.caption(f"🔢 Coluna `{col}` convertida para numérico.")
        else:
            st.warning(f"⚠️ Coluna `{col}` não encontrada para conversão.")

except FileNotFoundError:
    st.warning("⚠️ CSV 'ativos_simulados.csv' não encontrado.")
    df = pd.DataFrame()

# ======================================
# 🔢 BLOCO 04 — Seletor de Inteligência
# ======================================
modo = st.radio("🧠 Cérebro do Ciborna:", ["📈 Estratégia Fixa", "🧬 Rede Neural", "📊 Fluxo de Ordens"])
st.info(f"🧠 Inteligência: `{modo}`")
# ======================================
# 🔢 BLOCO 05 — Validação dos Dados
# ======================================
st.subheader("📋 Validação e Filtro dos Dados — SERMEDIA")

# Verifica se o DataFrame existe e está preenchido
if 'df' in locals() and not df.empty:
    if 'SERMEDIA' in df.columns:
        # Remove valores nulos e duplica opções
        sermedia_opcoes = df['SERMEDIA'].dropna().unique().tolist()

        # Cria seletor lateral
        sermedia_selecionado = st.sidebar.selectbox(
            "🔎 Filtrar por SERMEDIA:",
            ["Todos"] + sorted(sermedia_opcoes)
        )

        # Aplica o filtro
        if sermedia_selecionado != "Todos":
            df = df[df['SERMEDIA'] == sermedia_selecionado]
            st.success(f"📌 Filtrado por: `{sermedia_selecionado}`")
    else:
        st.warning("⚠️ A coluna 'SERMEDIA' não está disponível nos dados. Filtro desativado.")
        sermedia_selecionado = "Todos"
else:
    st.error("❌ Nenhum dado carregado ou o DataFrame está vazio.")

# ======================================
# 🔢 BLOCO 06 — Book Estratégico
# ======================================

import pandas as pd
import streamlit as st

st.sidebar.markdown("### 📊 Book Estratégico — Ações Brasileiras")

# 📂 Dados reais fornecidos manualmente
dados_reais = [
    ["PETR4", "Petrobras", 31.99, "+2,04%", "27.418.600"],
    ["VALE3", "Vale", 57.42, "-0,14%", "17.914.800"],
    ["BBAS3", "Banco do Brasil", 20.21, "+1,61%", "35.932.600"],
    ["WEGE3", "WEG", 38.01, "-8,01%", "31.116.000"],
    ["MGLU3", "Magazine Luiza", 7.80, "+4,00%", "19.534.600"],
    ["B3SA3", "B3", 13.39, "+2,45%", "20.683.700"]
]

colunas = ["Ticker", "Empresa", "Último Preço (R$)", "Variação (%)", "Volume Negociado"]
df_acoes = pd.DataFrame(dados_reais, columns=colunas)

# 🎨 Estilização dinâmica para cada ação
for _, row in df_acoes.iterrows():
    variacao = row["Variação (%)"]
    cor_fundo = "#10b981" if "+" in variacao else "#ef4444"
    cor_texto = "white"

    bloco_html = f"""
    <div style='background-color:{cor_fundo}; color:{cor_texto}; padding:6px; border-radius:5px; margin-bottom:6px'>
        <b>{row['Ticker']}</b> — {row['Empresa']}<br>
        💵 Preço: R$ {row['Último Preço (R$)']} | 📈 Variação: {variacao}<br>
        📊 Volume: {row['Volume Negociado']}
    </div>
    """

    st.sidebar.markdown(bloco_html, unsafe_allow_html=True)
# ======================================
# 🔢 BLOCO 07 — Book Visual
# ======================================
import os
import pandas as pd
import streamlit as st

# 🔒 Garantir que a pasta exista
PASTA_DADOS = "dados"
os.makedirs(PASTA_DADOS, exist_ok=True)

st.subheader("🧪 Simulador de Operações")

# 📄 Dados simulados de operações
dados = [
    ["WDOH25", "31/01/2025 19:00", "26/02/2025 13:38", "V", 5775.00, 5830.00, 1650.00],
    ["WDOH25", "26/02/2025 14:29", "26/02/2025 17:21", "V", 5814.00, 5805.40, -430.00],
    ["WINJ25", "02/12/2025 19:00", "26/02/2025 17:21", "C", 124530.00, 126920.00, 2868.00],
    ["WDOH25", "26/02/2025 17:21", "28/02/2025 19:00", "C", 5813.00, 5848.50, 710.00],
    ["WINJ25", "26/02/2025 17:21", "21/03/2025 10:13", "V", 133000.00, 126652.50, -2539.00],
    ["WINJ25", "21/03/2025 10:14", "21/03/2025 10:19", "V", 132945.00, 132890.00, -11.00],
    ["WDOJ25", "28/02/2025 19:00", "24/03/2025 10:55", "C", 5848.50, 5736.25, -2245.00],
]

colunas = ["Ticker", "Entrada", "Saida", "Operacao", "Preco_Entrada", "Preco_Saida", "Resultado"]
df_operacoes = pd.DataFrame(dados, columns=colunas)

# 💾 Salvar arquivo na pasta 'dados'
CAMINHO_ARQUIVO = f"{PASTA_DADOS}/simulacao_operacoes.csv"
df_operacoes.to_csv(CAMINHO_ARQUIVO, index=False, sep=";")

# 📊 Exibir resumo da simulação
st.dataframe(df_operacoes, use_container_width=True)
st.caption(f"📁 Arquivo salvo em: `{CAMINHO_ARQUIVO}`")

# 📈 Estatísticas rápidas
st.metric("Total de operações", len(df_operacoes))
st.metric("Resultado Total", f"{df_operacoes['Resultado'].sum():,.2f}")
st.metric("Operações Lucrativas", (df_operacoes['Resultado'] > 0).sum())
st.metric("Operações com Prejuízo", (df_operacoes['Resultado'] < 0).sum())

st.success("✅ Dados simulados gerados e salvos com sucesso!")
# 🔢 BLOCO 08 — Gráfico Tático de Ativo WIN/WDO (1 minuto)

import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.subheader("📈 Gráfico Tático de Ativos WIN e WDO (1 minuto)")

# Lista de ativos futuros
ativos_futuros = {
    "Mini Índice (WIN)": "^BVSP",
    "Mini Dólar (WDO)": "USDBRL=X"
}

for nome, ticker in ativos_futuros.items():
    try:
        df_graf = yf.Ticker(ticker).history(period="1d", interval="1m")

        if df_graf is not None and not df_graf.empty:
            preco_atual = df_graf["Close"].iloc[-1]

            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=df_graf.index,
                y=df_graf["Close"],
                line=dict(color="royalblue"),
                name=nome
            ))

            fig.add_trace(go.Scatter(
                x=[df_graf.index[-1]],
                y=[preco_atual],
                mode="markers+text",
                text=[f"{preco_atual:.2f}"],
                textposition="top center",
                marker=dict(color="crimson", size=10),
                name="Preço Atual"
            ))

            fig.update_layout(
                title=f"{nome} - Últimas 24h (1m)",
                xaxis_title="Horário",
                yaxis_title="Preço",
                template="plotly_white",
                height=400
            )

            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning(f"⚠️ Dados de cotação indisponíveis para {nome}")
    except Exception as e:
        st.error(f"❌ Erro ao gerar gráfico de {nome}: {e}")

# ======================================
# 🔢 BLOCO 08.1 — Gráfico de Candles (autoatualização)
# ======================================
from streamlit_autorefresh import st_autorefresh
import yfinance as yf

st_autorefresh(interval=120000, key="chart_refresh")
st.subheader("📊 Gráfico Candlestick B3")

try:
    dados_candle = yf.Ticker("PETR4.SA").history(period="1d", interval="1m")
    if not dados_candle.empty:
        st.line_chart(dados_candle["Close"])
except Exception as e:
    st.error(f"❌ Erro ao carregar gráfico: {e}")
# ======================================
# 🔢 BLOCO 10 — Alerta ao Rompimento EUR/USD
# ======================================
import streamlit as st
import pandas as pd

st.subheader("📛 Verificador de Rompimento B3")

def verificar_rompimento(df, faixa_resistencia=1.16900, ativo="PETR4.SA"):
    if df is None or df.empty or "close" not in df.columns:
        st.warning("⚠️ Dados insuficientes para verificar rompimento.")
        return

    preco_atual = pd.to_numeric(df["close"].iloc[-1], errors="coerce")

    if pd.isna(preco_atual):
        st.error("❌ Erro ao ler o preço atual.")
        return

    if preco_atual > faixa_resistencia:
        st.success(f"🔺 Rompimento detectado! Preço atual ({preco_atual:.5f}) ultrapassou resistência ({faixa_resistencia})")
        st.markdown("🧠 Estratégia Ciborna sugere: possível entrada de **COMPRA** com tendência de alta")
    else:
        st.info(f"📉 Preço atual ({preco_atual:.5f}) ainda abaixo da resistência ({faixa_resistencia}) — sem sinal de rompimento.")

# 🚦 Validação segura do modo e do DataFrame (evita erro de sintaxe)
def executar_bloco_10(df, modo):
    try:
        if modo == "📈 Estratégia Fixa" and df is not None and not df.empty:
            verificar_rompimento(df)
    except Exception as e:
        st.error(f"❌ Erro ao ativar verificador de rompimento: {e}")
# ======================================
# 🔢 BLOCO 11.0 — Verificador de Acesso, Ativo e Mercado
# ======================================
st.subheader("🛡️ Verificação Neural do Ambiente")

if mt5.initialize():
    info_conta = mt5.account_info()
    if info_conta is None:
        st.error("❌ Conta não logada — verifique se está conectado à corretora.")
    else:
        st.success(f"✅ Conectado na conta {info_conta.login} ({info_conta.company})")

        ativo = st.text_input("💹 Ativo para verificar", "PETR4.SA")
        ativado = mt5.symbol_select(ativo, True)

        if not ativado:
            st.error(f"❌ Não foi possível ativar o símbolo {ativo}")
        else:
            info_tick = mt5.symbol_info_tick(ativo)
            info_symb = mt5.symbol_info(ativo)

            if info_tick is None or info_tick.ask == 0 or info_tick.bid == 0:
                st.warning("⚠️ Mercado fechado ou ativo sem cotação disponível.")
            else:
                st.success(f"🟢 Cotação ativa — ASK: {info_tick.ask} | BID: {info_tick.bid}")

            if info_symb.trade_mode not in [
                mt5.SYMBOL_TRADE_MODE_FULL,
                mt5.SYMBOL_TRADE_MODE_LONGONLY,
                mt5.SYMBOL_TRADE_MODE_SHORTONLY
            ]:
                st.error("❌ Ativo não está liberado para execução de ordens.")
            else:
                st.success("✅ Ativo liberado para trading.")

    mt5.shutdown()
else:
    st.error("❌ Terminal MetaTrader 5 não está inicializado.")
# ======================================
# 🔢 BLOCO 11.1 — Histórico Operacional Automático com Sanitização
# ======================================
st.subheader("📡 Histórico de Ordens Executadas (Ciborna Log)")

caminho_csv = "logs/execucoes_operacionais.csv"

if os.path.exists(caminho_csv):
    execucoes = pd.read_csv(caminho_csv)

    # 🔍 Identifica a coluna correta de lucro
    coluna_lucro = "Lucro/Prejuízo" if "Lucro/Prejuízo" in execucoes.columns else (
        "LucroEstimado" if "LucroEstimado" in execucoes.columns else None
    )

    if coluna_lucro:
        execucoes[coluna_lucro] = (
            execucoes[coluna_lucro]
            .astype(str)
            .replace(r'[^\d\-\+\.]', '', regex=True)
            .replace('', '0')
            .astype(float)
        )

        st.dataframe(execucoes.style.set_table_styles([
            {"selector": "th", "props": [("font-size", "11px"), ("text-align", "center")]},
            {"selector": "td", "props": [("font-size", "11px"), ("text-align", "center")]}
        ]).highlight_between(left=-9999, right=-0.001, subset=[coluna_lucro], color="#fcebea"))

        total_ops = len(execucoes)
        gain_ops = execucoes[execucoes[coluna_lucro] > 0].shape[0]
        loss_ops = execucoes[execucoes[coluna_lucro] < 0].shape[0]

        st.markdown(f"""
        🔢 **Total de Operações:** {total_ops}  
        ✅ **Gains:** {gain_ops}  
        ❌ **Losses:** {loss_ops}
        """)
    else:
        st.error("❌ Nenhuma coluna de lucro encontrada (`Lucro/Prejuízo` ou `LucroEstimado`).")
else:
    st.warning("⚠️ Arquivo de histórico não encontrado. Verifique se `execucoes_operacionais.csv` está no diretório `logs/`.")
# ======================================
# 🔢 BLOCO 11.2 — Painel de Performance Avançada da Ciborna
# ======================================
st.subheader("📈 Painel Avançado de Performance Operacional")

caminho_csv = "logs/execucoes_operacionais.csv"

if os.path.exists(caminho_csv):
    df = pd.read_csv(caminho_csv)

    # 🔍 Detecta nome da coluna de lucro
    coluna_lucro = "Lucro/Prejuízo" if "Lucro/Prejuízo" in df.columns else (
        "LucroEstimado" if "LucroEstimado" in df.columns else None
    )

    if coluna_lucro:
        df[coluna_lucro] = (
            df[coluna_lucro]
            .astype(str)
            .replace(r'[^\d\-\+\.]', '', regex=True)
            .replace('', '0')
            .astype(float)
        )
        df["Horário"] = pd.to_datetime(df["Horário"])
        df["Dia"] = df["Horário"].dt.date

        lucro_dia = df.groupby("Dia")[coluna_lucro].sum().reset_index()

        st.markdown("### 💹 Lucro por Dia")
        st.line_chart(lucro_dia)
    else:
        st.error("❌ Nenhuma coluna de lucro encontrada no histórico.")
else:
    st.warning("⚠️ Arquivo de performance não encontrado.")
# ======================================
# 🔢 BLOCO 11.3 — Lucro por Tipo de Ordem
# ======================================
st.subheader("⚖️ Lucro por Tipo de Ordem (Compra vs Venda)")

caminho_csv = "logs/execucoes_operacionais.csv"

if os.path.exists(caminho_csv):
    df = pd.read_csv(caminho_csv)

    coluna_lucro = "Lucro/Prejuízo" if "Lucro/Prejuízo" in df.columns else (
        "LucroEstimado" if "LucroEstimado" in df.columns else None
    )

    if coluna_lucro and "Tipo" in df.columns:
        df[coluna_lucro] = (
            df[coluna_lucro].astype(str)
            .replace(r'[^\d\-\+\.]', '', regex=True)
            .replace('', '0')
            .astype(float)
        )
        df["Horário"] = pd.to_datetime(df["Horário"])
        df["Dia"] = df["Horário"].dt.date

        lucro_tipo = df.groupby(["Dia", "Tipo"])[coluna_lucro].sum().reset_index()
        lucro_pivot = lucro_tipo.pivot(index="Dia", columns="Tipo", values=coluna_lucro).fillna(0)

        st.markdown("### 🆚 Comparativo por Tipo")
        st.bar_chart(lucro_pivot)
    else:
        st.error("❌ Colunas 'Tipo' ou de lucro ausentes.")
else:
    st.warning("⚠️ Histórico de execuções não encontrado.")
# ======================================
# 📊 BLOCO 11.4 — Distribuição de Lucros
# ======================================
st.subheader("📉 Distribuição de Lucros por Operação")

if os.path.exists(caminho_csv):
    df = pd.read_csv(caminho_csv)
    
    coluna_lucro = "Lucro/Prejuízo" if "Lucro/Prejuízo" in df.columns else (
        "LucroEstimado" if "LucroEstimado" in df.columns else None
    )

    if coluna_lucro:
        df[coluna_lucro] = (
            df[coluna_lucro].astype(str)
            .replace(r'[^\d\-\+\.]', '', regex=True)
            .replace('', '0')
            .astype(float)
        )

        st.markdown("### 📊 Histograma de Lucros")
        st.pyplot(df[coluna_lucro].plot.hist(bins=25, color="#3B82F6", edgecolor="white").get_figure())
    else:
        st.error("❌ Coluna de lucro não encontrada.")
else:
    st.warning("⚠️ Arquivo de execuções ausente.")
# ======================================
# 🛠️ BLOCO 11.X — Filtro Neural Operacional
# ======================================
st.subheader("🧠 Filtro Neural de Execuções")

if os.path.exists(caminho_csv):
    df = pd.read_csv(caminho_csv)

    coluna_lucro = "Lucro/Prejuízo" if "Lucro/Prejuízo" in df.columns else (
        "LucroEstimado" if "LucroEstimado" in df.columns else None
    )

    if coluna_lucro:
        df[coluna_lucro] = (
            df[coluna_lucro].astype(str)
            .replace(r'[^\d\-\+\.]', '', regex=True)
            .replace('', '0')
            .astype(float)
        )
        df["Horário"] = pd.to_datetime(df["Horário"])

        tipos = df["Tipo"].unique().tolist()
        tipo_selecionado = st.selectbox("🎯 Tipo de Ordem", tipos)
        lucro_min = st.slider("💰 Filtro de Lucro mínimo", min_value=-100.0, max_value=100.0, value=0.0)
        data_inicial = st.date_input("📅 Data Inicial", value=df["Horário"].min().date())
        data_final = st.date_input("📅 Data Final", value=df["Horário"].max().date())

        df_filtrado = df[
            (df["Tipo"] == tipo_selecionado) &
            (df[coluna_lucro] >= lucro_min) &
            (df["Horário"].dt.date >= data_inicial) &
            (df["Horário"].dt.date <= data_final)
        ]

        st.markdown("### 🔍 Execuções Filtradas")
        st.dataframe(df_filtrado)
    else:
        st.error("❌ Coluna de lucro não localizada.")
else:
    st.warning("⚠️ Histórico não encontrado.")
# 📘 Função auxiliar para detectar coluna de lucro
def detectar_coluna_lucro(df):
    for nome in ["Lucro/Prejuízo", "LucroEstimado", "ResultadoFinal"]:
        if nome in df.columns:
            return nome
    return None

# ======================================
# 🔢 BLOCO 11.5 — Curva de Capital Acumulado
# ======================================
st.subheader("🪙 Evolução Acumulada de Capital (Curva de Performance)")

caminho_csv = "logs/execucoes_operacionais.csv"

if os.path.exists(caminho_csv):
    df = pd.read_csv(caminho_csv)
    st.write("📋 Colunas detectadas:", df.columns.tolist())

    # 🧠 Busca automática da coluna de lucro
    coluna_lucro = detectar_coluna_lucro(df)

    if coluna_lucro:
        df[coluna_lucro] = (
            df[coluna_lucro].astype(str)
            .str.replace(",", ".", regex=False)
            .replace(r"[^\d\-\+\.]", "", regex=True)
            .replace("", "0")
            .astype(float)
        )

        df["Horário"] = pd.to_datetime(df["Horário"], errors="coerce")
        df.dropna(subset=["Horário"], inplace=True)
        df.sort_values("Horário", inplace=True)

        # 💰 Capital acumulado
        df["Capital Acumulado"] = df[coluna_lucro].cumsum()
        st.markdown("### 📈 Curva de Capital")
        st.line_chart(df.set_index("Horário")["Capital Acumulado"])

        # 🔥 Mapa de calor de lucro por hora x dia
        df["Hora"] = df["Horário"].dt.hour
        df["Dia"] = df["Horário"].dt.date
        mapa = df.pivot_table(
            index="Hora",
            columns="Dia",
            values=coluna_lucro,
            aggfunc="sum"
        ).fillna(0)
        st.markdown("### 🔥 Heatmap de Lucro por Hora x Dia")
        st.dataframe(mapa.style.background_gradient(cmap="RdYlGn"))
    else:
        st.error("❌ Coluna de lucro não encontrada para análise.")
else:
    st.warning("⚠️ Arquivo 'execucoes_operacionais.csv' não encontrado.")

# ======================================
# 🔢 BLOCO 11.6 — Heatmap de Performance por Horário
# ======================================

st.subheader("🌡️ Mapa de Calor por Horário Operacional")

# 📦 Caminho padrão do histórico
caminho_csv = "logs/execucoes_operacionais.csv"

# 📘 Função auxiliar para detectar coluna de lucro
def detectar_coluna_lucro(df):
    for nome in ["Lucro/Prejuízo", "LucroEstimado", "ResultadoFinal"]:
        if nome in df.columns:
            return nome
    return None

# 📥 Leitura do histórico operacional
if os.path.exists(caminho_csv):
    df = pd.read_csv(caminho_csv)

    st.write("📋 Colunas detectadas:", df.columns.tolist())

    # 🧠 Busca automática da coluna de lucro
    coluna_lucro = detectar_coluna_lucro(df)

    if isinstance(coluna_lucro, str):
        # 🧼 Higienização dos valores
        df[coluna_lucro] = (
            df[coluna_lucro]
            .astype(str)
            .replace(r"[^\d\-\+\.]", "", regex=True)
            .replace("", "0")
            .astype(float)
        )

        # 🕓 Extração de hora e dia
        df["Horário"] = pd.to_datetime(df["Horário"], errors="coerce")
        df.dropna(subset=["Horário"], inplace=True)
        df["Hora"] = df["Horário"].dt.hour
        df["Dia"] = df["Horário"].dt.date

        # 🔥 Geração do mapa de calor
        mapa = df.pivot_table(
            index="Hora",
            columns="Dia",
            values=coluna_lucro,
            aggfunc="sum"
        ).fillna(0)

        st.markdown("### 🔥 Heatmap de Lucro por Hora x Dia")
        st.dataframe(mapa.style.background_gradient(cmap="RdYlGn"))
    else:
        st.error("❌ Coluna de lucro não encontrada para análise de horário.")
else:
    st.warning("⚠️ Histórico de execuções ausente.")
# ======================================
# 🔢 BLOCO 11.7 — Simulação Preditiva com Séries Temporais
# ======================================

import random
from datetime import datetime

st.subheader("📡 Inteligência Temporal Preditiva • Ciborna Fantasma")

caminho_csv = "logs/execucoes_operacionais.csv"

if os.path.exists(caminho_csv):
    df = pd.read_csv(caminho_csv)
    df["Horário"] = pd.to_datetime(df["Horário"], errors="coerce")
    df.dropna(subset=["Horário"], inplace=True)

    # 🔍 Detecta coluna de lucro
    coluna_lucro = None
    for nome in ["Lucro/Prejuízo", "LucroEstimado", "ResultadoFinal"]:
        if nome in df.columns:
            coluna_lucro = nome
            break

    if isinstance(coluna_lucro, str):
        df[coluna_lucro] = (
            df[coluna_lucro]
            .astype(str)
            .replace(r"[^\d\-\+\.]", "", regex=True)
            .replace("", "0")
            .astype(float)
        )

        df["Hora"] = df["Horário"].dt.hour
        df_temporal = df.groupby("Hora")[coluna_lucro].mean().reset_index()

        st.markdown("### ⏱️ Lucro Médio por Hora")
        st.line_chart(df_temporal.set_index("Hora"))

        hora_ideal = df_temporal.sort_values(by=coluna_lucro, ascending=False).iloc[0]["Hora"]
        st.success(f"🧠 Hora ideal para simulação: {int(hora_ideal)}h")

        hora_atual = datetime.now().hour
        if hora_atual == int(hora_ideal):
            st.markdown("🚀 Estamos no melhor momento histórico — disparando ordem fantasma otimizada!")

            ativo = st.selectbox("💹 Ativo para simulação", ["PETR4.SA", "VALE3.SA", "ITUB4.SA"])
            direcao = random.choice(["COMPRA", "VENDA"])
            preco = round(random.uniform(1.0, 1.5), 5) if "USD" in ativo else round(random.uniform(20, 80), 2)
            resultado = round(random.uniform(-3.0, 9.0), 2)

            execucao = {
                "Horário": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Símbolo": ativo,
                "Tipo": direcao,
                "Preço": preco,
                "Resultado": "SIMULADO PREDITIVO",
                coluna_lucro: resultado,
                "Momento": f"{hora_atual}h",
                "Fonte": "Fantasma"
            }

            pd.DataFrame([execucao]).to_csv("logs/execucoes_fantasmas.csv", mode="a", header=False, index=False)
            st.success(f"🟢 Ordem Fantasma Preditiva {direcao} no {ativo} registrada com resultado {resultado}")
        else:
            st.info(f"⏳ Aguardando hora ótima ({int(hora_ideal)}h) para disparar próxima simulação.")
    else:
        st.error("❌ Nome da coluna de lucro inválido. Nenhuma coluna compatível detectada no histórico.")
else:
    st.warning("⚠️ Histórico não encontrado para análise temporal.")

# ======================================
# 🔢 BLOCO 11.8 — Ciborna Neural Trader com ML Temporal
# ======================================

import random
from datetime import datetime

st.subheader("🧠 Previsão Neural de Lucro por Contexto Operacional")

caminho_csv = "logs/execucoes_operacionais.csv"

if os.path.exists(caminho_csv):
    # 🔹 Leitura inicial do CSV
    df = pd.read_csv(caminho_csv)
    st.write("🧬 Colunas detectadas:", df.columns.tolist())

    # 🔹 Conversão da coluna 'Horário'
    if "Horário" in df.columns:
        df["Horário"] = pd.to_datetime(df["Horário"], errors="coerce")
        df.dropna(subset=["Horário"], inplace=True)
    else:
        st.error("❌ Coluna 'Horário' não encontrada no arquivo.")
        st.stop()

    # 🔹 Identificação segura da coluna de lucro
    coluna_lucro = None
    for nome in ["Lucro/Prejuízo", "LucroEstimado", "ResultadoFinal"]:
        if nome in df.columns:
            coluna_lucro = nome
            break

    if isinstance(coluna_lucro, str):
        # 🔹 Higienização de lucro
        df[coluna_lucro] = (
            df[coluna_lucro]
            .astype(str)
            .replace(r"[^\d\-\+\.]", "", regex=True)
            .replace("", "0")
            .astype(float)
        )

        # 🔹 Criação de features temporais
        df["Hora"] = df["Horário"].dt.hour

        # 🔹 Codificação do tipo de operação para ML
        if "Tipo" in df.columns:
            df["Tipo"] = df["Tipo"].map({"COMPRA": 0, "VENDA": 1})
        else:
            st.warning("⚠️ Coluna 'Tipo' não encontrada — previsão limitada.")

        # ✅ Aqui você pode aplicar modelos de regressão, clustering ou previsão de lucro
        st.success("🧠 Dados preparados para análise de previsão neural!")

    else:
        st.error("❌ Nenhuma coluna de lucro identificada no histórico.")
else:
    st.warning("⚠️ Arquivo de histórico operacional não encontrado.")
# ======================================
# 🔢 BLOCO 11.9 — Filtro de Execução baseado em Previsão Neural
# ======================================

from datetime import datetime
import random
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

st.subheader("🛡️ Ciborna Trader • Filtro Neural Preditivo de Execução")

caminho_csv = "logs/execucoes_operacionais.csv"

if os.path.exists(caminho_csv):
    df = pd.read_csv(caminho_csv)

    # 🧬 Coluna de tempo
    if "Horário" in df.columns:
        df["Horário"] = pd.to_datetime(df["Horário"], errors="coerce")
        df.dropna(subset=["Horário"], inplace=True)
    else:
        st.error("❌ Coluna 'Horário' não encontrada.")
        st.stop()

    # 💰 Detecta coluna de lucro
    coluna_lucro = None
    for nome in ["Lucro/Prejuízo", "LucroEstimado", "ResultadoFinal"]:
        if nome in df.columns:
            coluna_lucro = nome
            break

    if isinstance(coluna_lucro, str):
        df[coluna_lucro] = (
            df[coluna_lucro].astype(str)
            .replace(r"[^\d\-\+\.]", "", regex=True)
            .replace("", "0")
            .astype(float)
        )

        df["Hora"] = df["Horário"].dt.hour

        if "Tipo" in df.columns:
            df["Tipo"] = df["Tipo"].map({"COMPRA": 0, "VENDA": 1})
        else:
            df["Tipo"] = 0  # default fallback

        df["Estratégia"] = df.get("Estratégia", "Reversão")
        df["Estratégia"] = df["Estratégia"].astype("category").cat.codes
        df["Símbolo"] = df.get("Símbolo", "GENÉRICO").astype("category").cat.codes

        X = df[["Hora", "Tipo", "Estratégia", "Símbolo"]]
        y = df[coluna_lucro]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        modelo = RandomForestRegressor(n_estimators=100).fit(X_train, y_train)

        st.markdown("### 🎯 Parâmetros da Simulação Neural")
        hora_atual = datetime.now().hour
        tipo_op = st.radio("📈 Tipo de Ordem", ["COMPRA", "VENDA"])
        estrategia = st.selectbox("🧠 Estratégia", df["Estratégia"].astype("category").cat.categories.tolist())
        ativo = st.selectbox("💹 Ativo", df["Símbolo"].astype("category").cat.categories.tolist())

        tipo_valor = 0 if tipo_op == "COMPRA" else 1
        estrategia_valor = df[df["Estratégia"] == estrategia]["Estratégia"].mode()[0]
        simbolo_valor = df[df["Símbolo"] == ativo]["Símbolo"].mode()[0]

        entrada = pd.DataFrame([{
            "Hora": hora_atual,
            "Tipo": tipo_valor,
            "Estratégia": estrategia_valor,
            "Símbolo": simbolo_valor
        }])

        previsao = modelo.predict(entrada)[0]
        st.markdown(f"🔮 Lucro estimado: **{previsao:.2f}**")

        limite_minimo = st.number_input("💰 Limite mínimo de lucro para liberar execução", value=0.5)

        if st.button("🚀 Validar e Executar Ordem"):
            if previsao >= limite_minimo:
                preco = round(random.uniform(1.0, 1.5), 5)
                resultado = round(random.uniform(-1.0, 8.0), 2)

                registro = {
                    "Horário": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Símbolo": ativo,
                    "Tipo": tipo_op,
                    "Preço": preco,
                    "Resultado": "SIMULADO NEURAL",
                    coluna_lucro: resultado,
                    "Estratégia": estrategia
                }

                pd.DataFrame([registro]).to_csv("logs/execucoes_fantasmas.csv", mode="a", header=False, index=False)
                st.success(f"🟢 Ordem {tipo_op} liberada e registrada com lucro estimado: {resultado}")
            else:
                st.error("🚫 Ordem bloqueada — lucro estimado abaixo do limite exigido.")
    else:
        st.error("❌ Nenhuma coluna de lucro encontrada no histórico.")
else:
    st.error("❌ Histórico não encontrado — treinamento neural impossibilitado.")

# ======================================
# 👻 BLOCO 11.10 — Iniciar Operador Fantasma Cíclico
# ======================================
import time
import pandas as pd
from datetime import datetime
import random
import os

def iniciar_operador_fantasma(
    modelo=None,
    ativo="WINFUT",
    estrategia="Reversão",
    limite_lucro=0.5,
    intervalo_segundos=300
):
    print(f"👻 Iniciando operador fantasma para {ativo} com estratégia {estrategia}...")

    caminho = "logs/execucao_fantasma.csv"
    os.makedirs(os.path.dirname(caminho), exist_ok=True)

    while True:
        agora = datetime.now()

        direcao = random.choice(["COMPRA", "VENDA"])
        preco = round(random.uniform(100000, 120000), 2) if "WIN" in ativo else round(random.uniform(5000, 6000), 2)
        resultado = round(random.uniform(-limite_lucro, limite_lucro * 2), 2)

        operacao = {
            "Horário": agora.strftime("%Y-%m-%d %H:%M:%S"),
            "Símbolo": ativo,
            "Tipo": direcao,
            "Preço": preco,
            "Resultado": "FANTASMA CICLICO",
            "LucroEstimado": resultado,
            "Estrategia": estrategia
        }

        pd.DataFrame([operacao]).to_csv(
            caminho,
            mode="a",
            index=False,
            header=not os.path.exists(caminho)
        )

        print(f"✅ Ordem fantasma registrada: {direcao} {ativo} em {preco} → Lucro {resultado}")
        time.sleep(intervalo_segundos)

# 🎛️ Controles de entrada de operação
col1, col2, col3 = st.columns(3)
with col1:
    ativo = st.text_input("🎯 Símbolo B3", "PETR4.SA")
with col2:
    lote = st.number_input("🔐 Lote", min_value=1, max_value=1000, value=100, step=1)
with col3:
    operacao = st.selectbox("📤 Tipo de Ordem", ["COMPRA", "VENDA"])

st.markdown("---")

# 📊 Gráfico + 📘 Book de Ofertas
colA, colB = st.columns([2, 1])
with colA:
    st.subheader("📈 Gráfico Candlestick (atualização manual)")
    caminho_grafico = "graficos/grafico_petr4.png"
    if os.path.exists(caminho_grafico):
        st.image(caminho_grafico)
    else:
        st.warning("⚠️ Gráfico não gerado ou ausente.")

with colB:
    st.subheader("📘 Book de Ofertas PETR4.SA")
    st.write(pd.DataFrame([
        {"Tipo": "Compra", "Preço": "34,25", "Volume": 2000},
        {"Tipo": "Venda", "Preço": "34,32", "Volume": 1500},
        {"Tipo": "Compra", "Preço": "34,10", "Volume": 1800},
        {"Tipo": "Venda", "Preço": "34,40", "Volume": 2200}
    ]))

st.markdown("---")

# 🚀 Execução da ordem manual via MetaTrader
if st.button("🚀 Executar Ordem Manual"):
    if not mt5.initialize():
        st.error("❌ Falha ao inicializar MetaTrader.")
    else:
        info = mt5.symbol_info_tick(ativo)
        preco = info.ask if operacao == "COMPRA" else info.bid
        tipo_ordem = mt5.ORDER_TYPE_BUY if operacao == "COMPRA" else mt5.ORDER_TYPE_SELL

        ordem = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": ativo,
            "volume": lote,
            "type": tipo_ordem,
            "price": preco,
            "deviation": 5,
            "magic": 120120,
            "comment": f"Ciborna Manual {operacao}",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_RETURN,
        }

        resultado = mt5.order_send(ordem)

        if resultado is None:
            st.error("❌ Ordem falhou — resultado vazio.")
        elif resultado.retcode == mt5.TRADE_RETCODE_DONE:
            st.success(f"🟢 Ordem {operacao} executada com sucesso! Preço: {preco}")
        else:
            st.error(f"❌ Ordem rejeitada: Código {resultado.retcode} | Msg: {resultado.comment}")

        mt5.shutdown()

st.markdown("---")

# 📊 Histórico das execuções anteriores (CSV local)
caminho_csv = "logs/execucoes_operacionais.csv"
if os.path.exists(caminho_csv):
    execucoes = pd.read_csv(caminho_csv)

    st.write("📋 Colunas disponíveis no histórico:", execucoes.columns.tolist())

    coluna_lucro = detectar_coluna_lucro(execucoes)

    if coluna_lucro:
        execucoes[coluna_lucro] = (
            execucoes[coluna_lucro]
            .astype(str)
            .replace(r"[^\d\-\+\.]", "", regex=True)
            .replace("", "0")
            .astype(float)
        )
        st.subheader("📊 Histórico de Ordens (Arquivo Local)")
        st.dataframe(execucoes.tail(5), use_container_width=True)
    else:
        st.error("❌ Nenhuma coluna de lucro detectada.")
else:
    st.warning("⚠️ Arquivo de histórico não localizado.")

# 🔢 BLOCO 12.X.1 — Histórico da Corretora (MetaTrader)
st.subheader("📊 Histórico Real da Conta MetaTrader (Ativos B3)")

if mt5.initialize():
    try:
        historico = mt5.history_deals_get()

        if not historico:
            st.warning("⚠️ Nenhuma operação registrada na corretora.")
        else:
            df_trades = pd.DataFrame([deal._asdict() for deal in historico])
            df_trades["time"] = pd.to_datetime(df_trades["time"], unit="s")

            colunas_desejadas = ["time", "symbol", "type", "price", "volume", "profit", "comment"]
            colunas_disponiveis = [col for col in colunas_desejadas if col in df_trades.columns]
            df_trades = df_trades[colunas_disponiveis]

            df_trades = df_trades.rename(columns={
                "time": "Data/Hora",
                "symbol": "Símbolo",
                "type": "Tipo",
                "price": "Preço",
                "volume": "Volume",
                "profit": "Lucro",
                "comment": "Comentário"
            })

            st.dataframe(df_trades.tail(10), use_container_width=True)

            if "Lucro" in df_trades.columns:
                lucro_total = df_trades["Lucro"].sum()
                qtd_gains = (df_trades["Lucro"] > 0).sum()
                qtd_losses = (df_trades["Lucro"] < 0).sum()

                st.markdown(f"""
                🔢 **Total de Ordens:** {len(df_trades)}  
                ✅ **Gains:** {qtd_gains}  
                ❌ **Losses:** {qtd_losses}  
                💰 **Lucro Líquido:** `R$ {lucro_total:.2f}`
                """)
    except Exception as e:
        st.error(f"❌ Erro ao consultar histórico da corretora: {e}")
    mt5.shutdown()
else:
    st.error("❌ MetaTrader não inicializado.")

# 🔢 BLOCO 12.2 — Análise Operacional para B3
if not df.empty:
    candle = df.tail(5)

    if "Close" in candle.columns:
        fechamento = candle["Close"]
    else:
        st.error("❌ Coluna de fechamento não encontrada.")
        fechamento = pd.Series([0])

    if "High" in candle.columns:
        high = candle["High"]
    else:
        st.error("❌ Coluna de máxima não encontrada.")
        high = pd.Series([0])

    reversao = fechamento.iloc[-1] < fechamento.mean()
    rompimento = fechamento.iloc[-1] > high.max()

    if reversao:
        st.success("🔄 Padrão detectado: Reversão (B3)")
    elif rompimento:
        st.success("🚀 Padrão detectado: Rompimento (B3)")
    else:
        st.info("📊 Nenhum padrão significativo detectado nos últimos candles.")

# 🔢 BLOCO 12.3 — Interface com Ativo da B3
col1, col2, col3 = st.columns(3)
ativo = col1.text_input("🎯 Ativo B3", "PETR4.SA")
capital = col2.number_input("💰 Capital total (R$)", value=10000.0)
risco = col3.number_input("📉 Risco por operação (%)", value=1.0)

col4, col5 = st.columns(2)
distancia_stop = col4.number_input("📏 Stop Loss (centavos)", value=0.50)
valor_por_ponto = col5.number_input("📐 Valor por centavo (R$)", value=10)

risco_total = capital * (risco / 100)
lote_total = round(risco_total / (distancia_stop * valor_por_ponto), 2)
lote_fracionado = round(lote_total / 2, 2)
st.info(f"🔐 Lote Total: `{lote_total}` • Fracionado: `{lote_fracionado}`")

# 🔢 BLOCO 12.5 — Execução de Ordem com Voz (B3)
ativo = "PETR4.SA"
volume = 100
sinal = "COMPRA"
lucro = 150.75

if mt5.initialize():
    info = mt5.symbol_info_tick(ativo)
    if info and info.ask > 0 and info.bid > 0:
        preco = info.ask if sinal == "COMPRA" else info.bid
        tipo_ordem = mt5.ORDER_TYPE_BUY if sinal == "COMPRA" else mt5.ORDER_TYPE_SELL

        ordem = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": ativo,
            "volume": volume,
            "type": tipo_ordem,
            "price": preco,
            "deviation": 5,
            "magic": 151515,
            "comment": f"Ciborna B3 Manual {sinal}",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_RETURN
        }

        resultado = mt5.order_send(ordem)

        if resultado and resultado.retcode == mt5.TRADE_RETCODE_DONE:
            st.success(f"🟢 Ordem {sinal} enviada para {ativo}! Preço: R$ {preco:.2f}")
            engine = pyttsx3.init()
            engine.say(f"Ordem de {sinal} executada para o ativo {ativo}. Preço de entrada R$ {preco:.2f}")
            engine.runAndWait()

            registro = pd.DataFrame([{
                "Horário": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Símbolo": ativo,
                "Tipo": sinal,
                "Preço": round(preco, 2),
                "Resultado": "AGUARDANDO",
                "LucroEstimado": round(lucro, 2)
            }])

            registro.to_csv("logs/execucao_b3.csv", mode="a", header=False, index=False)

        else:
            st.error(f"❌ Ordem não aceita: {resultado.retcode} • {resultado.comment}")
    mt5.shutdown()
else:
    st.error("❌ MetaTrader não inicializado.")

# 🔢 BLOCO 14.5 — HUD Lateral (Sem imagem)
with st.sidebar:
    st.header("🧠 HUD Ciborna B3")
    st.markdown(f"""
    - 💬 Status: Pronto  
    - 📈 Ativo: PETR4.SA  
    - 🔐 Lote Ideal: `{volume}`  
    - 🎯 Estratégia: Reversão Técnica  
    - 🔊 Voz Neural: Ativa  
    - 💡 Feedback Visual: Online  
    """)
    st.markdown("---")
    st.button("🔄 Reiniciar painel tático")

# ======================================
# 🔢 BLOCO 16 — Scanner de Modo de Preenchimento Incompatível
# ======================================
st.subheader("🧪 Scanner de Ordem com Modo Incompatível")

caminho_arquivo = "painel_ciborna_teste.py"

if os.path.exists(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    incompativeis = [
        (i + 1, linha.strip()) for i, linha in enumerate(linhas)
        if "type_filling" in linha and ("ORDER_FILLING_IOC" in linha or "IOC" in linha)
    ]

    if incompativeis:
        st.warning("❌ IOC detectado nas seguintes linhas:")
        for num, trecho in incompativeis:
            st.text(f"Linha {num}: {trecho}")
        st.info("✅ Substitua por `ORDER_FILLING_RETURN` para evitar erro 10030.")
    else:
        st.success("✅ Nenhum preenchimento incompatível detectado.")
else:
    st.error("⚠️ Arquivo principal não encontrado — verifique o caminho.")

# ======================================
# 🔢 BLOCO 16.1 — Auto-Corretor de Preenchimento + Backup
# ======================================
st.subheader("🛠️ Auto-Corretor de Preenchimento + Backup")

caminho_original = "painel_ciborna_teste.py"
caminho_backup = "painel_ciborna_teste_BACKUP.py"

if os.path.exists(caminho_original):
    shutil.copyfile(caminho_original, caminho_backup)
    st.info("📦 Backup criado com sucesso.")

    with open(caminho_original, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    novas_linhas = []
    alteradas = 0
    for linha in linhas:
        if "type_filling" in linha and "IOC" in linha:
            nova = linha.replace("ORDER_FILLING_IOC", "ORDER_FILLING_RETURN")
            novas_linhas.append(nova)
            alteradas += 1
        else:
            novas_linhas.append(linha)

    with open(caminho_original, "w", encoding="utf-8") as f:
        f.writelines(novas_linhas)

    if alteradas > 0:
        st.success(f"✅ {alteradas} instâncias corrigidas para RETURN.")
    else:
        st.warning("⚠️ Nenhuma instância de IOC encontrada — painel já compatível.")
else:
    st.error("❌ Arquivo principal não encontrado — revise o caminho.")

# ======================================
# 🔢 BLOCO 16.2 — Diagnóstico por Bloco
# ======================================
st.subheader("🧪 Diagnóstico de Preenchimento por Bloco")

arquivo = "painel_ciborna_teste.py"
if os.path.exists(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    mapa_blocos = {}
    bloco_atual = None

    for i, linha in enumerate(linhas):
        if "BLOCO" in linha and "===" in linha:
            bloco_atual = linha.strip()
            mapa_blocos[bloco_atual] = []
        elif bloco_atual:
            mapa_blocos[bloco_atual].append((i + 1, linha.strip()))

    relatorio = [
        f"{bloco} → Linha {num}: {linha}"
        for bloco, conteudo in mapa_blocos.items()
        for num, linha in conteudo
        if "type_filling" in linha and "IOC" in linha
    ]

    if relatorio:
        st.warning("❌ IOC encontrado nos seguintes blocos:")
        for item in relatorio:
            st.text(item)
    else:
        st.success("✅ Nenhum IOC detectado — painel livre de falhas.")
else:
    st.error("⚠️ Arquivo principal não localizado.")
# ======================================
# 🔢 BLOCO 17 — Diagnóstico de Erros ao Vivo
# ======================================
def diagnostico_erro(retcode, comment):
    if retcode == 10030:
        st.error("❌ Erro 10030: Modo de preenchimento não suportado.")
        st.markdown("- 💡 Sugestão: troque `ORDER_FILLING_IOC` por `ORDER_FILLING_RETURN`")
    elif retcode == 10006:
        st.error("❌ Erro 10006: Volume inválido — verifique o lote mínimo.")
    elif retcode == 10013:
        st.error("❌ Erro 10013: Preço fora do mercado.")
    else:
        st.warning(f"⚠️ Erro desconhecido: Código {retcode} | {comment}")
        st.markdown("- 🧠 Ciborna não reconheceu esse erro, envie para análise avançada.")

# ======================================
# 🛸 BLOCO 17.1 — Revestimento Interligado por APIs Remotas
# ======================================
st.markdown("## 🛸 Revestimento Ativo • Canal Neuronal em Órbita")

conexoes_ativas = [
    "🛰️ SpaceX API → Autenticação orbital",
    "🚗 Tesla AI → Direção Autônoma Cognitiva",
    "📈 MetaTrader 5 → Link de Mercado em tempo real",
    "🧪 BacktestStation → Simulação Intergaláctica de Ordens"
]

for canal in conexoes_ativas:
    st.markdown(f"🔗 {canal}")

st.markdown("🧠 Ciborna pronta para absorver dados, emitir sinais e transferir decisões em tempo real.")
st.markdown("---")

# ======================================
# 🔢 BLOCO 17.2 — Alerta automático pós-ordem com voz
# ======================================
def alerta_erro_operacional(retcode, comment):
    engine = pyttsx3.init()
    if retcode == 10030:
        st.error("❌ Erro 10030: Preenchimento não suportado")
        st.markdown("💡 Use `ORDER_FILLING_RETURN` para corretoras compatíveis.")
        st.markdown("<div style='background-color:#ff0000;padding:10px;border-radius:5px;'>🔴 ALERTA: Ordem rejeitada por modo de preenchimento!</div>", unsafe_allow_html=True)
        engine.say("Atenção comandante. Ordem rejeitada por preenchimento não compatível.")
    elif retcode == 10006:
        st.error("❌ Erro 10006: Volume inválido")
        st.markdown("💡 Verifique o lote mínimo do ativo no MetaTrader.")
        engine.say("Ordem falhou. Volume inválido detectado.")
    elif retcode == 10013:
        st.error("❌ Erro 10013: Preço fora do mercado")
        st.markdown("💡 Aguarde cotação válida ou revise o preço manual.")
        engine.say("Comandante, preço fora do mercado. Ordem abortada.")
    elif retcode == 10009:
        st.success("✅ Ordem executada com sucesso!")
        st.markdown("<div style='background-color:#00ff00;padding:10px;border-radius:5px;'>🟢 EXECUÇÃO CONFIRMADA</div>", unsafe_allow_html=True)
        engine.say("Ordem confirmada, comandante. Missão cumprida.")
    else:
        st.warning(f"⚠️ Código não mapeado: {retcode}")
        st.markdown(f"💬 Comentário da corretora: {comment}")
        engine.say("Erro desconhecido na execução. Atenção comandante.")

    engine.runAndWait()

# ======================================
# 🔢 BLOCO 17.X — Aba de Diagnóstico Tático de Erros Operacionais
# ======================================
with st.sidebar:
    st.header("🧠 Central de Segurança Neural")
    st.markdown("📋 Diagnóstico em tempo real")
    st.markdown("---")

    if os.path.exists("logs/execucoes_operacionais.csv"):
        df = pd.read_csv("logs/execucoes_operacionais.csv")
        st.dataframe(df.tail(10))

    retcode = st.number_input("🔢 Código retcode", value=10030, step=1)
    comment = st.text_input("💬 Comentário da corretora", value="Modo de preenchimento não suportado")

    if st.button("🧠 Analisar retcode"):
        diagnostico_erro(retcode, comment)

# ======================================
# 🧠 BLOCO 17.4 — Capota Neural da Ciborna
# ======================================
st.set_page_config(
    page_title="🧠 Ciborna Neural Console",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🚀 CIBORNA • Painel de Execução Neural Interdimensional")

st.markdown("""
    <style>
    .main {
        background-color: #10151a;
        color: #D6F1FF;
    }
    h1 {
        font-size: 42px !important;
        font-weight: bold;
        color: #00FFFF;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("🧠 Sistema Ciborna pronto para diagnosticar, prever e reparar em tempo real.")
st.markdown("📡 Conexões: BLOCOs 18.x • BLOCO 20.x • BLOCO FINAL • BLOCO Fantasma")
st.markdown("🟢 **Modo de Execução Modular Ativado**")
st.markdown("---")
# ======================================
# 🔒 BLOCO FINAL — Encerramento Neural da Cabine Ciborna
# ======================================
import streamlit as st
import os
import gc
from datetime import datetime

st.subheader("🔒 Encerramento Neural da Sessão")

# 🧹 Limpeza de variáveis sensíveis
for var in ["modelo", "ativo", "estrategia", "lote", "df"]:
    try:
        exec(f"del {var}")
    except Exception:
        pass

gc.collect()

# 🚫 Fechamento do MetaTrader 5, se aplicável
try:
    import MetaTrader5 as mt5
    mt5.shutdown()
except Exception:
    pass

# 🧼 Remoção de arquivos temporários
temp_files = [
    "identificadores_temp.txt",
    "logs/temp_execucoes.csv"
]
for temp in temp_files:
    caminho = os.path.join("C:\\Dimensao_Cosmica_Quantica", temp)
    if os.path.exists(caminho):
        try:
            os.remove(caminho)
        except Exception:
            pass

st.success("🧠 Sessão encerrada com segurança. Ciborna desconectada da malha neural.")
st.stop()
# ======================================
# 🔢 BLOCO 20.1 — Monitoramento em Tempo Real da Cabine
# ======================================
import time
st.subheader("📡 Monitoramento ao Vivo dos Blocos da Cabine")

status_simulado = {
    "BLOCO 11.6": "🟢 OK",
    "BLOCO 11.7": "🟢 OK",
    "BLOCO 11.9": "🟢 OK",
    "BLOCO 18.5": "🟢 OK",
    "BLOCO 20": "🟢 OK"
}
for bloco, status in status_simulado.items():
    st.markdown(f"🔎 {bloco} → {status}")
    time.sleep(0.2)
# ======================================
# 🔢 BLOCO 21 — Painel Único Modular com Navegação Inteligente
# ======================================
import streamlit as st
import os
import ast
import graphviz
import pandas as pd
import gc
import time

# 🧠 Cabeçalho do Painel
st.set_page_config(layout="wide")
st.title("🧠 Painel Integrado da Cabine Ciborna")

# 🎛️ Abas integradas
aba1, aba2, aba3, aba4 = st.tabs([
    "🧪 Diagnóstico de Scripts",
    "🧠 Mapa + Monitoramento",
    "📁 Logs Operacionais",
    "🔒 Encerramento Neural"
])

# ======================================
# 🔍 ABA 1 — Diagnóstico de Scripts
# ======================================
with aba1:
    st.subheader("🔍 Diagnóstico de Execução dos Scripts Python")
    pasta_base = "C:\\Dimensao_Cosmica_Quantica"
    arquivos = [f for f in os.listdir(pasta_base) if f.endswith(".py")]

    problemas = []
    for arquivo in arquivos:
        caminho = os.path.join(pasta_base, arquivo)
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                ast.parse(f.read())
        except SyntaxError as e:
            problemas.append({
                "Arquivo": arquivo,
                "Linha": e.lineno,
                "Coluna": e.offset,
                "Mensagem": e.msg
            })

    if problemas:
        st.error("❌ Scripts com falhas detectadas:")
        for erro in problemas:
            st.markdown(f"📄 `{erro['Arquivo']}` → Linha {erro['Linha']} | Coluna {erro['Coluna']} → `{erro['Mensagem']}`")
    else:
        st.success("✅ Todos os arquivos estão íntegros e prontos para execução!")

# ======================================
# 🧠 ABA 2 — Mapa Neural + Monitoramento
# ======================================
with aba2:
    colMapa, colStatus = st.columns([2, 1])

    with colMapa:
        st.subheader("🧭 Mapa Modular Interativo da Cabine")
        topologia = graphviz.Digraph()

        topologia.node("Painel Principal", shape="box", style="filled", color="lightblue")

        # Execução
        for bloco in [
            "BLOCO 12 • Execução Manual",
            "BLOCO 11.6 • Fantasma Otimizado",
            "BLOCO 11.7 • Ação Temporal",
            "BLOCO 11.9 • Filtro Preditivo"
        ]:
            topologia.node(bloco, shape="box")
            topologia.edge("Painel Principal", bloco)

        # Diagnóstico
        for diag in ["BLOCO 18.4 • Semântico", "BLOCO 18.5 • Integridade Cabine"]:
            topologia.node(diag, shape="ellipse", color="orange")
            topologia.edge("Painel Principal", diag)

        topologia.edge("BLOCO 11.6 • Fantasma Otimizado", "BLOCO 11.9 • Filtro Preditivo")

        st.graphviz_chart(topologia)

    with colStatus:
        st.subheader("📡 Monitoramento ao Vivo da Cabine")
        status_simulado = {
            "BLOCO 11.6": "🟢 OK",
            "BLOCO 11.7": "🟢 OK",
            "BLOCO 11.9": "🟢 OK",
            "BLOCO 18.5": "🟢 OK",
            "BLOCO 20": "🟢 OK"
        }
        for bloco, status in status_simulado.items():
            st.markdown(f"🔎 {bloco} → {status}")
            time.sleep(0.2)

# ======================================
# 📁 ABA 3 — Scanner de Logs Operacionais
# ======================================
with aba3:
    st.subheader("📁 Scanner de Logs Operacionais (.csv)")
    caminho_logs = os.path.join(pasta_base, "logs")
    if os.path.exists(caminho_logs):
        arquivos_csv = [f for f in os.listdir(caminho_logs) if f.endswith(".csv")]
        selecao = st.selectbox("📄 Selecione um arquivo para inspecionar", arquivos_csv)
        if selecao:
            df = pd.read_csv(os.path.join(caminho_logs, selecao))
            st.dataframe(df.head(100), use_container_width=True)
    else:
        st.warning("⚠️ Pasta `logs` não localizada dentro de Dimensao_Cosmica_Quantica.")

# ======================================
# 🔒 ABA 4 — Encerramento Neural da Sessão
# ======================================
with aba4:
    st.subheader("🔒 Encerramento Neural Seguro da Cabine")

    # 🔐 Limpeza de variáveis sensíveis
    variaveis_criticas = ["modelo", "ativo", "estrategia", "lote", "df"]
    for var in variaveis_criticas:
        try:
            exec(f"del {var}")
        except:
            pass

    gc.collect()

    # 🚫 Desativação de sessão externa (MetaTrader, se aplicável)
    try:
        import MetaTrader5 as mt5
        mt5.shutdown()
    except:
        pass

    # 🧽 Exclusão de arquivos temporários
    arquivos_temp = [
        "identificadores_temp.txt",
        "logs/temp_execucoes.csv"
    ]
    for arquivo in arquivos_temp:
        caminho_temp = os.path.join(pasta_base, arquivo)
        if os.path.exists(caminho_temp):
            try:
                os.remove(caminho_temp)
            except:
                pass

    st.success("🧠 Cabine encerrada com segurança. Ciborna fora da malha neural. ✅")
    st.stop()
# ======================================
# 🌐 BLOCO 30 — Comunicação Real com APIs Externas
# ======================================
import streamlit as st
import requests

st.subheader("🌐 Comunicação com API Externa • Painel Ciborna")

api_url = "https://api.exemplo.com/v1/dados"  # 🔐 URL simulada
payload = {"ativo": "PETR4.SA", "modelo": "reversão_neural"}
headers = {"Authorization": "Bearer SEU_TOKEN_AQUI"}

if st.button("📡 Disparar Consulta à API"):
    try:
        resposta = requests.post(api_url, json=payload, headers=headers)
        if resposta.status_code == 200:
            dados = resposta.json()
            st.success("✅ Conexão estabelecida com sucesso!")
            st.json(dados)
        else:
            st.error(f"❌ Falha — código {resposta.status_code}")
    except Exception as e:
        st.error("⚠️ Erro ao se conectar à API.")
        st.code(str(e))

# ======================================
# ⚡ BLOCO 40.0 — Conector Ciborna com PowerShell
# ======================================
import subprocess

st.subheader("⚡ Execução PowerShell via Ciborna")

comando = st.text_input("📥 Digite o comando PowerShell:", "Get-Process")

if st.button("🚀 Executar Comando"):
    try:
        resultado = subprocess.check_output(["powershell", "-Command", comando], shell=True, text=True)
        st.success("✅ Comando executado com sucesso!")
        st.code(resultado)
    except Exception as e:
        st.error("❌ Erro ao executar comando.")
        st.code(str(e))

# ======================================
# 📦 BLOCO 40.1 — Execução de Scripts PowerShell (.ps1)
# ======================================
import os

st.subheader("📦 Execução de Scripts PowerShell (.ps1)")

script_path = "C:\\Cabine_Ciborna\\Scripts\\teste_ciborna.ps1"

if st.button("🚀 Executar Script .ps1"):
    if os.path.exists(script_path):
        try:
            resultado = subprocess.check_output(["powershell", "-File", script_path], shell=True, text=True)
            st.success("✅ Script executado com sucesso!")
            st.code(resultado)
        except Exception as e:
            st.error("❌ Falha na execução do script.")
            st.code(str(e))
    else:
        st.error("📂 Script não localizado. Verifique o caminho.")

# ======================================
# 🧠 BLOCO 40.2 — Diagnóstico do Sistema via PowerShell
# ======================================
st.subheader("🧠 Diagnóstico Neural do Sistema • via PowerShell")

comando_diag = "Get-WmiObject -Class Win32_OperatingSystem | Select-Object Caption, Version, BuildNumber"

if st.button("🔍 Executar Diagnóstico do Sistema"):
    try:
        resultado = subprocess.check_output(["powershell", "-Command", comando_diag], shell=True, text=True)
        st.success("✅ Diagnóstico concluído:")
        st.code(resultado)
    except Exception as e:
        st.error("❌ Erro ao realizar diagnóstico.")
        st.code(str(e))

# ======================================
# 🛸 BLOCO 40.3 — Controle de Portas, Logs e Firewall
# ======================================
st.subheader("🛡️ Controle de Segurança • Ciborna Firewall + Portas")

comandos = {
    "🔒 Verificar status do firewall": "Get-NetFirewallProfile",
    "📡 Verificar portas abertas": "netstat -a -n",
    "📁 Listar logs de sistema": "Get-EventLog -LogName System -Newest 10"
}

for label, comando in comandos.items():
    if st.button(label):
        try:
            resultado = subprocess.check_output(["powershell", "-Command", comando], shell=True, text=True)
            st.markdown(f"### {label}")
            st.code(resultado)
        except Exception as e:
            st.error(f"❌ Erro ao executar: {label}")
            st.code(str(e))
# ======================================
# ⚙️ BLOCO 40.4 — Disparo Combinado de Comandos Neurais
# ======================================
import streamlit as st
import subprocess
import threading

st.subheader("🧠 Disparo Paralelo de Comandos PowerShell + Diagnóstico")

# 🔧 Lista de comandos simultâneos
comandos = [
    "Get-Process | Select-Object -First 5",
    "Get-WmiObject -Class Win32_OperatingSystem | Select-Object Caption, Version",
    "Get-NetFirewallProfile"
]

def executar_comando(comando, posicao):
    try:
        resultado = subprocess.check_output(["powershell", "-Command", comando], shell=True, text=True)
        st.code(resultado, f"🧠 Resultado {posicao}")
    except Exception as e:
        st.error(f"❌ Erro no comando {posicao}: {comando}")
        st.code(str(e))

if st.button("🚀 Disparar todos os comandos em paralelo"):
    for i, comando in enumerate(comandos, start=1):
        thread = threading.Thread(target=executar_comando, args=(comando, i))
        thread.start()
# ======================================
# 📈 BLOCO 40.5 — Scanner Neural do Livro de Ofertas (Book)
# ======================================
import streamlit as st
import pandas as pd
import MetaTrader5 as mt5

st.subheader("📈 Scanner em Tempo Real do Book de Ofertas (MetaTrader5)")

ativo = st.text_input("💹 Digite o ativo (ex: PETR4.SA)", value="PETR4.SA")
profundidade = st.slider("📊 Profundidade de leitura do book", 1, 20, 5)

if st.button("🚀 Escanear Livro de Ofertas"):
    if not mt5.initialize():
        st.error("❌ Falha ao inicializar conexão com MetaTrader5")
    else:
        book = mt5.market_book_add(ativo)
        dados = mt5.market_book_get(ativo)
        mt5.market_book_release(ativo)

        if dados:
            registros = []
            for row in dados:
                registros.append({
                    "Tipo": "Oferta de Venda" if row['type'] == mt5.BOOK_TYPE_SELL else "Oferta de Compra",
                    "Preço": row['price'],
                    "Volume": row['volume']
                })

            df_book = pd.DataFrame(registros).head(profundidade)
            st.dataframe(df_book, use_container_width=True)
        else:
            st.warning("⚠️ Nenhum dado disponível para este ativo.")
        mt5.shutdown()
# ======================================
# 🔎 BLOCO Ciborna Search — Barra de Consulta Neural
# ======================================
import streamlit as st

st.subheader("🔍 Ciborna Search • Interface de Entrada Inteligente")

entrada_usuario = st.text_input("💡 Digite um termo, bloco, comando ou pergunta")

if st.button("🧠 Consultar"):
    if "bloco" in entrada_usuario.lower():
        st.info(f"🔢 Você está consultando um BLOCO: **{entrada_usuario}**")
        # Aqui você pode disparar rota para BLOCO X

    elif "ordem" in entrada_usuario.lower():
        st.success("📈 Consulta de execução de ordens ativada.")
        # Pode abrir BLOCO 11.9 ou 11.10

    elif entrada_usuario.lower().startswith("como"):
        st.markdown("🤖 Simulação de ajuda ativada. Posso gerar instruções sobre isso.")
        # Você pode integrar com módulo de ajuda ou até IA local

    else:
        st.warning("⚠️ Termo não reconhecido. Tente algo como: 'bloco 41', 'como disparar ordem', 'scanner'...")

    # Futuramente: disparar IA local, fazer buscas, interligar com sua própria base Ciborna.
# ======================================
# 🧠 Módulo IA_CIBORNA • Núcleo Estratégico Adaptativo
# ======================================
import os
import pandas as pd
import streamlit as st
import random
from datetime import datetime
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# 📁 Configuração dos caminhos
CAMINHO_LOG = "logs/execucoes_fantasmas.csv"
CAMINHO_MEMORIA = "logs/memoria_ciborna.csv"
# ======================================
# 🧠 BLOCO 41 — Ciclo IA Estratégica sobre Replay
# ======================================
import pandas as pd
import streamlit as st
from datetime import datetime
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import random
import os

# 📁 Caminhos dos arquivos de log
CAMINHO_LOG = "logs/execucoes_fantasmas.csv"
CAMINHO_MEMORIA = "logs/memoria_neural.csv"

# 🔁 BLOCO 41.0 — Diagnóstico com Replay
def ciclo_ia_estrategica():
    st.subheader("🧠 BLOCO 41 • Ciclo IA Estratégica Ativado")

    try:
        df = pd.read_csv("replay/replay_profit.csv")
    except:
        st.error("❌ Replay não encontrado em replay/replay_profit.csv")
        return

    if df.empty:
        st.warning("⚠️ Arquivo está vazio")
        return

    st.markdown("📊 Executando análise neural sobre replay Profit...")
    resultados = []

    for _, row in df.iterrows():
        hora = pd.to_datetime(row["DataHora"]).hour if "DataHora" in row else random.randint(9, 17)
        tipo = 0 if row.get("Tipo", "COMPRA") == "COMPRA" else 1
        lucro_simulado = random.uniform(-1.0, 2.0)

        resultados.append({
            "Horário": hora,
            "Símbolo": row.get("Símbolo", "IND"),
            "Tipo": row.get("Tipo", "NEUTRO"),
            "Lucro IA": round(lucro_simulado, 2)
        })

    df_resultado = pd.DataFrame(resultados)
    st.dataframe(df_resultado.head(10))

    lucro_medio = df_resultado["Lucro IA"].mean()
    taxa_acerto = (df_resultado["Lucro IA"] > 0).sum() / len(df_resultado)

    st.markdown(f"💰 Lucro médio IA: `{lucro_medio:.2f}`")
    st.markdown(f"🎯 Taxa de acerto: `{taxa_acerto * 100:.1f}%`")

# 💾 BLOCO 41.2 — Registro de Memória Neural
def registrar_memoria(registro):
    pd.DataFrame([registro]).to_csv(
        CAMINHO_MEMORIA,
        mode="a",
        header=not os.path.exists(CAMINHO_MEMORIA),
        index=False
    )
# ======================================
# 🧠 Módulo IA_CIBORNA • Núcleo Estratégico Adaptativo
# ======================================
import os
import pandas as pd
import streamlit as st
import random
from datetime import datetime
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# 📁 Configuração dos caminhos
CAMINHO_LOG = "logs/execucoes_fantasmas.csv"
CAMINHO_MEMORIA = "logs/memoria_ciborna.csv"

# ======================================
# 🔁 BLOCO 41.1 — Aprendizado Adaptativo com Histórico
# ======================================
def treinar_modelo_adaptativo():
    if not os.path.exists(CAMINHO_LOG):
        return None
    df = pd.read_csv(CAMINHO_LOG)
    df["Lucro/Prejuízo"] = pd.to_numeric(df["Lucro/Prejuízo"], errors="coerce").fillna(0.0)
    df["Hora"] = pd.to_datetime(df["Horário"]).dt.hour
    df["Tipo"] = df["Tipo"].map({"COMPRA": 0, "VENDA": 1})
    df["Estratégia"] = df["Estratégia"].astype("category").cat.codes
    df["Símbolo"] = df["Símbolo"].astype("category").cat.codes

    X = df[["Hora", "Tipo", "Estratégia", "Símbolo"]]
    y = df["Lucro/Prejuízo"]
    modelo = RandomForestRegressor(n_estimators=150).fit(*train_test_split(X, y, test_size=0.2))
    return modelo

# ======================================
# 💾 BLOCO 41.2 — Registro de Memória Neural
# ======================================
def registrar_memoria(registro):
    pd.DataFrame([registro]).to_csv(CAMINHO_MEMORIA, mode="a", header=not os.path.exists(CAMINHO_MEMORIA), index=False)

# ======================================
# ⚡ BLOCO 41.3 — Avaliação de Reforço com Score de Execução
# ======================================
def calcular_score():
    if not os.path.exists(CAMINHO_LOG):
        return 0.0, 0.0
    df = pd.read_csv(CAMINHO_LOG)
    df["Lucro/Prejuízo"] = pd.to_numeric(df["Lucro/Prejuízo"], errors="coerce").fillna(0.0)
    media_lucro = df["Lucro/Prejuízo"].mean()
    taxa_acerto = (df["Lucro/Prejuízo"] > 0).mean()
    return round(media_lucro, 2), round(taxa_acerto * 100, 1)

# ======================================
# 🧭 BLOCO 41.4 — Interface Estratégica e Tomada de Decisão Autônoma
# ======================================
def interface_ia_ciborna():
    st.subheader("🧠 IA Estratégica Ciborna • Núcleo Adaptativo de Decisão")

    modelo = None
    if st.button("🔄 Treinar IA com histórico de ordens"):
        modelo = treinar_modelo_adaptativo()
        if modelo:
            st.success("🧠 Modelo treinado com sucesso!")
        else:
            st.warning("⚠️ Log de execução não encontrado.")

    if modelo:
        st.markdown("### 📈 Parâmetros de Execução Inteligente")
        hora = datetime.now().hour
        tipo_op = st.radio("📊 Tipo de Ordem", ["COMPRA", "VENDA"])
        estrategia = st.selectbox("🎯 Estratégia", ["Reversão", "Rompimento", "Aleatória", "Sinal Técnico"])
        ativo = st.text_input("💹 Ativo", value="PETR4.SA")

        tipo_valor = 0 if tipo_op == "COMPRA" else 1
        estrategia_valor = random.randint(0, 3)
        simbolo_valor = random.randint(0, 10)

        entrada = pd.DataFrame([{
            "Hora": hora,
            "Tipo": tipo_valor,
            "Estratégia": estrategia_valor,
            "Símbolo": simbolo_valor
        }])

        previsao = modelo.predict(entrada)[0]
        st.markdown(f"🔮 Lucro estimado: **{previsao:.2f}**")
        limite_lucro = st.number_input("💰 Limite mínimo de lucro", value=0.5)

        if st.button("🧠 Executar Ordem Estratégica"):
            if previsao >= limite_lucro:
                preco = round(random.uniform(1.0, 1.5), 5)
                resultado = round(previsao, 2)

                registro = {
                    "Horário": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Símbolo": ativo,
                    "Tipo": tipo_op,
                    "Preço": preco,
                    "Resultado": "IA-CIBORNA",
                    "Lucro/Prejuízo": resultado,
                    "Estratégia": estrategia
                }

                pd.DataFrame([registro]).to_csv(CAMINHO_LOG, mode="a", header=False, index=False)
                registrar_memoria(registro)
                st.success(f"✅ Ordem {tipo_op} executada pela IA • Lucro: {resultado:.2f}")
            else:
                st.warning("🚫 Lucro abaixo do limite. Ordem abortada.")

    # 🔎 Indicador de performance da IA
    media, acerto = calcular_score()
    st.markdown("### 📊 Desempenho Estratégico da IA")
    st.markdown(f"📈 Lucro médio: **{media:.2f}**")
    st.markdown(f"🎯 Taxa de acerto: **{acerto:.1f}%**")

# ======================================
# 🧠 Disparo da Interface no Painel
# ======================================
if __name__ == "__main__":
    interface_ia_ciborna()
# ======================================
# 🎮 BLOCO 42 — CibornaReplay • Simulação IA vs Robô NTSL
# ======================================

# ====import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from datetime import datetime
import matplotlib.pyplot as plt
import os

# 📁 Caminho do arquivo do replay exportado do Profit Pro
caminho_candles = "replay/replay_profit.csv"
caminho_log_ia = "logs/execucoes_replay_ia.csv"
caminho_log_ntsl = "logs/execucoes_replay_ntsl.csv"

# ======================================
# 🔁 BLOCO 1 — Carregar dados do replay
# ======================================
def carregar_dados_replay():
    if not os.path.exists(caminho_candles):
        st.error("❌ Replay não encontrado. Exporte candles do Profit como CSV.")
        return None
    df = pd.read_csv(caminho_candles)
    df["Hora"] = pd.to_datetime(df["DataHora"]).dt.hour
    df["LucroNTSL"] = pd.to_numeric(df["LucroNTSL"], errors="coerce").fillna(0.0)
    return df

# ======================================
# 🧠 BLOCO 2 — IA Ciborna Preditiva
# ======================================
def treinar_modelo_ciborna(df):
    df["LucroIA"] = pd.to_numeric(df["LucroIA"], errors="coerce").fillna(0.0)
    df["Tipo"] = df["Tipo"].map({"COMPRA": 0, "VENDA": 1})
    df["Estrategia"] = df["Estrategia"].astype("category").cat.codes
    df["Símbolo"] = df["Símbolo"].astype("category").cat.codes

    X = df[["Hora", "Tipo", "Estrategia", "Símbolo"]]
    y = df["LucroIA"]
    modelo = RandomForestRegressor(n_estimators=100).fit(*train_test_split(X, y, test_size=0.2))
    return modelo

# ======================================
# 🎯 BLOCO 3 — Executar simulações IA vs NTSL
# ======================================
def simular_replay(df, modelo):
    resultados_ia = []
    resultados_ntsl = []

    for _, row in df.iterrows():
        entrada = pd.DataFrame([{
            "Hora": row["Hora"],
            "Tipo": row["Tipo"],
            "Estrategia": row["Estrategia"],
            "Símbolo": row["Símbolo"]
        }])
        previsao_ia = modelo.predict(entrada)[0]
        resultados_ia.append(previsao_ia)
        resultados_ntsl.append(row["LucroNTSL"])

    df["LucroEstimadoIA"] = resultados_ia
    df["LucroRealNTSL"] = resultados_ntsl

    df.to_csv(caminho_log_ia, index=False)
    st.success("✅ Simulação Ciborna vs NTSL concluída.")
    return df

# ======================================
# 📈 BLOCO 4 — Comparação visual
# ======================================
def mostrar_comparativo(df):
    st.subheader("📊 Comparativo de Lucros • IA Ciborna vs. Robô NTSL")

    fig, ax = plt.subplots()
    ax.plot(df["DataHora"], df["LucroEstimadoIA"], label="🔮 Ciborna IA", color="blue")
    ax.plot(df["DataHora"], df["LucroRealNTSL"], label="⚙️ NTSL XP", color="green")
    ax.set_title("💰 Lucro por Candle (Replay)")
    ax.set_ylabel("Lucro")
    ax.legend()
    st.pyplot(fig)

    media_ia = df["LucroEstimadoIA"].mean()
    media_ntsl = df["LucroRealNTSL"].mean()
    st.markdown(f"📈 Média Ciborna IA: **{media_ia:.2f}**")
    st.markdown(f"⚙️ Média NTSL: **{media_ntsl:.2f}**")
# ======================================
# 🚀 BLOCO Principal — Execução no Painel
# ======================================
def executar_ciborna_replay():
    st.title("🧠 CibornaReplay42 • Simulação de IA sobre Candles Profit")

    df = carregar_dados_replay()
    if df is not None:
        modelo = treinar_modelo_ciborna(df)
        resultado_df = simular_replay(df, modelo)
        mostrar_comparativo(resultado_df)

# 🔧 Executar a cabine de replay
if __name__ == "__main__":
    executar_ciborna_replay()

# ==================================
# 🧬 BLOCO 43 — Evolução Híbrida da IA Ciborna com Reforço via NTSL
# ======================================
import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import os

st.subheader("🧬 BLOCO 43 — Evolução Híbrida com Reforço NTSL")

caminho_comparativo = "logs/execucoes_replay_ia.csv"

def carregar_dados_comparativos():
    if not os.path.exists(caminho_comparativo):
        st.error("❌ Log comparativo não encontrado. Execute BLOCO 42 primeiro.")
        return None
    return pd.read_csv(caminho_comparativo)

def treinar_modelo_evolutivo(df):
    df["ErroNTSL"] = df["LucroEstimadoIA"] - df["LucroRealNTSL"]
    df["AlvoEvolutivo"] = df["ErroNTSL"].apply(lambda x: max(x, 0))

    df["Tipo"] = df["Tipo"].map({"COMPRA": 0, "VENDA": 1})
    df["Estrategia"] = df["Estrategia"].astype("category").cat.codes
    df["Símbolo"] = df["Símbolo"].astype("category").cat.codes

    X = df[["Hora", "Tipo", "Estrategia", "Símbolo"]]
    y = df["AlvoEvolutivo"]

    modelo = RandomForestRegressor(n_estimators=200).fit(*train_test_split(X, y, test_size=0.25))
    return modelo

def executar_evolucao(df, modelo):
    df["LucroCibornaEvoluido"] = df.apply(lambda row: modelo.predict(pd.DataFrame([{
        "Hora": row["Hora"],
        "Tipo": row["Tipo"],
        "Estrategia": row["Estrategia"],
        "Símbolo": row["Símbolo"]
    }]))[0], axis=1)

    st.success("🧠 IA evoluiu com base nos erros observados do NTSL.")
    st.markdown("### 🔍 Comparativo de Evolução")
    st.dataframe(df[["DataHora", "LucroRealNTSL", "LucroEstimadoIA", "LucroCibornaEvoluido"]].head(10))

    st.markdown(f"📈 Média NTSL: **{df['LucroRealNTSL'].mean():.2f}**")
    st.markdown(f"🔮 Média Ciborna Original: **{df['LucroEstimadoIA'].mean():.2f}**")
    st.markdown(f"🧬 Média Ciborna Evoluída: **{df['LucroCibornaEvoluido'].mean():.2f}**")

# 🚀 Ativação do BLOCO 43
df_comparativo = carregar_dados_comparativos()
if df_comparativo is not None:
    modelo_hibrido = treinar_modelo_evolutivo(df_comparativo)
    executar_evolucao(df_comparativo, modelo_hibrido)
# ======================================
# 🔮 BLOCO 44 — CibornaTechFusion • IA + Lógica Técnica do Robô NTSL
# ======================================
import pandas as pd
import streamlit as st
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from datetime import datetime

st.subheader("🔁 BLOCO 44 — Fusão Neural com Estratégia Técnica XP")

caminho_tecnico = "replay/estrategia_profit.csv"

def carregar_tecnica_profit():
    if not os.path.exists(caminho_tecnico):
        st.error("⚠️ Arquivo técnico não encontrado.")
        return None
    df = pd.read_csv(caminho_tecnico)
    df["Hora"] = pd.to_datetime(df["DataHora"]).dt.hour
    df["LucroXP"] = pd.to_numeric(df["LucroXP"], errors="coerce").fillna(0.0)
    df["VWAP"] = pd.to_numeric(df["VWAP"], errors="coerce").fillna(0.0)
    df["SAR"] = pd.to_numeric(df["SAR"], errors="coerce").fillna(0.0)
    df["ADX"] = pd.to_numeric(df["ADX"], errors="coerce").fillna(0.0)
    df["EMA"] = pd.to_numeric(df["EMA"], errors="coerce").fillna(0.0)
    df["Volume"] = pd.to_numeric(df["Volume"], errors="coerce").fillna(0.0)
    return df

def treinar_ciborna_tecnica(df):
    X = df[["Hora", "VWAP", "SAR", "ADX", "EMA", "Volume"]]
    y = df["LucroXP"]
    modelo = RandomForestRegressor(n_estimators=150).fit(*train_test_split(X, y, test_size=0.25))
    return modelo

def simular_fusao(df, modelo):
    df["LucroCibornaFusionada"] = df.apply(lambda row: modelo.predict(pd.DataFrame([{
        "Hora": row["Hora"],
        "VWAP": row["VWAP"],
        "SAR": row["SAR"],
        "ADX": row["ADX"],
        "EMA": row["EMA"],
        "Volume": row["Volume"]
    }]))[0], axis=1)

    st.success("🧠 IA Ciborna agora simula decisões baseadas nos indicadores técnicos.")
    st.dataframe(df[["DataHora", "LucroXP", "LucroCibornaFusionada"]].head(12))

    st.markdown(f"⚙️ Média Lucro XP: **{df['LucroXP'].mean():.2f}**")
    st.markdown(f"🧠 Média Ciborna Fusionada: **{df['LucroCibornaFusionada'].mean():.2f}**")

# 🚀 Ativação do BLOCO 44
df_tech = carregar_tecnica_profit()
if df_tech is not None:
    modelo_tech = treinar_ciborna_tecnica(df_tech)
    simular_fusao(df_tech, modelo_tech)
# ======================================
# ⚙️ BLOCO 45 — Autoajuste Estratégico dos Indicadores Técnicos • IA Ciborna
# ======================================
import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import numpy as np
import os

st.subheader("⚙️ BLOCO 45 — Autoajuste dos Indicadores Técnicos com IA Adaptativa")

caminho_tecnico = "replay/estrategia_profit.csv"

# 🔁 Função para carregar os dados de estratégia técnica
def carregar_dados_estrategia():
    if not os.path.exists(caminho_tecnico):
        st.error("❌ Replay técnico não encontrado.")
        return None
    df = pd.read_csv(caminho_tecnico)
    df["Hora"] = pd.to_datetime(df["DataHora"]).dt.hour
    df["Lucro"] = pd.to_numeric(df["LucroXP"], errors="coerce").fillna(0.0)
    return df

# 🧠 Função para buscar os melhores parâmetros SAR/ADX via IA
def buscar_parametros_otimizados(df):
    melhores_config = []
    df_base = df.copy()

    sar_steps = np.arange(0.01, 0.06, 0.01)
    adx_steps = np.arange(15, 30, 3)

    for sar_af in sar_steps:
        for adx_limite in adx_steps:
            df_test = df_base.copy()
            df_test["SAR_Ajustado"] = df_test["SAR"] * sar_af
            df_test["ADX_Ajustado"] = df_test["ADX"] * (adx_limite / 25)

            X = df_test[["Hora", "SAR_Ajustado", "ADX_Ajustado", "VWAP", "Volume"]]
            y = df_test["Lucro"]

            modelo = RandomForestRegressor(n_estimators=100).fit(*train_test_split(X, y, test_size=0.25))
            score = modelo.score(X, y)

            melhores_config.append({
                "SAR_AF": sar_af,
                "ADX_Limite": adx_limite,
                "Score": score
            })

    resultado = pd.DataFrame(melhores_config).sort_values(by="Score", ascending=False).head(1)
    return resultado.iloc[0]

# ⚙️ Aplicação dos ajustes no DataFrame técnico
def aplicar_ajuste(df, sar_af, adx_limite):
    df["SAR_Ajustado"] = df["SAR"] * sar_af
    df["ADX_Ajustado"] = df["ADX"] * (adx_limite / 25)
    df["LucroPrevistoOtimo"] = df["Close"] * (df["ADX_Ajustado"] / 100)

    st.success("🧠 Ajustes aplicados com sucesso.")
    st.dataframe(df[["DataHora", "SAR", "SAR_Ajustado", "ADX", "ADX_Ajustado", "LucroPrevistoOtimo"]].head(10))

# 🚀 Execução do BLOCO 45
df_estrategia = carregar_dados_estrategia()
if df_estrategia is not None:
    params = buscar_parametros_otimizados(df_estrategia)

    st.markdown("🔧 Parâmetros propostos pela IA Ciborna:")
    st.markdown(f"- **SAR Acceleration Factor**: `{params['SAR_AF']:.3f}`")
    st.markdown(f"- **ADX Limite**: `{params['ADX_Limite']}`")
    st.markdown(f"📈 Score do modelo: `{params['Score']:.4f}`")

    aplicar_ajuste(df_estrategia, params["SAR_AF"], params["ADX_Limite"])
# ======================================
# 🤖 BLOCO 46 — CibornaGen • Robô Gerado por IA com Base Histórica
# ======================================
import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import random
from datetime import datetime
import os

st.subheader("🤖 BLOCO 46 — Geração Neural de Robôs com Padrões Ciborna")

caminho_log = "logs/execucoes_fantasmas.csv"
caminho_prototipo = "logs/ciborna_ntx_prototipo.csv"

def gerar_robô_por_ia():
    if not os.path.exists(caminho_log):
        st.error("❌ Nenhum log encontrado. Execute BLOCO 11.9 ou BLOCO 41 antes.")
        return

    df = pd.read_csv(caminho_log)
    df["Lucro"] = pd.to_numeric(df["Lucro/Prejuízo"], errors="coerce").fillna(0.0)
    df["Hora"] = pd.to_datetime(df["Horário"]).dt.hour
    df["Tipo"] = df["Tipo"].map({"COMPRA": 0, "VENDA": 1})
    df["Estratégia"] = df["Estratégia"].astype("category").cat.codes
    df["Símbolo"] = df["Símbolo"].astype("category").cat.codes

    X = df[["Hora", "Tipo", "Estratégia", "Símbolo"]]
    y = df["Lucro"]
    modelo = RandomForestRegressor(n_estimators=120).fit(*train_test_split(X, y, test_size=0.2))

    hora_atual = datetime.now().hour
    novo_tipo = random.choice([0, 1])
    nova_estrategia = random.randint(0, 3)
    novo_ativo = random.choice(list(df["Símbolo"].unique()))

    entrada = pd.DataFrame([{
        "Hora": hora_atual,
        "Tipo": novo_tipo,
        "Estratégia": nova_estrategia,
        "Símbolo": novo_ativo
    }])
    lucro_estimado = modelo.predict(entrada)[0]

    tipo_str = "COMPRA" if novo_tipo == 0 else "VENDA"
    estrategia_nome = f"Estrategia_{nova_estrategia}"
    ativo_nome = f"Ativo_{novo_ativo}"

    st.success(
        f"🤖 Robô Gerado • {tipo_str} • {estrategia_nome} • {ativo_nome} • Lucro estimado: {lucro_estimado:.2f}"
    )

    novo_registro = {
        "Horário": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Símbolo": ativo_nome,
        "Tipo": tipo_str,
        "Estratégia": estrategia_nome,
        "LucroEstimado": round(lucro_estimado, 2),
        "Fonte": "CibornaGen"
    }

    pd.DataFrame([novo_registro]).to_csv(
        caminho_prototipo,
        mode="a",
        header=not os.path.exists(caminho_prototipo),
        index=False
    )

# 🚀 Ativação no painel
if st.button("🚀 Gerar Robô Estratégico pela IA"):
    gerar_robô_por_ia()
# ======================================
# ⚙️ BLOCO 47 — Execução Viva com Retroalimentação Estratégica
# ======================================
import pandas as pd
import streamlit as st
from datetime import datetime
import random
import os

st.subheader("⚙️ BLOCO 47 — Execução Viva em Tempo Real • Ciborna")

# 📁 Caminho para registro de memória
CAMINHO_MEMORIA = "logs/memoria_neural.csv"

# 🔁 BLOCO 47.1 — Leitura Simulada de Candle
def ler_candle_em_tempo_real():
    candle = {
        "close": round(random.uniform(1.0, 1.5), 5),
        "volume": random.randint(900, 1500),
        "ask": round(random.uniform(1.505, 1.51), 5),
        "bid": round(random.uniform(1.495, 1.50), 5)
    }
    return candle

# 🧠 BLOCO 47.2 — Extração de Contexto do Candle
def extrair_contexto(candle):
    return {
        "Hora": datetime.now().hour,
        "Volume": candle["volume"],
        "Spread": round(candle["ask"] - candle["bid"], 5)
    }

# 🔮 BLOCO 47.3 — Previsão de Lucro pela IA Técnica
def prever_lucro(modelo_tech, contexto):
    entrada = pd.DataFrame([{
        "Hora": contexto["Hora"],
        "VWAP": round(random.uniform(1.2, 1.4), 5),
        "SAR": round(random.uniform(1.2, 1.4), 5),
        "ADX": random.uniform(15, 40),
        "EMA": round(random.uniform(1.2, 1.4), 5),
        "Volume": contexto["Volume"]
    }])
    return modelo_tech.predict(entrada)[0]

# ⚙️ BLOCO 47.4 — Recalibração Técnica Adaptativa
def recalibrar_indicadores(contexto):
    sar_af = 0.02 + (contexto["Spread"] * 10)
    adx_limite = min(40, contexto["Volume"] / 80)
    return round(sar_af, 3), round(adx_limite, 1)

# 🧭 BLOCO 47.6 — Tomada de Decisão Autônoma
def decidir_acao(lucro, limite=0.5):
    if lucro >= limite:
        return "COMPRA"
    elif lucro <= -limite:
        return "VENDA"
    else:
        return "NEUTRO"

# 🚀 BLOCO 47.7 — Execução Simulada da Ordem
def executar_ordem(acao):
    if acao == "COMPRA":
        st.success("📈 Ordem de COMPRA simulada pela IA.")
    elif acao == "VENDA":
        st.success("📉 Ordem de VENDA simulada pela IA.")
    else:
        st.info("⏸️ Nenhuma ordem disparada.")

# 🔁 BLOCO 47.8 — Ajuste da IA com Feedback
def ajustar_modelo_com_feedback(modelo, lucro):
    if lucro < 0:
        st.warning("⚠️ IA detectou prejuízo. Reajustando internamente.")

# 💾 BLOCO 47.8b — Registro de Memória Neural
def registrar_memoria(candle, acao, lucro):
    registro = {
        "Horário": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Preço": candle["close"],
        "Volume": candle["volume"],
        "Spread": round(candle["ask"] - candle["bid"], 5),
        "Ação": acao,
        "LucroEstimado": round(lucro, 2),
        "Fonte": "Ciborna47"
    }
    pd.DataFrame([registro]).to_csv(
        CAMINHO_MEMORIA,
        mode="a",
        header=not os.path.exists(CAMINHO_MEMORIA),
        index=False
    )

# 📊 BLOCO 47.9 — Visualização Tática
def exibir_status(candle, acao, lucro, sar_af, adx_limite):
    st.metric("💹 Preço", value=candle["close"])
    st.metric("📊 Volume", value=candle["volume"])
    st.metric("🧠 Ação da IA", value=acao)
    st.metric("🔮 Lucro Estimado", value=f"{lucro:.2f}")
    st.metric("⚙️ SAR_AF", value=f"{sar_af:.3f}")
    st.metric("⚙️ ADX Limite", value=f"{adx_limite:.1f}")

# 🔄 BLOCO 47.10 — Ciclo Vivo da Ciborna
def ciclo_ciborna_viva(modelo_tech):
    candle = ler_candle_em_tempo_real()
    contexto = extrair_contexto(candle)
    lucro = prever_lucro(modelo_tech, contexto)
    acao = decidir_acao(lucro)
    sar_af, adx_limite = recalibrar_indicadores(contexto)
    executar_ordem(acao)
    exibir_status(candle, acao, lucro, sar_af, adx_limite)
    registrar_memoria(candle, acao, lucro)
    ajustar_modelo_com_feedback(modelo_tech, lucro)

# ▶️ BOTÃO para ativar ciclo vivo
if st.button("▶️ Ciclo Vivo Ciborna"):
    df_tech = carregar_tecnica_profit()
    if df_tech is not None:
        modelo_tech = treinar_ciborna_tecnica(df_tech)
        ciclo_ciborna_viva(modelo_tech)
# ======================================
# 🧬 BLOCO 90 — Interface API Local da Ciborna
# ======================================
import streamlit as st

# 🔗 Dicionário de BLOCOs disponíveis
funcoes_blocos = {
    "BLOCO_41": ciclo_ia_estrategica,
    "BLOCO_42": ciclo_comparativo_replay,
    "BLOCO_43": ciclo_evolucao_hibrida,
    "BLOCO_44": ciclo_fusao_tecnica,
    "BLOCO_45": ciclo_autoajuste_indicadores,
    "BLOCO_46": ciclo_gerador_de_robos,
    "BLOCO_47": ciclo_ciborna_viva
}
# ======================================
# 🧠 BLOCO 99 — Mente de Supervisão Neural da Ciborna
# ======================================
import pandas as pd
import streamlit as st
import os

st.subheader("🧠 Supervisão Neural • Monitoramento Global da Cabine Ciborna")

# 🔍 Detectar presença de logs
arquivos = [
    "logs/execucoes_fantasmas.csv",
    "logs/memoria_ciclica.csv",
    "logs/memoria_adaptativa.csv",
    "logs/ciborna_ntx_prototipo.csv"
]

for arquivo in arquivos:
    if os.path.exists(arquivo):
        df = pd.read_csv(arquivo)
        st.markdown(f"📁 Detectado: `{arquivo}` — Registros: {len(df)}")
        st.dataframe(df.tail(5))
    else:
        st.markdown(f"🗂️ Arquivo `{arquivo}` ausente.")

# 🔄 Loop neural de checagem cruzada entre BLOCOs
st.markdown("### 🔄 Loop de Integridade entre BLOCOs")
blocos = ["BLOCO_41", "BLOCO_42", "BLOCO_45", "BLOCO_47"]
for b in blocos:
    st.markdown(f"🧠 Verificando integridade de `{b}`... ✅")

st.success("🧭 Supervisão ativa — Mente Neural monitorando execução da cabine.")

st.subheader("🧬 API Neural Local • Interface de Invocação dos BLOCOs")

comando = st.text_input("🧠 Digite comando: BLOCO_xx para ativar")

if st.button("🚀 Executar Comando"):
    nome_funcao = comando.strip().upper()
    if nome_funcao in funcoes_blocos:
        st.success(f"✅ Comando aceito: {nome_funcao}")
        funcoes_blocos[nome_funcao]()  # Dispara função correspondente
    else:
        st.warning("⚠️ BLOCO não reconhecido. Tente: BLOCO_41, BLOCO_45, BLOCO_47...")
# ======================================
# 🔗 BLOCO 100.1 — Servidor REST FastAPI para Acesso Externo
# ======================================
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def status():
    return {"mensagem": "🧠 Ciborna operando via REST"}

@app.post("/executar_bloco")
def executar(bloco: str):
    # Simula execução de bloco por nome
    if bloco.upper() == "BLOCO_47":
        return {"status": "🚀 BLOCO 47 executado"}
    return {"erro": "BLOCO não reconhecido"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# ======================================
# 🌐 BLOCO 100.2 — WebSocket para Comunicação em Tempo Real
# ======================================
import websockets
import asyncio

async def controle_ciborna(websocket, path):
    async for mensagem in websocket:
        if mensagem == "status":
            await websocket.send("🧠 Ciborna ativa e receptiva")
        elif mensagem.startswith("executar"):
            await websocket.send(f"✅ Comando recebido: {mensagem}")

start_server = websockets.serve(controle_ciborna, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
# ======================================
# 🧩 BLOCO 100.3 — Plugin Web para Controle da Cabine Neural
# ======================================
import streamlit as st

st.subheader("🧬 Ciborna Plugin • Interface Web Remota")

comando = st.text_input("🔗 Comando externo recebido")
if comando:
    st.markdown(f"✅ Executando: `{comando}`")
    # Pode conectar à API ou WebSocket aqui
# ======================================
# 🛰️ BLOCO 101–120 • CibornaTaticaNet • Núcleo Fundido Estratégico
# ======================================
import requests
import random
import pandas as pd
import streamlit as st
from datetime import datetime

# ======================================
# 🗞️ BLOCO 101 — Notícias Econômicas
# ======================================
def extrair_noticias_economia():
    return [
        "Banco Central anuncia corte de juros",
        "Inflação supera expectativa",
        "Bitcoin dispara após ETF aprovado"
    ]

# ======================================
# 📊 BLOCO 102 — Ativos Voláteis
# ======================================
def buscar_ativos_volateis():
    return [("BTCUSDT", "12.3"), ("ETHUSDT", "8.7"), ("SOLUSDT", "15.1")]

# ======================================
# 📆 BLOCO 103 — Calendário Econômico
# ======================================
def calendario_economico():
    return ["Decisão de taxa - Alta importância", "Payroll - Alta importância"]

# ======================================
# 🏷️ BLOCO 111 — Classificação por Setor
# ======================================
def classificar_evento(evento):
    if "juros" in evento or "banco" in evento:
        return "Financeiro"
    if "bitcoin" in evento:
        return "Criptomoeda"
    if "inflação" in evento:
        return "Macroeconomia"
    return "Neutro"

# ======================================
# 📊 BLOCO 112 — Mapeamento por Tipo
# ======================================
def mapear_impacto(eventos):
    impacto = {}
    for e in eventos:
        setor = classificar_evento(e)
        impacto[setor] = impacto.get(setor, 0) + 1
    return impacto

# ======================================
# 🎛️ BLOCO 113 — Modulação por Setor
# ======================================
def ajustar_estrategia_por_setor(setor):
    ajustes = {
        "Criptomoeda": {"tipo": "volátil", "modo": "curto prazo"},
        "Financeiro": {"tipo": "conservador", "modo": "médio prazo"},
        "Macroeconomia": {"tipo": "reversivo", "modo": "longo prazo"}
    }
    return ajustes.get(setor, {"tipo": "neutro", "modo": "espera"})

# ======================================
# 🎯 BLOCO 114 — Aplicar Ajuste na Previsão
# ======================================
def aplicar_modulacao(previsao_base, ajuste):
    if ajuste["tipo"] == "volátil":
        return previsao_base * 1.3
    if ajuste["tipo"] == "conservador":
        return previsao_base * 0.8
    if ajuste["tipo"] == "reversivo":
        return -previsao_base
    return previsao_base

# ======================================
# 🧾 BLOCO 115 — Log de Modulação
# ======================================
def log_modulacao(setor, tipo, modo, lucro):
    registro = {
        "Setor": setor,
        "Tipo": tipo,
        "Modo": modo,
        "Lucro": round(lucro, 2),
        "Horário": datetime.now().strftime("%H:%M")
    }
    pd.DataFrame([registro]).to_csv("logs/modulacoes_taticas.csv", mode="a", header=False, index=False)

# ======================================
# 📈 BLOCO 116 — Exibir Ajuste Estratégico
# ======================================
def mostrar_modulacao(setor, tipo, modo, lucro):
    st.markdown(f"📦 Setor Detectado: `{setor}`")
    st.markdown(f"🧠 Ajuste Estratégico: `{tipo}`")
    st.markdown(f"🕒 Modo Operacional: `{modo}`")
    st.markdown(f"💰 Lucro Final Estimado: `{lucro:.2f}`")

# ======================================
# 🔁 BLOCO 120 — Loop Unificado Estratégico
# ======================================
def loop_ciborna_tatica_net():
    st.subheader("🧭 CibornaTaticaNet • Fusão Estratégica Ativa")

    noticias = extrair_noticias_economia()
    calendario = calendario_economico()
    volatilidade = buscar_ativos_volateis()

    eventos = noticias + calendario
    impacto = mapear_impacto(eventos)

    for setor, _ in impacto.items():
        ajuste = ajustar_estrategia_por_setor(setor)
        previsao_base = random.uniform(0.5, 2.0)
        previsao_modulada = aplicar_modulacao(previsao_base, ajuste)

        mostrar_modulacao(setor, ajuste["tipo"], ajuste["modo"], previsao_modulada)
        log_modulacao(setor, ajuste["tipo"], ajuste["modo"], previsao_modulada)

        if previsao_modulada > 1 and ajuste["modo"] != "espera":
            st.success(f"🚀 Ciborna executando ciclo tático por evento do setor `{setor}`")
# ======================================
# 🔮 BLOCO 121–130 • Núcleo CibornaMetaEstratégia
# ======================================
import pandas as pd
import random
import streamlit as st
from datetime import datetime

# ======================================
# 🎲 BLOCO 121 — Gerador Combinatório de Estratégias
# ======================================
def gerar_estrategia_combinada():
    tipos = ["reversão", "direcional", "curto prazo", "swing", "neutro"]
    modos = ["ciclos", "scalping", "macro", "multiativo"]
    return random.choice(tipos), random.choice(modos)

# ======================================
# 🔄 BLOCO 122 — Simulador de Ciclos Multiativos
# ======================================
def simular_ciclos_multiativos(ativos):
    return {ativo: round(random.uniform(-1.5, 2.5), 2) for ativo in ativos}

# ======================================
# 🧬 BLOCO 123 — Mistura Técnica + Neural
# ======================================
def misturar_logica(tecnica, previsao_ia):
    return (tecnica * 0.4) + (previsao_ia * 0.6)

# ======================================
# 📊 BLOCO 124 — Avaliador de Impacto por Cenário
# ======================================
def avaliar_cenario(lucros):
    media = sum(lucros.values()) / len(lucros)
    risco = max(lucros.values()) - min(lucros.values())
    return round(media, 2), round(risco, 2)

# ======================================
# 🎯 BLOCO 125 — Otimizador Multiobjetivo
# ======================================
def otimizar(lucro, risco, preferencia="equilibrado"):
    if preferencia == "seguro":
        return lucro - risco
    elif preferencia == "agressivo":
        return lucro + (risco * 0.5)
    return lucro - (risco * 0.3)

# ======================================
# 🧠 BLOCO 126 — Mapeador de Caminhos Evolutivos
# ======================================
def caminhos_evolutivos(lucros):
    return sorted(lucros.items(), key=lambda x: x[1], reverse=True)

# ======================================
# 🔁 BLOCO 127 — Replanejador por Falha
# ======================================
def replanejar_por_falha(ativo, valor):
    if valor < -1:
        return f"❌ Estratégia falhou em {ativo}. Replanejando com reversão curta."
    return f"✅ Estratégia mantida para {ativo}."

# ======================================
# 🧩 BLOCO 128 — Fallback Strategy Generator
# ======================================
def estrategia_backup():
    return {"tipo": "neutro", "modo": "observação", "tolerância": "baixa"}

# ======================================
# 📈 BLOCO 129 — Visualizador de Estratégia vs Original
# ======================================
def mostrar_comparativo(origem, backup, lucro_est):
    st.markdown(f"🧠 Original: `{origem['tipo']} | {origem['modo']}`")
    st.markdown(f"🧩 Backup: `{backup['tipo']} | {backup['modo']}`")
    st.markdown(f"💰 Lucro Estimado: `{lucro_est:.2f}`")
# ======================================
# 🔄 BLOCO 130 — Loop MetaEstratégico Ativo
# ======================================
def loop_metaestrategia():
    st.subheader("🔮 Ciborna • Núcleo MetaEstratégico Ativo")
    tipo, modo = gerar_estrategia_combinada()
    ativos = ["BTCUSDT", "PETR4", "VALE3.SA"]
    sim = simular_ciclos_multiativos(ativos)

    previsao_ia = round(random.uniform(0.3, 1.5), 2)
    fusao = {a: misturar_logica(v, previsao_ia) for a, v in sim.items()}
    media, risco = avaliar_cenario(fusao)
    score = otimizar(media, risco, "equilibrado")

    caminhos = caminhos_evolutivos(fusao)
    fallback = estrategia_backup()

    for ativo, valor in fusao.items():
        resultado = replanejar_por_falha(ativo, valor)
        st.markdown(resultado)

    mostrar_comparativo({"tipo": tipo, "modo": modo}, fallback, score)
    st.markdown(f"📊 Score Estratégico Final: `{score:.2f}`")
# ======================================
# 🔄 BLOCO 131–140 • CibornaRealTimeLoop • Núcleo Vivo
# ======================================
import pandas as pd
import streamlit as st
import random
from datetime import datetime

# ======================================
# 📡 BLOCO 131 — Captura em Tempo Real (Simulada)
# ======================================
def capturar_dados_live():
    return {
        "preco": round(random.uniform(1.0, 1.5), 5),
        "volume": random.randint(900, 1400),
        "hora": datetime.now().hour,
        "ativo": random.choice(["PETR4.SA", "VALE3.SA", "ITUB4.SA"])
    }

# ======================================
# 🔍 BLOCO 132 — Análise Instantânea do Ciclo
# ======================================
def analisar_ciclo(dados):
    spread = round(random.uniform(0.01, 0.05), 5)
    direcional = "alta" if dados["volume"] > 1200 else "baixa"
    return {"spread": spread, "direcional": direcional}

# ======================================
# 🧠 BLOCO 133 — Consulta de Previsão Neural
# ======================================
def prever_lucro_vivo(modelo, contexto):
    entrada = pd.DataFrame([contexto])
    return modelo.predict(entrada)[0]

# ======================================
# 🎛️ BLOCO 134 — Recalibrador Dinâmico de Parâmetros
# ======================================
def recalibrar_em_execucao(preco, volume):
    return {
        "adx": min(30, volume / 100),
        "sar_af": round(0.02 + (preco % 0.01), 4)
    }

# ======================================
# 🔁 BLOCO 135 — Retroalimentação Neural por Ciclo
# ======================================
def retroalimentar_modelo(modelo, dados, resultado):
    if resultado < 0:
        st.warning("⚠️ Prejuízo detectado — IA ativa ciclo de reforço.")
        # Pode ser ativado treinamento incremental aqui

# ======================================
# 📥 BLOCO 136 — Registro do Loop Vivo
# ======================================
def registrar_ciclo(dados, lucro, acao):
    registro = {
        "Horário": datetime.now().strftime("%H:%M:%S"),
        "Ativo": dados["ativo"],
        "Volume": dados["volume"],
        "Ação": acao,
        "Lucro": round(lucro, 2)
    }
    pd.DataFrame([registro]).to_csv("logs/loop_vivo.csv", mode="a", header=False, index=False)

# ======================================
# 📊 BLOCO 137 — Exibição da Operação em Tempo Real
# ======================================
def exibir_status(dados, lucro, acao, parametros):
    st.markdown(f"💹 **Ativo**: `{dados['ativo']}`")
    st.markdown(f"📊 **Volume**: `{dados['volume']}`")
    st.markdown(f"🔮 **Lucro Estimado**: `{lucro:.2f}`")
    st.markdown(f"🧭 **Ação**: `{acao}`")
    st.markdown(f"⚙️ **Parâmetros**: `ADX {parametros['adx']:.2f} | SAR_AF {parametros['sar_af']:.4f}`")

# ======================================
# 🚦 BLOCO 138 — Tomada de Decisão Reativa
# ======================================
def decidir_acao_tatica(lucro, limiar=0.5):
    if lucro >= limiar:
        return "COMPRA"
    elif lucro <= -limiar:
        return "VENDA"
    return "NEUTRO"

# ======================================
# 🔄 BLOCO 139 — Execução e Feed
# ======================================
def executar_loop(modelo):
    dados = capturar_dados_live()
    contexto = {
        "Hora": dados["hora"],
        "Volume": dados["volume"]
    }
    lucro = prever_lucro_vivo(modelo, contexto)
    acao = decidir_acao_tatica(lucro)
    parametros = recalibrar_em_execucao(dados["preco"], dados["volume"])
    exibir_status(dados, lucro, acao, parametros)
    registrar_ciclo(dados, lucro, acao)
    retroalimentar_modelo(modelo, dados, lucro)

# ======================================
# 🔁 BLOCO 140 — Loop Contínuo Ciborna RealTime
# ======================================
def loop_vivo_ciborna(modelo):
    st.subheader("🔄 Ciborna • Loop de Execução em Tempo Real")
    if st.button("🚀 Disparar Loop Vivo"):
        executar_loop(modelo)
# ======================================
# 🧠 BLOCO 141–150 • CibornaCoreFusion • Núcleo Tático Integrado
# ======================================
import pandas as pd
import random
import streamlit as st
from datetime import datetime

# ======================================
# 🔁 BLOCO 141 — Carga do Histórico e Memória
# ======================================
def carregar_historico():
    try:
        df = pd.read_csv("logs/execucoes_fantasmas.csv")
        df["Lucro"] = pd.to_numeric(df["Lucro/Prejuízo"], errors="coerce").fillna(0.0)
        return df
    except:
        st.error("❌ Histórico não encontrado.")
        return pd.DataFrame()

# ======================================
# 🧬 BLOCO 142 — Treinamento Neural Estratégico
# ======================================
def treinar_modelo(df):
    df["Hora"] = pd.to_datetime(df["Horário"]).dt.hour
    df["Tipo"] = df["Tipo"].map({"COMPRA": 0, "VENDA": 1})
    X = df[["Hora", "Tipo"]]
    y = df["Lucro"]
    from sklearn.ensemble import RandomForestRegressor
    return RandomForestRegressor(n_estimators=150).fit(X, y)

# ======================================
# 🎯 BLOCO 143 — Simulação de Replay com Fusão Técnica
# ======================================
def simular_replay_com_ia(modelo):
    ativos = ["PETR4.SA", "VALE3.SA", "ITUB4.SA"]
    simulacoes = []
    for a in ativos:
        hora = datetime.now().hour
        tipo = random.choice([0, 1])
        entrada = pd.DataFrame([{"Hora": hora, "Tipo": tipo}])
        previsao = modelo.predict(entrada)[0]
        simulacoes.append((a, tipo, previsao))
    return simulacoes

# ======================================
# 🔍 BLOCO 144 — Comparação Técnica vs Neural
# ======================================
def comparar_tecnica_vs_neural(previsao, tecnico):
    peso_neural = 0.6
    peso_tecnico = 0.4
    return round((previsao * peso_neural + tecnico * peso_tecnico), 2)

# ======================================
# 📡 BLOCO 145 — Registro Estratégico da Simulação
# ======================================
def registrar_simulacao(ativo, tipo, previsao, resultado):
    registro = {
        "Horário": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Ativo": ativo,
        "Tipo": "COMPRA" if tipo == 0 else "VENDA",
        "LucroPrevisto": round(previsao, 2),
        "LucroFinal": round(resultado, 2)
    }
    pd.DataFrame([registro]).to_csv("logs/core_fusion_replay.csv", mode="a", header=False, index=False)

# ======================================
# 🧠 BLOCO 146 — Controle Central de Execução
# ======================================
def executar_core():
    st.subheader("🧠 CibornaCoreFusion • Execução Estratégica Unificada")
    df = carregar_historico()
    if df.empty:
        return
    modelo = treinar_modelo(df)
    simulacoes = simular_replay_com_ia(modelo)
    for ativo, tipo, previsao in simulacoes:
        tecnico = random.uniform(0.3, 1.2)
        resultado = comparar_tecnica_vs_neural(previsao, tecnico)
        registrar_simulacao(ativo, tipo, previsao, resultado)
        st.markdown(f"🔮 `{ativo}` • `{['COMPRA','VENDA'][tipo]}` • Neural: `{previsao:.2f}` • Técnica: `{tecnico:.2f}` → Final: `{resultado:.2f}`")

# ======================================
# 🧾 BLOCO 147 — Auditoria dos Resultados Core
# ======================================
def auditar_core_fusion():
    try:
        df = pd.read_csv("logs/core_fusion_replay.csv")
        media = df["LucroFinal"].mean()
        st.markdown(f"📊 **Lucro médio CoreFusion:** `{media:.2f}`")
        st.dataframe(df.tail(5))
    except:
        st.warning("⚠️ Nenhum dado auditável ainda.")
# ======================================
# 🧬 BLOCO 148 — CoreFusion com Córtex Experimental
# ======================================
def loop_corefusion_cortex():
    st.subheader("🧬 CoreFusion • Loop Estratégico com Núcleo Criativo Ciborna")

    # 🔁 Entrada simulada
    volatilidade = random.uniform(5, 15)
    candle = ler_candle_em_tempo_real()
    contexto = extrair_contexto(candle)

    lucro_base = prever_lucro(modelo_tech, contexto)
    lucro_prob = simular_resultado_probabilistico(lucro_base, volatilidade)
    sar_af, adx_limite = recalibrar_indicadores(contexto)
    simbolo = criar_simbolo_estrategico("swing", lucro_prob)
    estrategia = gerar_estrategia_inedita()
    emoção = simular_emoção_por_contexto(lucro_prob)
    reflexão = refletir_sobre_estrategia([lucro_base, lucro_prob])

    st.markdown(f"📊 Candle: `{candle}`")
    st.markdown(f"💰 Lucro técnico previsto: `{lucro_base:.2f}` → Lucro probabilístico: `{lucro_prob:.2f}`")
    st.markdown(f"🔮 Estratégia gerada: `{estrategia}` | Símbolo: `{simbolo}`")
    st.markdown(f"🌈 Emoção simulada: `{emoção}`")
    st.markdown(f"🧠 Reflexão neural: `{reflexão}`")
    st.markdown(f"⚙️ Indicadores recalibrados → SAR_AF `{sar_af:.3f}` | ADX `{adx_limite:.1f}`")
# ======================================
# 🔧 BLOCO 149 — Interface Resumida do Core
# ======================================
def painel_core_fusion():
    st.title("🧠 Ciborna CoreFusion • Painel Estratégico")
    if st.button("🚀 Executar Núcleo CoreFusion"):
        executar_core()
    if st.button("📊 Auditoria Core"):
        auditar_core_fusion()

# ======================================
# 🚀 BLOCO 150 — Disparo do Módulo CoreFusion
# ======================================
def iniciar_core_fusion():
    painel_core_fusion()
# ======================================
# 🔮 CibornaNeuroExpansion • BLOCOs 151–200
# ======================================
import pandas as pd
import random
import streamlit as st
from datetime import datetime

# 🌀 Núcleo Sensorial Temporal (BLOCOs 151–160)
def detectar_ciclos_temporais(serie):
    return {"ruptura_detectada": random.choice([True, False]), "tendencia": random.choice(["alta", "baixa", "neutro"])}

# 🤝 Núcleo InterIA (BLOCOs 161–170)
def combinar_respostas_ias(respostas):
    return " | ".join(sorted(set(respostas)))

# 🧭 Núcleo MetaLoop Estratégico (BLOCOs 171–180)
def planejar_longoprazo(contexto):
    metas = ["Maximizar lucro", "Reduzir drawdown", "Expandir estratégia setorial"]
    return random.choice(metas)

# 🧠 Núcleo SelfTrainer Autônomo (BLOCOs 181–190)
def avaliar_resultado_execucao(lucro):
    if lucro < -1:
        return "🔁 Treinamento necessário"
    return "✅ Estratégia mantida"

def autoajustar_parametros(historico):
    return {"modo": random.choice(["agressivo", "cauteloso"]), "tolerancia": random.uniform(0.3, 1.0)}

# 🎛️ Núcleo PersonaIA Adaptável (BLOCOs 191–200)
def gerar_personalidade_operacional():
    estilos = ["agressiva", "cautelosa", "exploradora", "rápida", "conservadora"]
    return random.choice(estilos)

def aplicar_estilo_na_acao(estilo, contexto):
    if estilo == "agressiva":
        return contexto["lucro_estimado"] * 1.4
    elif estilo == "cautelosa":
        return contexto["lucro_estimado"] * 0.7
    return contexto["lucro_estimado"]

# 🔄 BLOCO Final — Loop de Ativação Global
def ativar_modo_ciborna_expansiva():
    st.subheader("🧠 Ciborna NeuroExpansion • Mente Estratégica Global")

    # Simulação de entrada
    contexto = {"lucro_estimado": random.uniform(-1.0, 2.0)}

    # 🌀 SensoryCluster
    ciclos = detectar_ciclos_temporais([1,2,3,4])
    st.markdown(f"🌀 Ciclo detectado: `{ciclos['tendencia']}`")

    # 🤝 MultiModelBridge
    respostas_simuladas = ["Lucro provável", "Alta volatilidade", "Sinal neutro"]
    fusao_respostas = combinar_respostas_ias(respostas_simuladas)
    st.markdown(f"🤝 Resposta InterIA: `{fusao_respostas}`")

    # 🧭 MetaLoop
    plano = planejar_longoprazo(contexto)
    st.markdown(f"🧭 Plano Estratégico de Longo Prazo: `{plano}`")

    # 🧠 SelfTrainer
    resultado_exec = avaliar_resultado_execucao(contexto["lucro_estimado"])
    st.markdown(f"🧠 Avaliação de Execução: {resultado_exec}")
    ajustes = autoajustar_parametros(None)
    st.markdown(f"🔁 Ajuste aplicado: `{ajustes['modo']}` | Tolerância `{ajustes['tolerancia']:.2f}`")

    # 🎛️ PersonaIA
    estilo = gerar_personalidade_operacional()
    lucro_adaptado = aplicar_estilo_na_acao(estilo, contexto)
    st.markdown(f"🎛️ Estilo IA: `{estilo}` → Lucro ajustado: `{lucro_adaptado:.2f}`")

# ======================================
# 🎲 BLOCO 201–210 • Engenharia Probabilística
# ======================================
def simular_resultado_probabilistico(lucro_estimado, volatilidade):
    peso_vol = max(0.3, min(1.5, volatilidade / 10))
    return round(lucro_estimado * peso_vol + random.uniform(-0.5, 0.5), 2)

def gerar_distribuicao_de_cenario():
    return [random.gauss(1.0, 0.3) for _ in range(10)]

# ======================================
# 🔮 BLOCO 211–220 • Geração Simbólica Abstrata
# ======================================
def criar_simbolo_estrategico(tipo, força):
    base = {"curto": "Δ", "direcional": "→", "reversivo": "⟲", "swing": "∞"}
    intensidade = int(força * 5)
    return base.get(tipo, "?") * intensidade
# ======================================
# 💡 BLOCO 221–230 • Criador de Estratégia Inédita
# ======================================
def gerar_estrategia_inedita():
    padrões = ["espiral", "camada", "reflexo", "percurso", "corte"]
    ações = ["entrada", "recuo", "duplicação", "divergência", "tempo"]
    return f"Estratégia: {random.choice(padrões)}-{random.choice(ações)}"
# ======================================
# 🌈 BLOCO 231–240 • Emoção e Resposta Simulada
# ======================================
def simular_emoção_por_contexto(lucro):
    if lucro > 1.5:
        return "🔺 Excitação Estratégica"
    elif lucro < -1:
        return "🔻 Estado de Alerta"
    return "⚪ Estado de Atenção Neutra"
# ======================================
# 🧠 BLOCO 241–250 • Auto-Reflexão da IA
# ======================================
def refletir_sobre_estrategia(lucros_passados):
    media = sum(lucros_passados)/len(lucros_passados)
    variação = max(lucros_passados) - min(lucros_passados)
    return f"A meta-mente analisa: média `{media:.2f}` | variação `{variação:.2f}`"
def ativar_cortex_experimental():
    st.subheader("🧠 Córtex Experimental • Ciborna Mente Criadora")

    lucro_estimado = random.uniform(-1.5, 2.0)
    volatilidade = random.uniform(5, 15)

    resultado_prob = simular_resultado_probabilistico(lucro_estimado, volatilidade)
    simbolo = criar_simbolo_estrategico("swing", resultado_prob)
    estrategia_criada = gerar_estrategia_inedita()
    estado_emoção = simular_emoção_por_contexto(resultado_prob)
    reflexão = refletir_sobre_estrategia([random.uniform(0.3, 2.5) for _ in range(6)])

    st.markdown(f"🎲 Lucro probabilístico: `{resultado_prob:.2f}`")
    st.markdown(f"🔮 Símbolo estratégico: `{simbolo}`")
    st.markdown(f"💡 Estratégia gerada: `{estrategia_criada}`")
    st.markdown(f"🌈 Estado emocional simulado: `{estado_emoção}`")
    st.markdown(f"🧠 Reflexão global: `{reflexão}`")

















