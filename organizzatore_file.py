import os
import shutil
from pathlib import Path

def organizza_cartella(percorso_target):
    print(f"🔧 Avvio automazione su: {percorso_target}")
    path = Path(percorso_target)
    
    if not path.exists():
        print("❌ Il percorso specificato non esiste.")
        return

    # Definizione delle cartelle di destinazione in base alle estensioni
    CATEGORIE = {
        "Documenti": [".pdf", ".docx", ".txt", ".xlsx", ".md"],
        "Immagini": [".png", ".jpg", ".jpeg", ".gif", ".svg"],
        "Video_e_Audio": [".mp4", ".mkv", ".mp3", ".wav"],
        "Codice_Sorgente": [".py", ".html", ".css", ".js", ".sh"],
        "Archivi": [".zip", ".tar", ".gz", ".rar"]
    }

    file_spostati = 0

    # Iterazione sui file della cartella
    for file in path.iterdir():
        if file.is_file():
            # Cerca la categoria corrispondente all'estensione del file
            for categoria, estensioni in CATEGORIE.items():
                if file.suffix.lower() in estensioni:
                    # Crea la cartella se non esiste
                    cartella_dest = path / categoria
                    cartella_dest.mkdir(exist_ok=True)
                    
                    # Sposta il file
                    shutil.move(str(file), str(cartella_dest / file.name))
                    print(f"🚚 Spostato: {file.name} ➡️ {categoria}/")
                    file_spostati += 1
                    break
                    
    print(f"✅ Automazione completata. File organizzati: {file_spostati}\n")

if __name__ == "__main__":
    # Puoi cambiare questo percorso con la cartella che desideri ordinare su Manjaro
    # Esempio: os.path.expanduser("~/Scaricati") o os.path.expanduser("~/Scrivania")
    percorso_da_ordinare = os.path.expanduser("~/Scrivania")
    organizza_cartella(percorso_da_ordinare)
