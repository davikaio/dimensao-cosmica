import time
import datetime

def buscar_instancias_ioc():
    # Mock: Retorna instâncias simuladas de IOC para teste
    instancias = [
        {"id": 101, "tipo": "IOC", "valor": 120.0},
        {"id": 102, "tipo": "IOC", "valor": 145.5}
    ]
    print("🟡 Verificando instâncias IOC...")
    return instancias if datetime.datetime.now().second % 2 == 0 else []

def log_mensagem(msg):
    with open("log_execucao.txt", "a", encoding="utf-8") as log:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] {msg}\n")

def executar_monitoramento():
    while True:
        iocs = buscar_instancias_ioc()
        if iocs:
            for i in iocs:
                msg = f"Ordem IOC encontrada: ID {i['id']}, Valor {i['valor']}"
                print(msg)
                log_mensagem(msg)
        else:
            print("Nenhuma instância IOC encontrada.")
            log_mensagem("Nenhuma instância IOC encontrada.")
        time.sleep(10)  # Espera 10 segundos antes da próxima verificação

if __name__ == "__main__":
    executar_monitoramento()