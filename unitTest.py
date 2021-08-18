import unittest
import calculations as prog

class test(unittest.TestCase):
    def test_total(self):
        result = prog.math.total(data1["Calories"])
        self.assertEqual(round(result, 2), 3637.2)

    def test_average(self):
        result = prog.math.average(data1["Calories"].mean())
        self.assertEqual(round(result, 2), 330.65)

if __name__ == "__main__":
    unittest.main()