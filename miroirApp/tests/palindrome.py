import unittest
from unittest.mock import patch

from app.palindrome import OHCE

class TestOHCE(unittest.TestCase):
    def test_says_hello_first(self):
        # Étant donné une instance de OHCE
        ohce = OHCE()
        # Quand on saisit une chaîne quelconque
        result = ohce.palindrome("chat")
        # Alors la réponse commence par "Bonjour"
        self.assertTrue(result.startswith("Bonjour"))

    def test_response_ends_with_goodbye(self):
        # Étant donné une instance de OHCE
        ohce = OHCE()
        # Quand on saisit "chat"
        result = ohce.palindrome("chat")
        # Alors la réponse se termine par "Au revoir"
        self.assertTrue(result.strip().endswith("Au revoir"))

    def test_returns_input_reversed(self):
        # Étant donné une instance de OHCE
        ohce = OHCE()
        # Quand on saisit "chat"
        result = ohce.palindrome("chat")
        # Alors la réponse contient "tahc"
        self.assertIn("tahc", result)

    def test_detects_palindrome(self):
        # Étant donné une instance de OHCE
        ohce = OHCE()
        # Quand on saisit un palindrome comme "kayak"
        result = ohce.palindrome("kayak")
        # Alors la réponse contient "Bien dit !"
        self.assertIn("Bien dit !", result)

    def test_bien_dit_not_present_if_not_palindrome(self):
        # Étant donné une instance de OHCE
        ohce = OHCE()
        # Quand on saisit une chaîne non palindrome
        result = ohce.palindrome("bonjour")
        # Alors la réponse ne contient pas "Bien dit !"
        self.assertNotIn("Bien dit !", result)

    def test_exact_reversed_value_is_correct(self):
        # Étant donné une instance de OHCE
        ohce = OHCE()
        # Quand on saisit "kayak"
        result = ohce.palindrome("kayak")
        # Alors la chaîne retournée contient bien "kayak" inversé
        self.assertIn("kayak", result)

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
