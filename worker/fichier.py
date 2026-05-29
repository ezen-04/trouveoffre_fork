import pandas as pd
from tkinter.messagebox import Message
from core.auto_config import now_re


def alerte(un, deux):
    Message(f"Nombre d'offres trouvées : {len(un)}\nNouvelles offres enregistrées : {len(deux)}")

def excel(new):
    pd.set_option("display.max_colwidth", None)
    df = pd.DataFrame(new, columns=["Titre", "Lien"])
    df.to_excel(f"offres/offres_jobbot_{now_re}.xlsx", index=False)
    print(f"Fichier Excel créé avec succès dans le dossier offres: offres_jobbot_{now_re}.xlsx")