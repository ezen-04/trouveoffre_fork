from db.session import filter_new_jobs
from worker.scraper import scraping
from worker.fichier import alerte, excel


all_jobs = scraping()
new_jobs = filter_new_jobs(all_jobs)


print("Nombre d'offres trouvées :", len(all_jobs))
print("Nouvelles offres enregistrées :", len(new_jobs))


alerte(all_jobs, new_jobs)
excel(new_jobs)