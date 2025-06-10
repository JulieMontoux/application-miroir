import unittest
from app.miroir import miroir_mot, est_palindrome, salutation, au_revoir

class TestMiroir(unittest.TestCase):
    def test_miroir_mot(self):
        self.assertEqual(miroir_mot("bonjour"), "ruojnob")
        self.assertEqual(miroir_mot("monde"), "ednom")

    def test_est_palindrome(self):
        self.assertTrue(est_palindrome("kayak"))
        self.assertTrue(est_palindrome("deed"))
        self.assertFalse(est_palindrome("bonjour"))

    def test_salutation_matin(self):
        self.assertIn(salutation(9), ["Bonjour"])

    def test_salutation_soir(self):
        self.assertIn(salutation(20), ["Bonsoir"])

    def test_au_revoir(self):
        self.assertIn(au_revoir(10), ["Au revoir, bonne journée !"])
        self.assertIn(au_revoir(21), ["Au revoir, bonne soirée !"])

if __name__ == '__main__':
    unittest.main()
