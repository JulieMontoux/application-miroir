from app.palindrome import OHCE
from unittest.mock import patch

class OHCEBuilder:
    def __init__(self):
        self.langue = "fr"
        self.heure = 9

    def with_langue(self, langue):
        self.langue = langue
        return self

    def with_heure(self, heure):
        self.heure = heure
        return self

    def build(self):
        ohce = OHCE(language=self.langue)
        # Patch de l'heure dans la méthode build()
        ohce.get_hour = lambda: self.heure
        return ohce
