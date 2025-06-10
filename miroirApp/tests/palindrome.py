import unittest
from app.palindrome import OHCE

class TestOHCE(unittest.TestCase):
    def test_dit_bonjour_en_premier(self):
        ohce = OHCE()
        result = ohce.Palindrome("chat")
        self.assertTrue(result.startswith("Bonjour"))  # add assertion here


if __name__ == '__main__':
    unittest.main()
