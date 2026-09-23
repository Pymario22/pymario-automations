import os
import sys
import time
try:
    import psutil
except ImportError:
    print("❌ Errore: Questo script richiede la libreria 'psutil'.")
    print("Installala eseguendo nel terminale: pip install psutil")
    sys.exit(1)

def genera_barra(percentuale, lunghezza=20):
    """Crea una barra di progresso visiva [#####.....]"""
    blocchi_pieni = int(round(lunghezza * percentuale / 100))
    barra = "█" * blocchi_pieni + "-" * (lunghezza - blocchi_pieni)
    return f"[{barra}] {percentuale}%"

def monitora_risorse():
    try:
        while True:
            # Pulisce il terminale a ogni ciclo (funziona sia su Linux che Windows)
            os.system('clear' if os.name == 'posix' else 'cls')
            
            print("========================================")
            print("📊 PYMARIO SYSTEM MONITOR - LIVE STATUS ")
            print("========================================")
            
            # Recupero statistiche CPU e RAM
            cpu_uso = psutil.cpu_percent(interval=None)
            ram_info = psutil.virtual_memory()
            
            print(f"\n💻 Utilizzo CPU:")
            print(f"   {genera_barra(cpu_uso)}")
            
            print(f"\n🧠 Utilizzo RAM:")
            print(f"   {genera_barra(ram_info.percent)}")
            print(f"   Dettaglio: {ram_info.used // (1024**2)} MB / {ram_info.total // (1024**2)} MB")
            
            print("\n----------------------------------------")
            print("Premi CTRL+C per interrompere il monitoraggio.")
            
            time.sleep(2) # Aggiorna i dati ogni 2 secondi
            
    except KeyboardInterrupt:
        print("\n\n👋 Monitoraggio interrotto dallo sviluppatore. Status: Offline.")

if __name__ == "__main__":
    monitora_risorse()
