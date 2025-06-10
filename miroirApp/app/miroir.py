from datetime import datetime

def miroir_mot(mot: str) -> str:
    return mot[::-1]

def est_palindrome(mot: str) -> bool:
    return mot == mot[::-1]