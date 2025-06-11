import unittest
from app.palindrome import OHCE

class TestOHCE(unittest.TestCase):
    def test_dit_bonjour_en_premier(self):
        # Étant donné une instance de OHCE
        ohce = OHCE()
        # Quand on saisit une chaîne quelconque
        result = ohce.Palindrome("chat")
        # Alors la réponse commence par "Bonjour"
        self.assertTrue(result.startswith("Bonjour"))

    def test_returns_input_reversed(self):
        # Étant donné une instance de OHCE
        ohce = OHCE()
        # Quand on saisit "chat"
        result = ohce.Palindrome("chat")
        # Alors la réponse contient "tahc"
        self.assertIn("tahc", result)

if __name__ == '__main__':
    unittest.main()
