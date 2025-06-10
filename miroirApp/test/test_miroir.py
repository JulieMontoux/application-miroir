import unittest
from app.miroir import miroir_mot

class TestMiroir(unittest.TestCase):
    def test_miroir_mot(self):
        self.assertEqual(miroir_mot("bonjour"), "ruojnob")
        self.assertEqual(miroir_mot("monde"), "ednom")
if __name__ == '__main__':
    unittest.main()
