import unittest
from unittest.mock import patch

from app.palindrome import OHCE
from tests.builder import OHCEBuilder

# Variables globales utilisées dans certains tests pour plus de fluidité
TEST_INPUTS = [
    # format : (mot, langue, heure simulée, hello attendu, goodbye attendu, est_palindrome)
    ("chat", "fr", 9, "Bonjour", "Au revoir, bonne journée !", False),
    ("kayak", "fr", 9, "Bonjour", "Au revoir, bonne journée !", True),
    ("chat", "fr", 20, "Bonsoir", "Bonne soirée, à bientôt !", False),
    ("kayak", "fr", 20, "Bonsoir", "Bonne soirée, à bientôt !", True),
    ("hello", "en", 9, "Good morning", "Goodbye, have a nice day!", False),
    ("madam", "en", 9, "Good morning", "Goodbye, have a nice day!", True),
    ("hello", "en", 20, "Good evening", "Good night, see you soon!", False),
    ("madam", "en", 20, "Good evening", "Good night, see you soon!", True),
]

PERIOD_INPUTS = [
    (6,"en" ,"matin", "Good morning", "Goodbye, have a nice day!"),
    (13,"en" , "après-midi", "Good afternoon", "Goodbye, enjoy your afternoon!"),
    (19, "en" ,"soirée", "Good evening", "Good night, see you soon!"),
    (23,"en" , "nuit", "Good night", "Goodbye, sleep well!"),
    (6, "fr" ,"matin", "Bonjour", "Au revoir, bonne journée !"),
    (13,"fr" , "après-midi", "Bonjour", "Au revoir, bonne fin d'après-midi !"),
    (19, "fr" ,"soirée", "Bonsoir", "Bonne soirée, à bientôt !"),
    (23,"fr" , "nuit", "Bonsoir", "Bonne nuit !"),
]

