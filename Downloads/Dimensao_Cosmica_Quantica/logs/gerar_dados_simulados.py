import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Definir número de linhas para os dados simulados
num_linhas = 100

# Gerar dados simulados
data = {
    'Asset': np.random.choice(['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'NVDA', 'META', 'NFLX'], num_linhas),
    'ADX': np.random.randint(10, 60, num_linhas),
    'SERMEDIA': np.random.choice(['Alta', 'Neutro', 'Baixa'], num_linhas),
    'Preco_Fechamento': np.round(np.random.uniform(100, 1000, num_linhas), 2),
    'Volume': np.random.randint(100000, 5000000, num_linhas),
    'RSI': np.random.randint(20, 80, num_linhas),
    'MACD': np.round(np.random.uniform(-10, 10, num_linhas), 2)
}

df_simulado = pd.DataFrame(data)

# Adicionar dados para o gráfico de candles
start_date = datetime(2024, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(num_linhas)]

df_simulado['Date'] = dates
df_simulado['Open'] = df_simulado['Preco_Fechamento'] * (1 + np.random.uniform(-0.02, 0.02, num_linhas))
df_simulado['High'] = df_simulado[['Open', 'Preco_Fechamento']].max(axis=1) * (1 + np.random.uniform(0, 0.03, num_linhas))
df_simulado['Low'] = df_simulado[['Open', 'Preco_Fechamento']].min(axis=1) * (1 - np.random.uniform(0, 0.03, num_linhas))
df_simulado['Close'] = df_simulado['Preco_Fechamento']

# Reordenar colunas para melhor visualização
df_simulado = df_simulado[['Date', 'Asset', 'Open', 'High', 'Low', 'Close', 'Volume', 'ADX', 'SERMEDIA', 'Preco_Fechamento', 'RSI', 'MACD']]

# Salvar para CSV
df_simulado.to_csv('ativos_simulados.csv', sep=';', index=False)

print('Arquivo ativos_simulados.csv gerado com sucesso com dados de candles!')

