import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
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


newData_sorted = newData.sort_values(by=["Calories"], ascending=True)
newData1 = newData.loc[(newData.Years >= 1900) & (newData.Years <= 1910)]
newData2 = newData.loc[(newData.Years >= 1911) & (newData.Years <= 1920)]
newData3 = newData.loc[(newData.Years >= 1921) & (newData.Years <= 1930)] 


def first():
    print("Total: ", newData1["Calories"].sum())
    print("Mean: ", newData1["Calories"].mean())
    newData_sorted = newData.sort_values(by="Calories", ascending=True)
    ps = newData1['Calories']
    index = newData1['Years']
    plt.xlabel('Year', fontsize=5)
    plt.ylabel('No. of Calories', fontsize=8)
    plt.xticks(newData_sorted.index, index, fontsize=10, rotation=90)
    plt.title('1900 - 1910')
    plt.bar(newData_sorted.index, newData_sorted.values)
    plt.savefig("1900 - 1910")
    plt.show()


def second():
    print("Total: ", newData2["Calories"].sum())
    print("Mean: ", newData2["Calories"].mean())
    ps = newData2['Calories']
    index = newData2['Years']
    plt.xlabel('Year', fontsize=5)
    plt.ylabel('No. of Calories', fontsize=8)
    plt.xticks(ps.index, index, fontsize=10, rotation=90)
    plt.title('1911 - 1920')
    plt.bar(ps.index, ps.values)
    plt.savefig("1911 - 1920")
    plt.show()


def third():
    print("Total: ", newData3["Calories"].sum())
    print("Mean: ", newData3["Calories"].mean())
    ps = newData3["Calories"]
    index = newData3['Years']
    plt.xlabel('Year', fontsize=5)
    plt.ylabel('No. of Calories', fontsize=8)
    plt.xticks(ps.index, index, fontsize=10, rotation=90)
    plt.title('1921 - 1930')
    plt.bar(ps.index, ps.values)
    plt.savefig("1921 - 1930")
    plt.show()


if __name__ == "__main__":
    first()
    second()
    third() 