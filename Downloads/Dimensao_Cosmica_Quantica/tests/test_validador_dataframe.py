import sys
import os
import pandas as pd
import pytest

# Garante que a pasta raiz esteja no sys.path para importar 'utils'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.validador_dados import verificar_dataframe_vazio


@pytest.mark.parametrize("input_df, esperado", [
    (None, "NULO"),
    (pd.DataFrame(), "VAZIO"),
    (pd.DataFrame({"a": [1, 2, 3]}), "OK")
])
def test_verificar_dataframe_vazio(input_df, esperado):
    resultado = verificar_dataframe_vazio(input_df)
    assert resultado == esperado, f"❌ Esperado '{esperado}', mas obtido '{resultado}'"
