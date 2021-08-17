import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Install 'python3 -m pip install --user xlrd'

data = pd.read_excel("dataNew.xls")
data1 = data["Period"].str.split(" ", n = 1, expand = True)
newData = data.assign(Years = data1[1])
newData["Years"] = newData["Years"].astype(int)
"""
moveColumn = newData.pop("Years")
newData.insert(0, 'Years', moveColumn) """
del newData["Period"]
print(newData)

newData1 = newData.loc[(newData.Years >= 1900) & (newData.Years <= 1910)]
newData2 = newData.loc[(newData.Years >= 1911) & (newData.Years <= 1920)]
newData3 = newData.loc[(newData.Years >= 1921) & (newData.Years <= 1930)] 

def first():
    print("First:")
    print("Total: ", round(newData1["Calories"].sum(), 2))
    print("Mean: ", round(newData1["Calories"].mean(), 2))
    ps = newData1['Calories'].sort_values(ignore_index=True)
    index = newData1['Years']
    plt.xlabel('Year', fontsize=5)
    plt.ylabel('No. of Calories', fontsize=8)
    plt.xticks(ps.index, index, fontsize=10, rotation=90)
    plt.title('1900 - 1910')
    plt.bar(ps.index, ps.values)
    plt.savefig("1900 - 1910")
    plt.show()


def second():
    print("Second:")
    print("Total: ", round(newData2["Calories"].sum(), 2))
    print("Mean: ", round(newData2["Calories"].mean(), 2))
    ps = newData2['Calories'].sort_values(ignore_index=True)
    index = newData2['Years']
    plt.xlabel('Year', fontsize=5)
    plt.ylabel('No. of Calories', fontsize=8)
    plt.xticks(ps.index, index, fontsize=10, rotation=90)
    plt.title('1911 - 1920')
    plt.bar(ps.index, ps.values)
    plt.savefig("1911 - 1920")
    plt.show()


def third():
    print("Third:")
    print("Total: ", round(newData3["Calories"].sum(), 2))
    print("Mean: ", round(newData3["Calories"].mean(), 2))
    ps = newData3["Calories"].sort_values(ignore_index=True)
    index = newData3['Years']
    plt.xlabel('Year', fontsize=5)
    plt.ylabel('No. of Calories', fontsize=8)
    plt.xticks(ps.index, index, fontsize=10, rotation=90)
    plt.title('1921 - 1930')
    plt.bar(ps.index, ps.values)
    plt.savefig("1921 - 1930")
    plt.show()


first()
second()
third()
    