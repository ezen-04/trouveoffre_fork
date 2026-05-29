import requests
import time
from bs4 import BeautifulSoup
from core.config import config, links 
from core.auto_config import headers

# Critères de recherche
KEYWORDS = [k.lower() for k in config['keywords']]
LOCATION = config['location']
CONTRACTS = [c.lower() for c in config['contract_types']]


# Fonction pour vérifier les critères de mots-clés et types de contrat
def matches_criteria(text):
    text = text.lower()
    return any(k in text for k in KEYWORDS) and any(c in text for c in CONTRACTS)


# Bot : Fonction pour aller récupérer les offres sur chaque page
def scraping():
    jobs = []
    for link in links.keys:
        results = []
        taille = len(links[link])
        liste = links[link]
        for keyword in KEYWORDS:
            url = liste[0]+f"{keyword.replace(' ', '%20')}{liste[1]}{LOCATION}"
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            for a in soup.find_all("a", href=True):
                href = a['href']
                title = a.get_text(strip=True)
                if taille == 3 :
                    if href.startswith("/rc") and matches_criteria(title):
                        full_link = liste[2] + href
                        results.append((title, full_link))
                elif taille == 4 :
                    if liste[2] in href and matches_criteria(title):
                        full_link = href if href.startswith("http") else liste[3] + href
                        results.append((title, full_link))
                else :
                    print(f"Erreur: la recherche sur {link} n'a pas été bien fournie ! veuillez corriger les informations dans le fichier 'config'.")
            time.sleep(1)
        jobs += results
    return jobs
