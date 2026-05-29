import sys

print("Détection du système d'exploitation...")
os_name = sys.platform


def detection():
    print(f"Système d'exploitation détecté : {os_name}.\nAttribution du User-Agent en conséquence...")
    if os_name.startswith("win") :
        headers = {"User-Agent": "Mozilla/5.0  (Windows NT 10.0; Win64; x64)"}
    else :
        headers = {"User-Agent": "Mozilla/5.0"}
    return headers
    print(f"User-Agent attribué : {headers['User-Agent']}")