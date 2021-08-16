import unittest
from unittest import result
import matplotlib.pyplot as plt
import pandas as pd
import calculations as prog


data = pd.read_excel("dataNew.xls")
data1 = data["Period"].str.split(" ", n = 1, expand = True)
newData = data.assign(Years= data1[1])
newData["Years"] = newData["Years"].astype(int)
data1 = newData.loc[(newData["Years"] >= 1900 ) & (newData["Years"] <= 1910)]

class test(unittest.TestCase):
    def test_total(self):
        result = prog.math.total(data1["Calories"])
        self.assertEqual(round(result, 2), 3637.2)

    def test_average(self):
        result = prog.math.average(data1["Calories"].mean())
        self.assertEqual(round(result, 2), 330.65)

if __name__ == "__main__":
    unittest.main()