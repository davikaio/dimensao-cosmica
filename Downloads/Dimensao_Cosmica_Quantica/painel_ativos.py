import pandas as pd
import streamlit as st
import altair as alt

# 🔄 Leitura do CSV
df = pd.read_csv("ativos_simulados.csv", sep=";")

st.title("📈 Painel PRO — Tendência, Book de Ofertas e DOM")

# 🎯 Filtro de ativo
ativos = df['Asset'].unique()
ativo_selecionado = st.selectbox("Selecionar ativo", ativos)

df_ativo = df[df['Asset'] == ativo_selecionado]

# 📊 Gráfico de linha de preço (Último vs. Máximo vs. Mínimo)
st.subheader("📈 Tendência de Preço")

grafico = alt.Chart(df_ativo).transform_fold(
    ['Último', 'Máximo', 'Mínimo'],
    as_=['Tipo', 'Valor']
).mark_line().encode(
    x=alt.X('Hora:N', title='Hora'),
    y=alt.Y('Valor:Q', title='Preço'),
    color=alt.Color('Tipo:N', scale=alt.Scale(domain=['Último','Máximo','Mínimo'],
                                               range=['#1e40af','#10b981','#ef4444']))
).properties(height=300)

st.altair_chart(grafico, use_container_width=True)

# Book de Ofertas Simulado
st.subheader("📦 Book de Ofertas Simulado")

preco_base = df_ativo['Preco_Fechamento'].iloc[0]  # ← ESTE É O PONTO QUE VOCÊ CITOU

book_data = {
    'Oferta': ['Compra', 'Compra', 'Compra', 'Venda', 'Venda', 'Venda'],
    'Preço': [preco_base - 0.01, preco_base - 0.02, preco_base - 0.03,
              preco_base + 0.01, preco_base + 0.02, preco_base + 0.03],
    'Quantidade': [1000, 800, 500, 900, 700, 300]
}
book_df = pd.DataFrame(book_data)


def cor_book(row):
    if row['Oferta'] == "Compra":
        return ['background-color: #3b82f6; color: white'] * len(row)
    else:
        return ['background-color: #ef4444; color: white'] * len(row)

st.dataframe(book_df.style.apply(cor_book, axis=1))

# 🔥 Super DOM Visual
st.subheader("🎯 Super DOM Visual")

dom_levels = {
    'Preço': [df_ativo['Último'].values[0] + i*0.01 for i in range(-5, 6)],
    'Volume': [500 + abs(i)*150 for i in range(-5, 6)]
}
dom_df = pd.DataFrame(dom_levels)

dom_chart = alt.Chart(dom_df).mark_bar().encode(
    x=alt.X('Volume:Q', title='Volume'),
    y=alt.Y('Preço:Q', title='Preço', sort='descending'),
    color=alt.value('#3b82f6')  # Azul DOM
).properties(height=400)

st.altair_chart(dom_chart, use_container_width=True)
import pandas as pd
import streamlit as st

# Título do painel
st.title("📊 Painel de Ativos com Destaques e Filtros")

# Leitura do CSV
df = pd.read_csv("ativos_simulados.csv", sep=";")

# 🎯 Filtros interativos
ativos = df['Asset'].unique()
ativo_selecionado = st.selectbox("Selecionar ativo", ["Todos"] + list(ativos))

sermedia_opcoes = df['SERMEDIA'].unique()
sermedia_selecionado = st.selectbox("Filtrar por SERMEDIA", ["Todos"] + list(sermedia_opcoes))

# Aplicar filtros
df_filtrado = df.copy()
if ativo_selecionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado['Asset'] == ativo_selecionado]
if sermedia_selecionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado['SERMEDIA'] == sermedia_selecionado]

# 🎨 Realce condicional baseado no ADX e SERMEDIA
def cor_linha(row):
    if row['ADX'] >= 30 and row['SERMEDIA'] == "Alta":
        return ['background-color: #10b981; color: white'] * len(row)
    elif row['ADX'] < 25 and row['SERMEDIA'] == "Neutro":
        return ['background-color: #fbbf24; color: black'] * len(row)
    else:
        return [''] * len(row)

# Exibir tabela estilizada
st.dataframe(df_filtrado.style.apply(cor_linha, axis=1))

# 📌 Exibir total de ativos filtrados
st.caption(f"Total exibido: {len(df_filtrado)} ativos")
