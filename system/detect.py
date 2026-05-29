import sys


os_name = sys.platform


def detection():
    if os_name.startswith("win") :
        headers = {"User-Agent": "Mozilla/5.0  (Windows NT 10.0; Win64; x64)"}
    else :
        headers = {"User-Agent": "Mozilla/5.0"}
    return headers