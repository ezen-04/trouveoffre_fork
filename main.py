from db.session import filter_new_jobs, close
from worker.scraper import scraping
from worker.fichier import alerte, excel


# Démarrage du bot & tri des nouvelles offres
print("Démarrage du bot de recherche d'offres d'emploi...")
all_jobs = scraping()
print("Recherche terminée. Filtrage des nouvelles offres...")
new_jobs = filter_new_jobs(all_jobs)
print("Filtrage terminé. Fermeture de la connexion à la base de données...")
close()
print("Connexion à la base de données fermée.")


# Affichage du nombre d'offres trouvées et de nouvelles offres enregistrées
print("Nombre d'offres trouvées :", len(all_jobs))
print("Nouvelles offres enregistrées :", len(new_jobs))
print("Envoi des alertes et génération du fichier Excel...")
alerte(all_jobs, new_jobs)


# Génération du fichier Excel
excel(new_jobs)
print("Processus terminé.")