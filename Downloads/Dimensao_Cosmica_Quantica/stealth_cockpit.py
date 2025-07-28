# 📂 [STEALTH COCKPIT v1.0] — Painel Visual Neural da Ciborna
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from ciborna.core import StrategyEngine, Executor, DataBridge, RiskManager

st.set_page_config(page_title="[Ciborna Stealth]", layout="wide")

# [01] Título e status
st.title("🧠 [01] Ciborna Neural Terminal")
st.caption("DOLAR2025INTELIGENTE • Modo Tático Ativo • Interface estilo Profit")

# [02] Seleção de ativo
ativos_b3 = ["PETR4", "VALE3", "ITUB4", "ABEV3", "BBAS3", "WDOQ25", "WINQ25"]
ativo_selecionado = st.selectbox("[02] Ativo B3", ativos_b3)

# [03] Controle de execução tática
execucao_ativa = st.toggle("[03] Execução Neural Ativa")

# [04] Gráfico candlestick
candles = pd.DataFrame(DataBridge.load_dummy_data())
st.subheader(f"[04] Gráfico Candlestick de {ativo_selecionado} (Simulado)")

fig = go.Figure(data=[go.Candlestick(
    x=candles["time"],
    open=candles["open"],
    high=candles["high"],
    low=candles["low"],
    close=candles["close"],
    increasing_line_color='green',
    decreasing_line_color='red'
)])
fig.update_layout(height=300, margin=dict(t=30, b=10), xaxis_rangeslider_visible=False)
st.plotly_chart(fig, use_container_width=True)

# [05] Análise do candle selecionado
selected = st.selectbox("[05] Selecionar Candle", candles.to_dict("records"), format_func=lambda x: x["time"])
if selected:
    decision = StrategyEngine.run(candle=selected)
    acao = decision["acao"] or "❌ Nenhuma"
    st.success(f"[05] Ação Tática: **{acao.upper()}**")
    st.caption(f"📊 Detalhes: {decision['detalhe']}")

# [06] Quadro de comandos operacionais
st.subheader("[06] Comandos de Execução")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🛒 Comprar Agora"):
        if execucao_ativa: Executor.test_run()
with col2:
    if st.button("📤 Vender Agora"):
        if execucao_ativa: Executor.test_run()
with col3:
    if st.button("❌ Fechar Posição"):
        st.warning("[06] Posição encerrada (simulada).")

# [07] Validação de risco
st.subheader("[07] Risco Tático")
if st.button("🔒 Validar Risco"):
    RiskManager.validate(dummy=True)

# [08] Rodapé informativo
st.divider()
st.caption(f"[08] Status: Ativo - {ativo_selecionado} | Execução - {'Ativa' if execucao_ativa else 'Pausada'}")
# [09] Curva de Capital Neural (Simulada)
st.subheader("[09] Evolução Simulada de Capital")

# Simula ganhos/perdas por candle
capital_inicial = 10000
capital = [capital_inicial]
registro = []

for c in candles.to_dict("records"):
    resultado = StrategyEngine.run(candle=c)
    acao = resultado["acao"]
    # Simulação simples: +50 se subida, -50 se descida (fictício)
    delta = 50 if acao == "comprar" else (-50 if acao == "vender" else 0)
    capital.append(capital[-1] + delta)
    registro.append({"Horário": c["time"], "Ação": acao or "neutro", "Lucro": delta})

# Cria gráfico
df_capital = pd.DataFrame({"Hora": ["start"] + [r["Horário"] for r in registro], "Capital": capital})
st.line_chart(df_capital.set_index("Hora"))

# Mostra registro tático
st.dataframe(pd.DataFrame(registro), use_container_width=True)

# [10] Estratégia Paralela
st.subheader("[10] Nova Estratégia com Outro Ativo")
if st.button("🧠 Iniciar Nova Estratégia"):
    st.info("🔁 Pronto para iniciar nova operação com ativo diferente.")

# [11] Estratégia de Posicionamento Diário
st.subheader("[11] Estratégia de Posicionamento para o Próximo Pregão")

import datetime
agora = datetime.datetime.now()
ultimo_horario = "17:00"

if agora.strftime("%H:%M") >= ultimo_horario:
    ultimo_candle = candles.iloc[-1]
    resultado = StrategyEngine.run(candle=ultimo_candle)
    acao = resultado["acao"] or "neutra"
    
    st.info(f"🧠 Estratégia definida às {agora.strftime('%H:%M')} com base no fechamento.")
    if acao == "comprar":
        st.success("✅ Posicionamento: Comprar no próximo pregão")
    elif acao == "vender":
        st.warning("⚠️ Posicionamento: Vender no próximo pregão")
    else:
        st.caption("📘 Nenhum posicionamento definido para amanhã")

    # Simulação de posicionamento no índice ou ações
    proximo_ativo = st.selectbox("🎯 Ativo para posicionar amanhã", ["WINFUT", "PETR4", "VALE3", "ITUB4"])
    st.write(f"🔮 Ciborna estará pronta para operar {proximo_ativo} amanhã com base na estratégia de hoje.")
