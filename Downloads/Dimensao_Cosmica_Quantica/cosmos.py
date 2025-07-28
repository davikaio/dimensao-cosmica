# ------------------------ IMPORTAÇÕES BÁSICAS ------------------------

import sys
import os
import streamlit as st
import pandas as pd
import openpyxl
import joblib
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Garante que a pasta atual esteja no sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# ------------------------ IMPORTAÇÕES INTERNAS ------------------------

from scripts.estrategias import EstrategiaDolarInteligente
from scripts.fluxo_ordens import AnaliseFluxoOrdens
from scripts.rede_neural import treinar_modelo, prever
from scripts.utils import check_colunas
from mt5_stream import obter_candle_e_book

# ------------------------ CONFIG STREAMLIT ------------------------

CAMINHO_PLANILHA = r"C:\Dimensao_Cosmica_Quantica\cotacao_dol.xlsx"
CAMINHO_DADOS = "dados_dolar.csv"

st.set_page_config(page_title="Cockpit Ciborna", page_icon="🤖", layout="centered")
st.title("🤖 CIBORNA INTELIGENTE - MONITORAMENTO ATIVO")
st.image("ciborna.png", width=180, caption="Ciborna Online")

# ------------------------ DADOS DA PLANILHA ------------------------

try:
    wb = openpyxl.load_workbook(CAMINHO_PLANILHA, data_only=True)
    aba = wb.active
    col1, col2, col3 = st.columns(3)
    col1.metric("📈 Último", f"R$ {aba['A1'].value}")
    col2.metric("🕐 Hora", str(aba['A2'].value))
    col3.metric("📊 Volume", str(aba['A3'].value))
except Exception as e:
    st.error(f"Erro ao carregar planilha: {e}")

# ------------------------ MODO REPLAY: CÉREBRO ATIVO ------------------------

try:
    df = pd.read_csv(CAMINHO_DADOS)
except FileNotFoundError:
    st.warning("⚠️ Arquivo 'dados_dolar.csv' não encontrado.")
    df = pd.DataFrame()

modo = st.radio("🧠 Selecione o cérebro do Ciborna:", [
    "📈 Estratégia Fixa",
    "🧬 Rede Neural",
    "📊 Fluxo de Ordens"
])

if not df.empty:
    if not any(col in df.columns for col in ['volume', 'tick_volume']):
        st.error("❌ Coluna 'volume' ou 'tick_volume' não encontrada.")
    elif not check_colunas(df):
        st.warning("⚠️ Problemas estruturais nas colunas.")
    else:
        try:
            if modo == "📈 Estratégia Fixa":
                bot = EstrategiaDolarInteligente()
                df = bot.executar(df)

            elif modo == "🧬 Rede Neural":
                df_validado = df.dropna()
                if 'sinal' in df_validado.columns:
                    modelo, scaler, encoder = treinar_modelo(df_validado)
                    df = prever(df_validado, modelo, scaler, encoder)
                    joblib.dump(modelo, "modelo_treinado.joblib")
                    joblib.dump(scaler, "scaler.save")
                    joblib.dump(encoder, "encoder.save")
                else:
                    st.warning("⚠️ Coluna 'sinal' não encontrada no DataFrame.")

            elif modo == "📊 Fluxo de Ordens":
                analise = AnaliseFluxoOrdens()
                df = analise.executar(df)

            st.success(f"✅ Análise concluída: {modo}")
            st.dataframe(df.tail(15))

            # ------------------------ GRÁFICO DE SINAIS ------------------------

            def plotar_grafico_sinais(df, ativo):
                fig = make_subplots(rows=1, cols=1, shared_xaxes=True)

                fig.add_trace(go.Candlestick(
                    x=df.index,
                    open=df['open'],
                    high=df['high'],
                    low=df['low'],
                    close=df['close'],
                    name='Candle'), row=1, col=1)

                cores = {
                    'COMPRA': 'green',
                    'VENDA': 'red',
                    'SAIR_COMPRA': 'orange',
                    'SAIR_VENDA': 'orange',
                    'COMPRA_ATIVA': 'lime',
                    'VENDA_ATIVA': 'crimson'
                }

                # Sinais reais
                for sinal, cor in cores.items():
                    df_sinal = df[df['sinal'] == sinal]
                    if not df_sinal.empty:
                        fig.add_trace(go.Scatter(
                            x=df_sinal.index,
                            y=df_sinal['close'],
                            mode='markers',
                            marker=dict(color=cor, size=10),
                            name=sinal), row=1, col=1)

                # Sinais previstos (se existirem)
                if 'sinal_previsto' in df.columns:
                    df_prev = df.copy()
                    df_prev['sinal'] = df_prev['sinal_previsto']
                    for sinal, cor in cores.items():
                        df_sinal = df_prev[df_prev['sinal'] == sinal]
                        if not df_sinal.empty:
                            fig.add_trace(go.Scatter(
                                x=df_sinal.index,
                                y=df_sinal['close'],
                                mode='markers',
                                marker=dict(color=cor, size=8, symbol="x"),
                                name=f"{sinal} (previsto)"), row=1, col=1)

                fig.update_layout(
                    title=f"📊 Gráfico de Sinais — {ativo}",
                    xaxis_rangeslider_visible=False,
                    height=500
                )
                return fig

            fig = plotar_grafico_sinais(df, ativo="REPLAY")
            st.plotly_chart(fig, use_container_width=True)

        except Exception as e:
            st.error(f"Erro no processamento do modo {modo}: {e}")

# ------------------------ MONITORAMENTO AO VIVO COM MT5 ------------------------

st.divider()
st.markdown("### 🌐 Dados em tempo real via MT5 da XP")

ativo = st.selectbox("📌 Selecione o ativo:", ["PETR4", "VALE3", "WINQ25", "WDOQ25", "BOVA11"])

@st.cache_data(ttl=5)
def obter_dados_ao_vivo(ativo):
    return obter_candle_e_book(ativo)

try:
    df_live, book = obter_dados_ao_vivo(ativo)

    if df_live.empty:
        st.warning(f"⚠️ Nenhum candle recebido para {ativo}.")
    else:
        st.subheader(f"📈 Último Candle (1min) — {ativo}")
        st.dataframe(df_live[['open', 'high', 'low', 'close', 'tick_volume']])

    if not book:
        st.info(f"ℹ️ Livro de ofertas de {ativo} está vazio ou indisponível.")
    else:
        st.subheader(f"📘 Book de Ofertas — {ativo}")
        for entry in book:
            tipo = "🟢 Compra" if entry.type == 1 else "🔴 Venda"
            st.markdown(f"**{tipo}** | R$ {entry.price:.2f} | Vol: {entry.volume}")

except Exception as e:
    st.error(f"Erro ao obter dados ao vivo: {e}")
