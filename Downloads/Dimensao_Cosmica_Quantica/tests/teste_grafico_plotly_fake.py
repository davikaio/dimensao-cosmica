import pandas as pd
import plotly.graph_objects as go

df = pd.DataFrame({
    "open": [10, 11, 12],
    "high": [12, 13, 14],
    "low": [9, 10, 11],
    "close": [11, 12, 13]
})

fig = go.Figure(data=[go.Candlestick(
    x=[1, 2, 3],
    open=df['open'],
    high=df['high'],
    low=df['low'],
    close=df['close']
)])

fig.update_layout(title="Gráfico Teste de Candlestick")
fig.show()
