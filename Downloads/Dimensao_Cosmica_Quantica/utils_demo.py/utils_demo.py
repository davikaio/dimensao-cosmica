"""
DEMO: Demonstração de uso dos utilitários da pasta /utils
"""

import pandas as pd
from utils.manipulador_arquivos import ler_csv, salvar_csv
from utils.normalizador_dados import preencher_nulos, padronizar_colunas_minusculas
from utils.validador_dados import check_colunas
from utils.validador_tipos import validar_tipos
from utils.diagnostico_dataset import resumo_estatistico, relatorio_nulos
from utils.log_neural import log_evento

# Exemplo de DataFrame inicial
df = pd.DataFrame({
    "Preco": [10.0, None, 30.5],
    "Volume": [100, 150, 200]
})

log_evento("Iniciando demonstração de uso dos módulos utils")

# Padronizar colunas
df = padronizar_colunas_minusculas(df)
log_evento("Colunas padronizadas")

# Preencher valores nulos
df = preencher_nulos(df, valor=0)
log_evento("Valores nulos preenchidos")

# Verificar integridade estrutural
check_colunas(df)

# Validar tipos
tipos = {"preco": float, "volume": int}
validar_tipos(df, tipos)

# Diagnósticos
resumo_estatistico(df)
relatorio_nulos(df)

# Salvar temporariamente
salvar_csv(df, "dados_processados.csv")
log_evento("DEMO concluída com sucesso")
