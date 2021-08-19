import unittest
import calculations as prog

class test(unittest.TestCase):
    def test_total(self):
        result = prog.math.total(1818.6)
        self.assertEqual(round(result, 2), 3637.2)

    def test_average(self):
        result = prog.math.average(330.65)
        self.assertEqual(round(result, 2), 330.65)

if __name__ == "__main__":
    unittest.main()