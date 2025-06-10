from datetime import datetime

def miroir_mot(mot: str) -> str:
    return mot[::-1]

def est_palindrome(mot: str) -> bool:
    return mot == mot[::-1]

def salutation(heure=None) -> str:
    heure = heure if heure is not None else datetime.now().hour
    return "Bonjour" if 5 <= heure < 17 else "Bonsoir"

def au_revoir(heure=None) -> str:
    heure = heure if heure is not None else datetime.now().hour
    return "Au revoir, bonne journée !" if 5 <= heure < 17 else "Au revoir, bonne soirée !"
