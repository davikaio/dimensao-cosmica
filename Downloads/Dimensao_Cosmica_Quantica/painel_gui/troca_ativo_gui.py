import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Painel de Ativo")
janela.geometry("300x150")

# 🔹 Lista de ativos disponíveis
lista_ativos = ["eurusd", "wsoo25", "btcusdt", "nasdaq", "ethbrl"]

# Variável que exibe o ativo selecionado
ativo_atual = tk.StringVar()
ativo_atual.set(lista_ativos[0])  # Valor inicial

# Função para atualizar o ativo
def trocar_ativo():
    ativo_selecionado = combobox.get()
    ativo_atual.set(ativo_selecionado)
    label_resultado.config(text=f"Ativo atual: {ativo_selecionado}")

# Elementos da interface
tk.Label(janela, text="Selecione um ativo:").pack(pady=5)

# 🔄 Combobox com os ativos
combobox = ttk.Combobox(janela, values=lista_ativos, state="readonly")
combobox.set(lista_ativos[0])  # Inicialização
combobox.pack()

tk.Button(janela, text="Confirmar", command=trocar_ativo).pack(pady=5)

label_resultado = tk.Label(janela, text="", fg="blue")
label_resultado.pack()

janela.mainloop()