class TestOHCE(unittest.TestCase):
    def test_says_hello_first(self):
        # Pour chaque mot
        for mot, lang, heure, hello_expected, _, _ in TEST_INPUTS:
            with self.subTest(mot=mot, lang=lang, heure=heure):
                # Étant donné une instance de OHCE
                ohce = OHCEBuilder().with_langue(lang).with_heure(heure).build()
                # Quand on saisit le mot
                result = ohce.palindrome(mot)
                # Alors la réponse commence par "Bonjour"
                self.assertTrue(result.startswith(hello_expected))

    def test_response_ends_with_goodbye(self):
        # Pour chaque mot
        for mot, lang, heure, _, goodbye_expected, _ in TEST_INPUTS:
            with self.subTest(mot=mot, lang=lang, heure=heure):
                # Étant donné une instance de OHCE
                ohce = OHCEBuilder().with_langue(lang).with_heure(heure).build()
                # Quand on saisit un mot
                result = ohce.palindrome(mot)
                # Alors la réponse se termine par "Au revoir"
                self.assertTrue(result.strip().endswith(goodbye_expected))

    def test_returns_input_reversed(self):
        for mot, lang, heure, *_ in TEST_INPUTS:
            with self.subTest(mot=mot, lang=lang, heure=heure):
                # Étant donné une instance de OHCE
                ohce = OHCEBuilder().with_langue(lang).with_heure(heure).build()
                # Quand on saisit le mot
                result = ohce.palindrome(mot)
                # Alors la réponse est son inverse
                self.assertIn(mot[::-1], result)

    def test_detects_palindrome(self):
        # Étant donné une instance de OHCE
        ohce = OHCEBuilder().with_langue("fr").with_heure(10).build()
        # Quand on saisit un palindrome comme "kayak"
        result = ohce.palindrome("kayak")
        # Alors la réponse contient "Bien dit !" et que kayak est inversé
        self.assertIn("kayak\n" + ohce.messages["well_said"], result)

    def test_bien_dit_not_present_if_not_palindrome(self):
        # Étant donné une instance de OHCE
        ohce = OHCEBuilder().with_langue("fr").with_heure(10).build()
        # Quand on saisit une chaîne non palindrome
        result = ohce.palindrome("bonjour")
        # Alors la réponse ne contient pas "Bien dit !"
        self.assertNotIn(ohce.messages["well_said"], result)

    def test_bien_dit_localized(self):
        # Pour chaque mot
        for mot, lang, heure, _, _, is_pal in TEST_INPUTS:
            # Si c'est un palindrome
            if is_pal:
                with self.subTest(mot=mot, lang=lang, heure=heure):
                    # Étant donné une instance de OHCE
                    ohce = OHCEBuilder().with_langue(lang).with_heure(heure).build()
                    # Quand on saisit une chaîne
                    result = ohce.palindrome(mot)
                    # Alors la réponse contient "Bien dit !"
                    self.assertIn(mot + "\n" + ohce.messages["well_said"], result)

    @patch.object(OHCE, 'is_palindrome')
    def test_bien_dit_is_not_checked_as_palindrome(self, mock_is_palindrome):
        # Étant donné une instance de OHCE
        ohce = OHCEBuilder().build()
        with patch.object(OHCE, 'is_palindrome') as mock_is_palindrome:
            # Quand on saisit "! tid neiB" (qui retourne "Bien dit !" mais n'est pas un palindrome)
            ohce.palindrome("! tid neiB")
            # Alors "Bien dit !" ne doit pas apparaître du tout
            mock_is_palindrome.assert_called_once_with("! tid neiB")

    @patch.object(OHCE, 'get_hour', return_value=9)
    def test_says_bonjour_morning(self, mock_hour):
        ohce = OHCEBuilder().with_langue("fr").with_heure(9).build()
        result = ohce.palindrome("kayak")
        self.assertTrue(result.startswith("Bonjour"))

    @patch.object(OHCE, 'get_hour', return_value=20)
    def test_says_bonsoir_evening(self, mock_hour):
        ohce = OHCEBuilder().with_langue("fr").with_heure(20).build()
        result = ohce.palindrome("kayak")
        self.assertTrue(result.startswith("Bonsoir"))

    def test_palindrome_renvoie_bien_dit_dans_la_bonne_langue(self):
        # ÉTANT DONNÉ un utilisateur parlant le français
        ohce = OHCEBuilder().with_langue("fr").with_heure(10).build()
        # QUAND on entre un palindrome
        result = ohce.palindrome("kayak")
        # ALORS il est renvoyé
        self.assertIn("kayak", result)
        # ET le "Bien dit !" de cette langue est envoyé
        self.assertIn("Bien dit !", result)

    def test_salutation_dans_la_bonne_langue_en_premier(self):
        # ÉTANT DONNÉ un utilisateur parlant anglais
        ohce = OHCEBuilder().with_langue("en").with_heure(9).build()
        # QUAND on entre "madam"
        result = ohce.palindrome("madam")
        # ALORS <hello> de cette langue est envoyé avant tout
        self.assertTrue(result.startswith("Good morning"))

    def test_au_revoir_envoye_en_dernier_selon_langue(self):
        # ÉTANT DONNÉ un utilisateur parlant le français
        ohce = OHCEBuilder().with_langue("fr").with_heure(21).build()
        # QUAND on entre "chat"
        result = ohce.palindrome("chat")
        # ALORS <auRevoir> est envoyé en dernier
        self.assertTrue(result.strip().endswith("Bonne soirée, à bientôt !"))

    def test_salutation_selon_periode_et_langue(self):
        for heure,lang, periode, salutation_attendue, _ in PERIOD_INPUTS:
            with self.subTest(periode=periode, langue=lang):
                # ÉTANT DONNÉ un utilisateur parlant anglais
                # ET que la période de la journée est <période>
                ohce = OHCEBuilder().with_langue(lang).with_heure(heure).build()
                # QUAND on saisit un palindrome
                result = ohce.palindrome("madam")
                # ALORS <salutation> de cette langue à cette période est envoyé avant tout
                self.assertTrue(result.startswith(salutation_attendue))

    def test_au_revoir_selon_periode(self):
        for heure,lang, periode, _, au_revoir_attendu in PERIOD_INPUTS:
            with self.subTest(periode=periode, langue=lang):
                # ÉTANT DONNÉ un utilisateur parlant anglais
                # ET que la période de la journée est <période>
                ohce = OHCEBuilder().with_langue(lang).with_heure(heure).build()
                # QUAND on saisit une chaîne
                result = ohce.palindrome("hello")
                # ALORS <auRevoir> dans cette langue à cette période est envoyé en dernier
                self.assertTrue(result.strip().endswith(au_revoir_attendu))


if __name__ == '__main__':
    unittest.main()
