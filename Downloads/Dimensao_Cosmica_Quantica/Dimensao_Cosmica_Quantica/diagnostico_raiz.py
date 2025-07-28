# diagnostico_raiz.py

import time

print("🧠 Iniciando diagnóstico da raiz Ciborna...\n")

try:
    from ciborna.core import StrategyEngine
    print("✅ StrategyEngine disponível")
except Exception as e:
    print("❌ Falha ao importar StrategyEngine:", e)

try:
    from ciborna.core import Executor
    Executor.test_run()
    print("✅ Executor funcional")
except Exception as e:
    print("❌ Executor quebrado:", e)

try:
    from ciborna.core import DataBridge
    dados = DataBridge.load_dummy_data()
    print("✅ DataBridge ok — dados carregados")
except Exception as e:
    print("❌ DataBridge falhou:", e)

try:
    from ciborna.core import RiskManager
    RiskManager.validate(dummy=True)
    print("✅ RiskManager estável")
except Exception as e:
    print("❌ RiskManager com erro:", e)

# ✨ Tempo total
time.sleep(1)
print("\n🏁 Diagnóstico concluído.")
