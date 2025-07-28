import pandas as pd

# 🔢 Dados simulados baseados em ativos da B3
data = {
    'Asset': ['PETR4', 'VALE3', 'BBAS3', 'WEGE3', 'MGLU3', 'B3SA3'],
    'Empresa': ['Petrobras', 'Vale', 'Banco do Brasil', 'WEG', 'Magazine Luiza', 'B3'],
    'Ultimo_Preco_R$': [31.99, 57.42, 20.21, 38.01, 7.80, 13.39],
    'Variacao_%': ['+2,04%', '-0,14%', '+1,61%', '-8,01%', '+4,00%', '+2,45%'],
    'Volume_Negociado': [27418600, 17914800, 35932600, 31116000, 19534600, 20683700]
}

# 📦 Criar o DataFrame
df_b3 = pd.DataFrame(data)

# 💎 Formatando números com ponto separador de milhar e vírgula decimal
df_b3['Ultimo_Preco_R$'] = df_b3['Ultimo_Preco_R$'].apply(lambda x: f"{x:,.2f}".replace('.', '*').replace(',', '.').replace('*', ','))
df_b3['Volume_Negociado'] = df_b3['Volume_Negociado'].apply(lambda x: f"{x:,}".replace(',', '.'))

# 📝 Salvar como CSV
df_b3.to_csv("ativos_b3_formatado.csv", sep=';', index=False, encoding='utf-8')

print("✅ Arquivo ativos_b3_formatado.csv gerado com sucesso!")
