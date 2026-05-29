import os
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from core.auto_config import now_re
from worker.scraper import LOCATION


def alerte(un, deux):
    print("Création de la fenêtre de base...")
    root = tk.Tk()
    root.withdraw()  # Masquer la fenêtre principale
    print("Envoi des alertes...")
    messagebox.showinfo("Information", f"Nombre d'offres trouvées : {len(un)}\nNouvelles offres enregistrées : {len(deux)}")

def excel(new):
    print("Création du fichier Excel...")
    pd.set_option("display.max_colwidth", None)
    df = pd.DataFrame(new, columns=["Titre", "Lien", "Localisation"])
    os.makedirs("offres", exist_ok=True)
    df.to_excel(f"offres/offres_jobbot_{now_re}.xlsx", index=False, engine='openpyxl')
    print(f"Fichier Excel créé avec succès dans le dossier offres: offres_jobbot_{now_re}.xlsx")