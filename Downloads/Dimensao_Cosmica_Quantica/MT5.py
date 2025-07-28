import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="SOMBRA DO MERCADO", layout="wide")

st.title("🫥 SOMBRA DO MERCADO")
st.subheader("Cockpit de Operações Ativado")
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("✅ Aprovar Entrada"):
        st.success("Entrada aprovada. Ordem autorizada.")
        st.session_state["ultimo_acao"] = "Aprovada"

with col2:
    if st.button("❌ Cancelar Entrada"):
        st.warning("Entrada cancelada. Nenhuma execução liberada.")
        st.session_state["ultimo_acao"] = "Cancelada"

with col3:
    if st.button("🧠 Ativar Modo Aprendizado"):
        st.info("Modo aprendizado ativado. Dados em coleta.")
        st.session_state["ultimo_acao"] = "Aprendizado"

st.markdown("---")
st.subheader("📜 LOG DE AÇÃO RECENTE")

if "ultimo_acao" in st.session_state:
    st.markdown(f"Ação realizada: **{st.session_state['ultimo_acao']}**")
else:
    st.markdown("Nenhuma ação realizada ainda.")

st.markdown("---")
st.subheader("📊 Histórico de Spread Simulado")

df = pd.DataFrame({
    "Operação": ["#1", "#2", "#3", "#4", "#5", "#6"],
    "Spread": [0.4, 0.7, 1.1, 0.3, 1.4, 0.9],
    "Resultado": ["Gain", "Gain", "Loss", "Gain", "Loss", "Loss"]
})

fig, ax = plt.subplots()
colors = df["Resultado"].map({"Gain": "green", "Loss": "red"})
ax.bar(df["Operação"], df["Spread"], color=colors)
ax.set_xlabel("Execuções")
ax.set_ylabel("Spread")
ax.set_title("Spreads Recentes (Simulado)")

st.pyplot(fig)

st.caption("🫥 Sombra do Mercado • Painel v1.0 • Núcleo visual operacional")