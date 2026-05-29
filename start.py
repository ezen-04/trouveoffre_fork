import os
import subprocess
import sys
from pathlib import Path
from core.config import venv_name

# Configuration
venv_path = Path(venv_name)
requirements_file = Path("requirements.txt")
main_file = Path("main.py")

def run_command(cmd, check=True):
    try:
        result = subprocess.run(cmd, shell=True, check=check, text=True, capture_output=True)
        if result.stdout:
            print(result.stdout.strip())
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erreur : {e.stderr.strip()}")
        return False

def main():
    print("=== Configuration et lancement du projet ===\n")

    # Creationn du venv s'il n'existe pas encore
    if not venv_path.exists():
        print(f"Création de l'environnement virtuel '{venv_name}'...")
        try:
            subprocess.run([sys.executable, "-m", "venv", venv_name], check=True)
            print("Environnement virtuel créé avec succès !")
        except Exception as e:
            print(f"Erreur de création du venv : {e}")
            sys.exit(1)
    else:
        print(f"Environnement virtuel '{venv_name}' déjà existant.")
    
    # Définir les chemins selon l'OS
    if os.name == "nt" :  # Windows
        python_venv = venv_path / "Scripts" / "python.exe"
        activate_cmd = f"{venv_name}\\Scripts\\pip.exe"
    else: # Linux / macOS
        python_venv = venv_path / "bin" / "python"
        activate_cmd = f"source {venv_name}/bin/activate"
    
    # Installation des dépendances
    if requirements_file.exists():
        print("Installation des dépendances...")
        try:
            subprocess.run([str(python_venv), "-m", "pip", "install", "--upgrade", "pip"], check=True)
            subprocess.run([str(python_venv), "-m", "pip", "install", "-r", str(requirements_file)], check=True)
            print("Dépences installées avec succès !")
        except Exception as e:
            print(f"Erreur lors de l'installation : {e}")
            sys.exit(1)
    else :
        print("requirements.txt non trouvé (installation ignorée)")

    # Lancement de main.py avec le python du venv
    if main_file.exists():
        print(f"Lancement de {main_file}...")
        print(f"Activation du venv et exécution du main.py")
        try:
            subprocess.run([str(python_venv), str(main_file)], check=True)
        except Exception as e:
            print(f"Erreur lors de l'exécution de main.py : {e}")
            sys.exit(1)

    else:
        print(f"Fichier {main_file} non trouvé !")
    
    print("Script terminé !")

if __name__ == "__main__" :
    main()