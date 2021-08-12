import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
# Install 'python3 -m pip install --user xlrd'


data = pd.read_excel("dataNew.xls")
data['Period'] = data['Period'].str.replace('Jan', '')
data["Period"] = data["Period"].astype(int)
#data = data[(data["Period"] >= 1900) & (data["Period"] <= 1910)]
data = data.loc[(data.Period >= 1900) & (data.Period <= 1910)]
print("Total: ", data["Calories"].sum())
print("Mean: ", data["Calories"].mean())
ps = data['Calories']
index = data['Period']
plt.xlabel('Year', fontsize=5)
plt.ylabel('No. of Calories', fontsize=8)
plt.xticks(ps.index, index, fontsize=10, rotation=90)
plt.title('1900 - 1910')
plt.bar(ps.index, ps.values)
plt.show()


data = pd.read_excel("dataNew.xls")
data['Period'] = data['Period'].str.replace('Jan', '')
data["Period"] = data["Period"].astype(int)
data = data.loc[(data.Period > 1910) & (data.Period <= 1920)]
print("Total: ", data["Calories"].sum())
print("Mean: ", data["Calories"].mean())
ps = data['Calories']
index = data['Period']
plt.xlabel('Year', fontsize=5)
plt.ylabel('No. of Calories', fontsize=8)
plt.xticks(ps.index, index, fontsize=10, rotation=90)
plt.title('1911 - 1920')
plt.bar(ps.index, ps.values)
plt.show()


data = pd.read_excel("dataNew.xls")
data['Period'] = data['Period'].str.replace('Jan', '')
data["Period"] = data["Period"].astype(int)
# data["Period"].to_numeric()
data = data[(data["Period"] > 1920) & (data["Period"] <= 1930)]
print("Total: ", data["Calories"].sum())
print("Mean: ", data["Calories"].mean())
ps = data['Calories']
index = data['Period']
plt.xlabel('Year', fontsize=5)
plt.ylabel('No. of Calories', fontsize=8)
plt.xticks(ps.index, index, fontsize=10, rotation=90)
plt.title('1921 - 1930')
plt.bar(ps.index, ps.values)
plt.show()