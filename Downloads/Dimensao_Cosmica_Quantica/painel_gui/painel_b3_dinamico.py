import tkinter as tk
from tkinter import ttk
import painel_ciborna_integrado  # Certifique-se que este módulo está no mesmo diretório ou no PYTHONPATH

# 🪐 Janela principal
janela = tk.Tk()
janela.title("Painel Interativo de Ativos B3")
janela.geometry("400x230")

# 🧠 Lista de ativos com ícones e categorias
lista_ativos = [
    "📈 AÇÃO - COGN3", "📈 AÇÃO - YDUQ3", "📈 AÇÃO - ASAI3",
    "📈 AÇÃO - CVCB3", "📈 AÇÃO - DIRR3", "📈 AÇÃO - LREN3",
    "📈 AÇÃO - TIMS3", "📈 AÇÃO - CYRE3", "📈 AÇÃO - TOTS3",
    "📈 AÇÃO - BPAC11",
    "🌀 FUTURO - WIN", "🌀 FUTURO - WDO",
    "💰 CRIPTO - BIT"
]

# 🔄 Variável para armazenar o ativo escolhido
ativo_atual = tk.StringVar()
ativo_atual.set(lista_ativos[0])

# 🎯 Função para atualizar o ativo escolhido + integrar com sistema externo
def trocar_ativo():
    selecionado = combobox.get()
    ativo_atual.set(selecionado)
    
    # 💬 Atualiza a interface
    label_resultado.config(text=f"✅ Ativo selecionado: {selecionado}")
    
    # 🧠 Remove o prefixo para enviar apenas o código puro (ex: COGN3)
    codigo_puro = selecionado.split(" - ")[-1]

    # 🔗 Integração com o sistema principal
    painel_ciborna_integrado.set_ativo(codigo_puro)

# 🧩 Elementos da interface
tk.Label(janela, text="Selecione um ativo ou índice da B3:", font=("Segoe UI", 10)).pack(pady=8)

combobox = ttk.Combobox(janela, values=lista_ativos, state="readonly", font=("Segoe UI", 10))
combobox.set(lista_ativos[0])
combobox.pack()

tk.Button(janela, text="Confirmar", command=trocar_ativo).pack(pady=10)

label_resultado = tk.Label(janela, text="", fg="darkblue", font=("Segoe UI", 10, "bold"))
label_resultado.pack()

# 🚀 Inicia o painel
janela.mainloop()
