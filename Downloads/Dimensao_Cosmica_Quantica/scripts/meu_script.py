# meu_script.py

def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo ao universo cósmico da programação. 🚀"

def somar(a, b):
    return a + b

if __name__ == "__main__":
    nome = input("Digite seu nome: ")
    print(saudacao(nome))

    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        resultado = somar(a, b)
        print(f"A soma de {a} e {b} é: {resultado}")
    except ValueError:
        print("❌ Por favor, digite números válidos.")
