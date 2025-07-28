import pandas as pd
from datetime import datetime
import random

def iniciar_operador_fantasma(modelo=None, ativo="EURUSD", estrategia="Reversão", limite_lucro=0.5, intervalo_segundos=300):
    resultado = round(random.uniform(-1.0, 9.0), 2)
    preco = round(random.uniform(1.0, 1.5), 5)
    registro = {
        "Horário": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Símbolo": ativo,
        "Tipo": "SIMULADA",
        "Preço": preco,
        "Resultado": "FANTASMA CICLICA",
        "LucroEstimado": resultado,
        "Estratégia": estrategia
    }

    pd.DataFrame([registro]).to_csv("logs/execucoes_fantasmas.csv", mode="a", header=False, index=False)
    print(f"Fantasma registrada: {registro}")
