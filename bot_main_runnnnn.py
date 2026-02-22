import subprocess
import sys
import time

print("🚀 Iniciando bot...")

while True:
    try:
        process = subprocess.run([sys.executable, "main.py"])
    except KeyboardInterrupt:
        print("⏹ Bot encerrado.")
        break
    except Exception as e:
        print(f"❌ Erro: {e}")

    print("🔁 Reiniciando em 5 segundos...")
    time.sleep(5)
