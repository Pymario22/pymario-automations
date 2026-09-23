# pymario-automations
## 🛠️ Requisiti e Installazione

Lo script `monitor_sistema.py` richiede la libreria di terze parti **`psutil`** per poter interrogare le risorse hardware (CPU, RAM) di Manjaro Linux o di qualsiasi altro sistema operativo.

Segui uno dei metodi indicati di seguito per configurare correttamente l'ambiente.

### Metodo 1: Tramite Ambiente Virtuale (Consigliato su Manjaro)
Su Manjaro Linux e altre distribuzioni basate su Arch, è consigliato utilizzare un ambiente virtuale (`venv`) per non interferire con i pacchetti Python globali del sistema operativo:

1. Apri il terminale nella cartella del progetto e crea l'ambiente:
   ```bash
   python -m venv .venv
   ```
2. Attiva l'ambiente virtuale:
   ```bash
   source .venv/bin/activate
   ```
3. Installa `psutil` tramite `pip`:
   ```bash
   pip install psutil
   ```

*(Nota: Ricordati di attivare l'ambiente virtuale con il comando `source` ogni volta che riapri il terminale per l'esecuzione).*

---

### Metodo 2: Tramite il Gestore Pacchetti di Manjaro (Pacman)
Se preferisci installare la libreria a livello globale su Manjaro senza usare gli ambienti virtuali, puoi sfruttare i repository ufficiali della tua distribuzione Linux tramite `pacman`:

```bash
sudo pacman -Syu python-psutil
```

---

### Metodo 3: Installazione Standard (Altri Sistemi/Windows)
Se stai eseguendo il progetto su un sistema che permette l'installazione globale diretta tramite `pip`:

```bash
pip install -r requirements.txt
```
*Oppure installando singolarmente il pacchetto:*
```bash
pip install psutil
```

---

## 🚀 Come Eseguire lo Script

Una volta completata l'installazione delle dipendenze, avvia il monitor di sistema con il comando:

```bash
python monitor_sistema.py
```
*Per interrompere il monitoraggio in tempo reale e chiudere lo script, premi la combinazione di tasti **`CTRL + C`** all'interno del terminale.*
