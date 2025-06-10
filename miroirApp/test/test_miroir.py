import unittest
from app.miroir import miroir_mot, est_palindrome

class TestMiroir(unittest.TestCase):
    def test_miroir_mot(self):
        self.assertEqual(miroir_mot("bonjour"), "ruojnob")
        self.assertEqual(miroir_mot("monde"), "ednom")

    def test_est_palindrome(self):
        self.assertTrue(est_palindrome("kayak"))
        self.assertTrue(est_palindrome("deed"))
        self.assertFalse(est_palindrome("bonjour"))

if __name__ == '__main__':
    unittest.main()
