# Ne rien modifier ici, ce fichier est utilisé pour configurer automatiquement les paramètres du bot 
# en fonction de l'environnement d'exécution (Windows, Linux, etc.). Il détecte le système d'exploitation 
# et ajuste les configurations en conséquence.

from datetime import datetime
from system.detect import detection


now = datetime.now()
now_re = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
headers = detection()