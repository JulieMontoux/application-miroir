import unittest
from unittest.mock import patch

from app.palindrome import OHCE

# Variables globales utilisées dans certains tests pour plus de fluidité
TEST_INPUTS = [
    ("chat", "fr", "Bonjour", "Au revoir", False),
    ("kayak", "fr", "Bonjour", "Au revoir", True),
    ("hello", "en", "Hello", "Goodbye", False),
    ("madam", "en", "Hello", "Goodbye", True),
]
class TestOHCE(unittest.TestCase):
    def test_says_hello_first(self):
        # Pour chaque mot
        for mot, lang, expected_hello, expected_bye, is_pal  in TEST_INPUTS:
            with self.subTest(mot=mot):
                # Étant donné une instance de OHCE
                ohce = OHCE(language=lang)

                # Quand on saisit le mot
                result = ohce.palindrome(mot)

                # Alors la réponse commence par "Bonjour"
                self.assertTrue(result.startswith(expected_hello), f"Échec pour mot: {mot}")

    def test_response_ends_with_goodbye(self):
        # Pour chaque mot
        for mot, lang, expected_hello, expected_bye, is_pal in TEST_INPUTS:
            with self.subTest(mot=mot):
                # Étant donné une instance de OHCE
                ohce = OHCE(language=lang)

                # Quand on saisit un mot
                result = ohce.palindrome(mot)

                # Alors la réponse se termine par "Au revoir"
                self.assertTrue(result.strip().endswith(expected_bye), f"Échec pour mot: {mot}")

    def test_returns_input_reversed(self):
        for mot, lang, *_ in TEST_INPUTS:
            with self.subTest(mot=mot, lang=lang):
                # Étant donné une instance de OHCE
                ohce = OHCE(language=lang)
                # Quand on saisit le mot
                result = ohce.palindrome(mot)
                # Alors la réponse est son inverse
                self.assertIn(mot[::-1], result)

    def test_detects_palindrome(self):
        # Étant donné une instance de OHCE
        ohce = OHCE(language="fr")
        # Quand on saisit un palindrome comme "kayak"
        result = ohce.palindrome("kayak")
        # Alors la réponse contient "Bien dit !" et que kayak est inversé
        self.assertIn("kayak\n"+ohce.messages["well_said"], result)

    def test_bien_dit_not_present_if_not_palindrome(self):
        # Étant donné une instance de OHCE
        ohce = OHCE(language='fr')
        # Quand on saisit une chaîne non palindrome
        result = ohce.palindrome("bonjour")
        # Alors la réponse ne contient pas "Bien dit !"
        self.assertNotIn(ohce.messages["well_said"], result)

    def test_bien_dit_localized(self):
        for mot, lang, _, _, is_pal in TEST_INPUTS:
            if is_pal:
                with self.subTest(mot=mot, lang=lang):
                    ohce = OHCE(language=lang)
                    result = ohce.palindrome(mot)
                    self.assertIn(ohce.messages["well_said"], result)

    @patch.object(OHCE, 'is_palindrome')
    def test_bien_dit_is_not_checked_as_palindrome(self, mock_is_palindrome):
        # Étant donné une instance de OHCE
        ohce = OHCE()
        # Quand on saisit "! tid neiB" (qui retourne "Bien dit !" mais n'est pas un palindrome)
        result = ohce.palindrome("! tid neiB")
        # Alors "Bien dit !" ne doit pas apparaître du tout
        mock_is_palindrome.assert_called_once_with("! tid neiB")

if __name__ == '__main__':
    unittest.main()
