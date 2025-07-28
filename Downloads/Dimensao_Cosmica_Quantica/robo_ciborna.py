import re

def iniciar(ultimo, hora, volume):
    try:
        numero_preco = re.search(r"\d+[\.,]?\d*", str(ultimo))
        valor = float(numero_preco.group(0).replace(",", "."))

        numero_vol = re.search(r"\d+", str(volume))
        vol = int(numero_vol.group(0))

        if vol > 1500 and valor > 4850:
            return "🧠 Entrada confirmada! O Ciborna recomenda ação imediata!"
        elif vol > 1000:
            return "📡 Volume crescente... Modo de observação ativado."
        else:
            return "🔎 Tudo tranquilo no replay. Aguardando sinais fortes."
    except Exception as e:
        return f"⚠️ Erro na análise: {e}"
