import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import requests
import time
import random
from datetime import datetime
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh

# ======================================
# ⚙️ CONFIGURAÇÃO INICIAL
# ======================================
st.set_page_config(
    page_title="🧠 Ciborna Neural Console - Enhanced",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================
# 🌐 CONFIGURAÇÃO DA API
# ======================================
API_BASE_URL = "http://localhost:5000/api/market"

# ======================================
# 🛠️ FUNÇÕES UTILITÁRIAS
# ======================================

@st.cache_data(ttl=5)  # Cache por 5 segundos para dados em tempo real
def get_market_status():
    """Obtém o status da API de mercado"""
    try:
        response = requests.get(f"{API_BASE_URL}/status", timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        st.error(f"Erro ao conectar com a API: {e}")
        return None

@st.cache_data(ttl=2)  # Cache por 2 segundos
def get_book_data(symbol="EURUSD"):
    """Obtém dados do book de ofertas"""
    try:
        response = requests.get(f"{API_BASE_URL}/book/{symbol}", timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        st.error(f"Erro ao obter book de ofertas: {e}")
        return None

@st.cache_data(ttl=1)  # Cache por 1 segundo para ticks
def get_tick_data(symbol="EURUSD"):
    """Obtém dados de tick"""
    try:
        response = requests.get(f"{API_BASE_URL}/tick/{symbol}", timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        st.error(f"Erro ao obter dados de tick: {e}")
        return None

@st.cache_data(ttl=10)  # Cache por 10 segundos para candles
def get_candles_data(symbol="EURUSD"):
    """Obtém dados de candles"""
    try:
        response = requests.get(f"{API_BASE_URL}/candles/{symbol}", timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        st.error(f"Erro ao obter dados de candles: {e}")
        return None

def start_market_simulation():
    """Inicia a simulação de mercado"""
    try:
        response = requests.post(f"{API_BASE_URL}/start", timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        st.error(f"Erro ao iniciar simulação: {e}")
        return None

def stop_market_simulation():
    """Para a simulação de mercado"""
    try:
        response = requests.post(f"{API_BASE_URL}/stop", timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        st.error(f"Erro ao parar simulação: {e}")
        return None

# ======================================
# 🖼️ SIDEBAR - CONTROLES E STATUS
# ======================================
with st.sidebar:
    st.header("🧠 Ciborna Enhanced HUD")
    
    st.markdown("### 🎛️ Controles da Simulação")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("▶️ Iniciar"):
            result = start_market_simulation()
            if result:
                st.success(result.get("message", "Iniciado"))
    
    with col2:
        if st.button("⏹️ Parar"):
            result = stop_market_simulation()
            if result:
                st.warning(result.get("message", "Parado"))
    
    st.markdown("### 📊 Status da API")
    status = get_market_status()
    if status:
        st.metric("🔄 Status", "🟢 Ativo" if status["is_running"] else "🔴 Inativo")
        st.metric("💰 Preço Atual", f"{status['current_price']:.5f}")
        st.metric("📈 Ticks Coletados", status["tick_count"])
        st.metric("📋 Entradas no Book", status["book_entries"])
    else:
        st.error("❌ API não disponível")
    
    st.markdown("---")
    st.markdown("### 🔄 Atualização Automática")
    auto_refresh = st.checkbox("Ativar atualização automática", value=True)
    if auto_refresh:
        st_autorefresh(interval=2000, key="main_refresh")  # 2 segundos

# ======================================
# 🌐 PAINEL PRINCIPAL
# ======================================
st.title("🚀 CIBORNA • Painel Neural Enhanced com API em Tempo Real")

# ======================================
# 📊 ABA: DADOS EM TEMPO REAL
# ======================================
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Book de Ofertas",
    "⚡ Dados de Tick",
    "🕯️ Gráfico de Candles",
    "🧠 Análise da Ciborna"
])

with tab1:
    st.header("📋 Book de Ofertas em Tempo Real")
    
    book_data = get_book_data()
    if book_data and book_data.get("book"):
        st.subheader(f"📊 {book_data['symbol']} - Book de Ofertas")
        
        # Separar ofertas de compra e venda
        buy_orders = [order for order in book_data["book"] if order["type"] == "BUY"]
        sell_orders = [order for order in book_data["book"] if order["type"] == "SELL"]
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🟢 Ofertas de Compra (BID)")
            if buy_orders:
                buy_df = pd.DataFrame(buy_orders)
                buy_df = buy_df.sort_values('price', ascending=False)
                st.dataframe(
                    buy_df.style.format({"price": "{:.5f}", "volume": "{:,}"}),
                    use_container_width=True
                )
        
        with col2:
            st.markdown("#### 🔴 Ofertas de Venda (ASK)")
            if sell_orders:
                sell_df = pd.DataFrame(sell_orders)
                sell_df = sell_df.sort_values('price', ascending=True)
                st.dataframe(
                    sell_df.style.format({"price": "{:.5f}", "volume": "{:,}"}),
                    use_container_width=True
                )
        
        # Visualização do spread
        if buy_orders and sell_orders:
            best_bid = max(buy_orders, key=lambda x: x['price'])['price']
            best_ask = min(sell_orders, key=lambda x: x['price'])['price']
            spread = best_ask - best_bid
            
            st.markdown("#### 📏 Spread Atual")
            col1, col2, col3 = st.columns(3)
            col1.metric("🟢 Melhor BID", f"{best_bid:.5f}")
            col2.metric("🔴 Melhor ASK", f"{best_ask:.5f}")
            col3.metric("📏 Spread", f"{spread:.5f}")
        
        st.caption(f"Última atualização: {book_data.get('timestamp', 'N/A')}")
    else:
        st.warning("⚠️ Dados do book não disponíveis. Verifique se a simulação está rodando.")

with tab2:
    st.header("⚡ Dados de Tick em Tempo Real")
    
    tick_data = get_tick_data()
    if tick_data and tick_data.get("latest_tick"):
        latest = tick_data["latest_tick"]
        
        st.subheader(f"📊 {tick_data['symbol']} - Último Tick")
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("💰 Preço", f"{latest['price']:.5f}")
        col2.metric("📊 Volume", f"{latest['volume']:,}")
        col3.metric("🟢 BID", f"{latest['bid']:.5f}")
        col4.metric("🔴 ASK", f"{latest['ask']:.5f}")
        
        # Histórico de ticks recentes
        if tick_data.get("recent_ticks"):
            st.subheader("📈 Histórico de Ticks Recentes")
            recent_df = pd.DataFrame(tick_data["recent_ticks"])
            recent_df['timestamp'] = pd.to_datetime(recent_df['timestamp'])
            
            # Gráfico de linha dos preços
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=recent_df['timestamp'],
                y=recent_df['price'],
                mode='lines+markers',
                name='Preço',
                line=dict(color='blue', width=2)
            ))
            fig.update_layout(
                title="Evolução do Preço (Últimos Ticks)",
                xaxis_title="Tempo",
                yaxis_title="Preço",
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Tabela de ticks
            st.dataframe(
                recent_df.style.format({
                    "price": "{:.5f}",
                    "volume": "{:,}",
                    "bid": "{:.5f}",
                    "ask": "{:.5f}"
                }),
                use_container_width=True
            )
        
        st.caption(f"Última atualização: {tick_data.get('timestamp', 'N/A')}")
    else:
        st.warning("⚠️ Dados de tick não disponíveis. Verifique se a simulação está rodando.")

with tab3:
    st.header("🕯️ Gráfico de Candles em Tempo Real")
    
    candles_data = get_candles_data()
    if candles_data and candles_data.get("candles"):
        st.subheader(f"📊 {candles_data['symbol']} - Candles ({candles_data.get('timeframe', '1m')})")
        
        candles_df = pd.DataFrame(candles_data["candles"])
        candles_df['timestamp'] = pd.to_datetime(candles_df['timestamp'])
        
        # Gráfico de candlesticks
        fig = go.Figure(data=go.Candlestick(
            x=candles_df['timestamp'],
            open=candles_df['open'],
            high=candles_df['high'],
            low=candles_df['low'],
            close=candles_df['close'],
            name="EURUSD"
        ))
        
        fig.update_layout(
            title="Gráfico de Candlesticks - EURUSD",
            xaxis_title="Tempo",
            yaxis_title="Preço",
            height=500,
            xaxis_rangeslider_visible=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Estatísticas dos candles
        if not candles_df.empty:
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("📈 Último Close", f"{candles_df['close'].iloc[-1]:.5f}")
            col2.metric("⬆️ Máxima", f"{candles_df['high'].max():.5f}")
            col3.metric("⬇️ Mínima", f"{candles_df['low'].min():.5f}")
            col4.metric("📊 Volume Total", f"{candles_df['volume'].sum():,.0f}")
        
        st.caption(f"Última atualização: {candles_data.get('timestamp', 'N/A')}")
    else:
        st.warning("⚠️ Dados de candles não disponíveis. Verifique se a simulação está rodando.")

with tab4:
    st.header("🧠 Análise Neural da Ciborna")
    
    # Combinar dados para análise
    status = get_market_status()
    tick_data = get_tick_data()
    book_data = get_book_data()
    
    if status and tick_data and book_data:
        st.subheader("🔍 O que a Ciborna Vê e Ouve")
        
        # Análise do mercado
        latest_tick = tick_data.get("latest_tick", {})
        current_price = latest_tick.get("price", 0)
        
        # Calcular spread do book
        buy_orders = [order for order in book_data.get("book", []) if order["type"] == "BUY"]
        sell_orders = [order for order in book_data.get("book", []) if order["type"] == "SELL"]
        
        if buy_orders and sell_orders:
            best_bid = max(buy_orders, key=lambda x: x['price'])['price']
            best_ask = min(sell_orders, key=lambda x: x['price'])['price']
            spread = best_ask - best_bid
            
            # Análise de liquidez
            total_bid_volume = sum(order['volume'] for order in buy_orders)
            total_ask_volume = sum(order['volume'] for order in sell_orders)
            
            st.markdown("#### 👁️ Percepção Visual da Ciborna")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**📊 Dados de Mercado:**")
                st.write(f"• Preço atual: {current_price:.5f}")
                st.write(f"• Spread: {spread:.5f} ({spread/current_price*10000:.1f} pips)")
                st.write(f"• Volume BID total: {total_bid_volume:,}")
                st.write(f"• Volume ASK total: {total_ask_volume:,}")
                
                # Análise de tendência (simulada)
                if len(tick_data.get("recent_ticks", [])) >= 5:
                    recent_prices = [t['price'] for t in tick_data["recent_ticks"][-5:]]
                    trend = "📈 Alta" if recent_prices[-1] > recent_prices[0] else "📉 Baixa"
                    st.write(f"• Tendência recente: {trend}")
            
            with col2:
                st.markdown("**🧠 Interpretação Neural:**")
                
                # Análise de liquidez
                liquidity_ratio = total_bid_volume / total_ask_volume if total_ask_volume > 0 else 1
                if liquidity_ratio > 1.2:
                    liquidity_analysis = "🟢 Pressão compradora forte"
                elif liquidity_ratio < 0.8:
                    liquidity_analysis = "🔴 Pressão vendedora forte"
                else:
                    liquidity_analysis = "🟡 Mercado equilibrado"
                
                st.write(f"• Liquidez: {liquidity_analysis}")
                
                # Análise de spread
                if spread < 0.0002:
                    spread_analysis = "🟢 Spread apertado - boa liquidez"
                elif spread > 0.0005:
                    spread_analysis = "🔴 Spread largo - baixa liquidez"
                else:
                    spread_analysis = "🟡 Spread normal"
                
                st.write(f"• Spread: {spread_analysis}")
                
                # Simulação de "decisão" da IA
                decision_score = random.uniform(-1, 1)
                if decision_score > 0.3:
                    decision = "🚀 Sinal de COMPRA"
                elif decision_score < -0.3:
                    decision = "📉 Sinal de VENDA"
                else:
                    decision = "⏸️ Aguardar"
                
                st.write(f"• Decisão IA: {decision}")
                st.write(f"• Score: {decision_score:.3f}")
            
            # Log de atividade da Ciborna
            st.markdown("#### 📝 Log de Atividade Neural")
            activity_log = [
                f"🕐 {datetime.now().strftime('%H:%M:%S')} - Analisando book de ofertas...",
                f"🕐 {datetime.now().strftime('%H:%M:%S')} - Spread detectado: {spread:.5f}",
                f"🕐 {datetime.now().strftime('%H:%M:%S')} - Liquidez: {liquidity_analysis}",
                f"🕐 {datetime.now().strftime('%H:%M:%S')} - Decisão: {decision}",
            ]
            
            for log_entry in activity_log:
                st.text(log_entry)
        
        else:
            st.warning("⚠️ Dados insuficientes para análise completa.")
    
    else:
        st.warning("⚠️ Dados não disponíveis para análise. Verifique se a API está rodando.")

# ======================================
# 🔒 RODAPÉ
# ======================================
st.markdown("---")
st.caption("🧠 Ciborna Enhanced • Painel Neural com API em Tempo Real • Versão 2.0")