else:
    st.caption("🕒 Aguardando fechamento do mercado para definir posicionamento...")
# ====================================
# [00.A] Importações essenciais
# ====================================
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import MetaTrader5 as mt5
import yfinance as yf
import os

# ====================================
# [00.B] Diagnóstico MetaTrader 5
# ====================================
def diagnostico_mt5():
    if not mt5.initialize():
        st.error("❌ MT5 não inicializado.")
        return
    ativo = "EURUSD"
    info = mt5.symbol_info_tick(ativo)
    if info and info.bid > 0:
        st.success(f"✅ MT5 OK | {ativo} BID: {info.bid:.5f} | ASK: {info.ask:.5f}")
    else:
        st.warning(f"⚠️ MT5 sem cotação válida para {ativo}")
    mt5.shutdown()

st.subheader("[00.B] Diagnóstico MT5")
diagnostico_mt5()

# ====================================
# [00.C] Cotação do Dólar
# ====================================
st.subheader("[00.C] Cotação Dólar BRL/USD")
try:
    dol = yf.Ticker("BRL=X")
    hist = dol.history(period="1d")
    preco = round(hist["Close"].iloc[-1], 4)
    hora = hist.index[-1].strftime("%H:%M")
    st.metric("💰 BRL/USD", f"R$ {preco}")
    st.caption(f"⏰ Cotado às {hora}")
except:
    st.warning("⚠️ Dólar indisponível")

# ====================================
# [00.D] Cotações internacionais
# ====================================
st.subheader("[00.D] Moedas Globais")
moedas = {
    "EUR/USD": "EURUSD=X",
    "GBP/USD": "GBPUSD=X",
    "JPY/USD": "JPY=X"
}
for nome, ticker in moedas.items():
    try:
        preco = round(yf.Ticker(ticker).history(period="1d")["Close"].iloc[-1], 4)
        st.metric(f"🌍 {nome}", preco)
    except:
        st.caption(f"🔘 {nome}: falhou")

# ====================================
# [00.E] Leitura de CSV tática
# ====================================
CAMINHO_CSV = "dados_dolar.csv"
try:
    df = pd.read_csv(CAMINHO_CSV, sep=",", on_bad_lines="skip")
    df.rename(columns={
        "fechamento": "close",
        "volume_tick": "volume",
        "saida_estrategia": "sinal"
    }, inplace=True)
    colunas = ["close", "volume", "sinal"]
    if all(col in df.columns for col in colunas):
        st.success("📄 CSV OK com colunas válidas")
    else:
        st.warning("⚠️ CSV incompleto")
        st.write("Colunas encontradas:", df.columns.tolist())
except FileNotFoundError:
    st.error(f"❌ CSV '{CAMINHO_CSV}' não encontrado")
    df = pd.DataFrame()

# ====================================
# [00.F] Seletor de inteligência
# ====================================
modo_ia = st.radio("🎛️ Modo de Estratégia:", ["📈 Estratégia Fixa", "🧬 Rede Neural", "📊 Fluxo de Ordens"])
st.caption(f"🧠 Inteligência ativa: {modo_ia}")

# ====================================
# [00.G] Book Estratégico EUR/USD
# ====================================
book_exemplo = pd.DataFrame({
    "Faixa": ["🔹 0.9100", "🔸 0.9200", "🔺 0.9400"],
    "Tipo": ["Compra Forte", "Consolidação", "Venda"],
    "Volume": [150000, 60000, 120000]
})
st.sidebar.markdown("📘 Book Estratégico")
for _, row in book_exemplo.iterrows():
    st.sidebar.write(f"{row['Faixa']} | {row['Tipo']} | Vol: {row['Volume']:,}")
# ======================================
# 🔢 BLOCO 08 — Gráfico EUR/USD com destaque de preço
# ======================================

import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.subheader("📈 Gráfico Tático do EUR/USD (1 minuto)")

