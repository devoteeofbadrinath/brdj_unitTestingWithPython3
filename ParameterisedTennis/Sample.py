import unittest

class TestExample(unittest.TestCase):
    def test_multiple(self):
        for a, b, expected in [(1, 2, 3), (2, 2, 5), (3, 3, 6)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(a + b, expected)

if __name__ == "__main__":
    unittest.main()
