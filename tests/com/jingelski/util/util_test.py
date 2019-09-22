import unittest
from com.jingelski.util.util import round_half_up

class UtilTest(unittest.TestCase):
    def test_rounding(self):
        self.assertEqual(round_half_up(25.55, 1), 25.6)
        self.assertEqual(round_half_up(25.23, 1), 25.2)
        self.assertEqual(round_half_up(-5.55, 1), -5.5)


if __name__ == '__main__':
    unittest.main()
