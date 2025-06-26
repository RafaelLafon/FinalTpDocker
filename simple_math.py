import unittest
from simple_math import SimpleMath


class SimpleMath:
    @staticmethod
    def addition(a, b):
        return a + b

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(SimpleMath.addition(2, 3), 5)

if __name__ == "__main__":
    unittest.main()