try:
    df_graf = yf.Ticker("EURUSD=X").history(period="1d", interval="1m")

    if df_graf is not None and not df_graf.empty:
        preco_atual_eur = df_graf["Close"].iloc[-1]

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df_graf.index,
            y=df_graf["Close"],
            line=dict(color="royalblue"),
            name="EUR/USD"
        ))

        fig.add_trace(go.Scatter(
            x=[df_graf.index[-1]],
            y=[preco_atual_eur],
            mode="markers+text",
            text=[f"{preco_atual_eur:.5f}"],
            textposition="top center",
            marker=dict(color="crimson", size=10),
            name="Preço Atual"
        ))

        fig.update_layout(
            title="EUR/USD - Últimas 24h (1m)",
            xaxis_title="Horário",
            yaxis_title="Preço",
            template="plotly_white",
            height=400
        )

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("⚠️ Dados de cotação indisponíveis no momento.")
except Exception as e:
    st.error(f"❌ Erro ao gerar gráfico: {e}")
# ======================================
# 🔢 BLOCO 08.1 — Gráfico de Candles (autoatualização)
# ======================================
from streamlit_autorefresh import st_autorefresh
import yfinance as yf

st_autorefresh(interval=120000, key="chart_refresh")
st.subheader("📊 Gráfico Candlestick EUR/USD")

try:
    dados_candle = yf.Ticker("EURUSD=X").history(period="1d", interval="1m")
    if not dados_candle.empty:
        st.line_chart(dados_candle["Close"])
except Exception as e:
    st.error(f"❌ Erro ao carregar gráfico: {e}")
# ======================================
# 🔢 BLOCO 10 — Alerta ao Rompimento EUR/USD
# ======================================
import streamlit as st
import pandas as pd

st.subheader("📛 Verificador de Rompimento EUR/USD")

def verificar_rompimento(df, faixa_resistencia=1.16900, ativo="EURUSD"):
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

        ativo = st.text_input("💹 Ativo para verificar", "EURUSD")
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
# ======================================
# 🔢 BLOCO 11.5 — Curva de Capital Acumulado
# ======================================
st.subheader("🪙 Evolução Acumulada de Capital (Curva de Performance)")

caminho_csv = "logs/execucoes_operacionais.csv"

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
        df.sort_values("Horário", inplace=True)
        df["Capital Acumulado"] = df[coluna_lucro].cumsum()

        st.markdown("### 📈 Curva de Capital")
        st.line_chart(df.set_index("Horário")["Capital Acumulado"])
    else:
       st.error("❌ Coluna de lucro não encontrada para cálculo acumulado.")
else:
    st.warning("⚠️ Arquivo de execução não encontrado.")

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

            ativo = st.selectbox("💹 Ativo para simulação", ["EURUSD", "BTCUSD", "PETR4.SA"])
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

import os
import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from datetime import datetime

st.subheader("🧠 Previsão Neural de Lucro por Contexto Operacional")

# 🔹 Caminho do histórico operacional
caminho_csv = "logs/execucoes_operacionais.csv"

if os.path.exists(caminho_csv):
    df = pd.read_csv(caminho_csv)
    st.write("📋 Colunas detectadas:", df.columns.tolist())

    # 🔹 Conversão da coluna 'Horário'
    if "Horário" in df.columns:
        try:
            df["Hora"] = pd.to_datetime(df["Horário"], errors="coerce").dt.hour
        except Exception as e:
            st.error(f"⚠️ Erro ao converter 'Horário': {e}")
    else:
        st.warning("🕒 Coluna 'Horário' não encontrada no CSV")

    # 🔹 Verifica colunas necessárias
    colunas_minimas = {"Hora", "Lucro", "Tipo"}
    if colunas_minimas.issubset(set(df.columns)):
        # 🔍 Preparação dos dados
        X = df[["Hora", "Tipo"]]
        y = df["Lucro"]

        # 🔧 Codifica 'Tipo' (ex: COMPRA = 0, VENDA = 1)
        X["Tipo"] = X["Tipo"].apply(lambda x: 0 if x.upper() == "COMPRA" else 1)

        # 🔁 Divide em treino e teste
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        # 🤖 Treina o modelo
        modelo = RandomForestRegressor(n_estimators=100, random_state=42)
        modelo.fit(X_train, y_train)

        # 📊 Avaliação e exibição de previsão
        score = modelo.score(X_test, y_test)
        st.markdown(f"✅ Precisão do modelo: `{score:.2%}`")

        exemplo = pd.DataFrame({"Hora": [10], "Tipo": [0]})  # Simulação: 10h COMPRA
        previsao = modelo.predict(exemplo)[0]
        st.markdown(f"🔮 Previsão de lucro para COMPRA às 10h: `{previsao:.2f}`")

    else:
        st.error("❌ Colunas mínimas ausentes: 'Hora', 'Lucro', 'Tipo'")

else:
    st.error(f"❌ Arquivo não encontrado em: `{caminho_csv}`")

