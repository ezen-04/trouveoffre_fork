# Importation des dépendances
import sqlite3
from core.config import DB_URL
from core.auto_config import now


# Connexion à la base de données
conn = sqlite3.connect(DB_URL)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS jobs (title TEXT, link TEXT UNIQUE, date TEXT)''')


# Filtrer les offres et retourner uniquement celles qui sont nouvelles
def filter_new_jobs(jobs):
    new_jobs = []
    for title, link in jobs:
        try:
            c.execute("INSERT INTO jobs (title, link, date) VALUES (?, ?, ?)", (title, link, str(now)))
            new_jobs.append((title, link))
        except sqlite3.IntegrityError:
            continue
    conn.commit()
    return new_jobs


# Fermeture de la connexion à la base de données
conn.close()