# Importation des dépendances
import sqlite3
from core.config import db_url
from core.auto_config import now
from worker.scraper import LOCATION


# Connexion à la base de données
print("Connexion à la base de données...")
conn = sqlite3.connect(db_url)
c = conn.cursor()
print("Connexion établie.\nCréation de la table 'jobs' si elle n'existe pas...")
c.execute('''CREATE TABLE IF NOT EXISTS jobs (title TEXT, link TEXT UNIQUE, date TEXT, Location TEXT)''')


# Filtrer les offres et retourner uniquement celles qui sont nouvelles
def filter_new_jobs(jobs):
    print("Lancement de la fonction de filtrage des nouvelles offres...")
    new_jobs = []
    for title, link, location in jobs:
        try:
            print(f"Vérification de l'offre : {title} - {link} - {location}")
            c.execute("INSERT INTO jobs (title, link, date, Location) VALUES (?, ?, ?, ?)", (title, link, str(now), location))
            new_jobs.append((title, link, location))
        except sqlite3.IntegrityError:
            print(f"Offre déjà enregistrée : {title} - {link} - {location}")
            continue
    print("Ajout des nouvelles offres à la base de données...")
    conn.commit()
    return new_jobs


def close():
    # Fermeture de la connexion à la base de données
    print("Lancement de la fonction de fermeture...")
    conn.close()