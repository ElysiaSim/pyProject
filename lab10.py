import pandas as pd
import numpy as np
import pandas as pd

ps1 = pd.Series([1,3,5,7,9])

ps2 = pd.Series([2,4,6,8,10])
ps = ps1 + ps2
ps = ps2 - ps1
ps = ps2 * ps1
ps = ps2 / ps1

print(ps2 == ps1)
print(ps2 > ps1)
print(ps2 < ps1)

dict = {'a': 10, 'b': 20, 'c':30, 'd':40, 'e':50}
psd = pd.Series(dict)
print(psd)

np_array = np.array([10,20,30,40,50])
print(np_array)
ps_numArray = pd.Series(np_array)
print(ps_numArray)

s1 = pd.Series([10, '20', 'python', '40', '50'])
print(s1)

s2 = pd.to_numeric(s1, errors='coerce')
print(s2)

s2 = s2.append(pd.Series([60,70]))
print(s2)

sorted_s2 = s2.sort_values()
print(sorted_s2)

sorted_s2.index = [1,2,3,4,5,6,7]
print(sorted_s2)

print("%.2f" % sorted_s2.mean())

print("%.2f" % sorted_s2.median())

print("%.2f" % sorted_s2.std())

var1 = s2.values.tolist()
print(var1)
type(var1)

npArray = np.array(var1)
print(npArray)
type(npArray)

colorlist = pd.Series([
    ['Red', 'Blue', 'Yellow'],
    ['Red', 'White'],
    ['Black']])
print(colorlist)

s = colorlist.apply(pd.Series).stack().reset_index(drop=True)
print(s)

list = [1,2,3,4,5]
df = pd.DataFrame(list)
print(df)

listOflist = [['Mike',5],['Peter',10],['Thomas',15]]
df = pd.DataFrame(listOflist,columns=['Name','Age'])
print(df)

dict = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "captial": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Bloemfontein"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}
brics = pd.DataFrame(dict)
print(brics)

brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

# import the cars.csv data: cars
cars = pd.read_csv('mtcars.csv')
# print out the cars
print(cars)

cars.head()
print(cars.head())

cars.tail()
print(cars.tail())

cars.columns
print(cars.columns)

print(cars.index)

car = cars['model'].str.split(' ', n = 1, expand = True)
print(car.head())

cars = cars.assign(car_brand=car[0])
cars = cars.assign(car_model=car[1])
cars[cars['car_brand'] == 'Mazda']
print(cars[cars['car_brand'] == 'Mazda'])


cars.index = cars['model']
del cars['model']
print(cars.index)

cars.iloc[:,:6].describe()
print(cars.iloc[:,:6].describe())

print(cars.head(10))

print(cars.mean())

import matplotlib.pyplot as plt
plt.scatter(cars['mpg'], cars['hp'])
plt.show()

ax = cars[['car_model', 'hp']].plot(kind='bar', title="Horse Power Comparison", figsize=(10,10), legend=True, fontsize=12)
plt.show()

ax = cars['hp'].plot(kind='hist', title="Range in HP", figsize=(10,10), legend=True, fontsize=12)
plt.show()

my_fig = ax.get_figure()
my_fig.savefig("Cars_Range_HP.png")

ps = cars['mpg'].sort_values()
index = np.arange(len(ps.index))
plt.xlabel('Models', fontsize=5)
plt.ylabel('Miles per gallon', fontsize=10)
plt.xticks(index, ps.index, fontsize=10, rotation=90)
plt.title('Miles per gallon of Cars')
plt.bar(ps.index, ps.values)
plt.show()

from scipy.stats import linregress
stats = linregress(cars['mpg'], cars['hp'])
m = stats.slope
b = stats.intercept
# Change the default figure size
plt.figure(figsize=(5,5))
plt.scatter(cars['mpg'], cars['hp'])
# Set the linewidth on the regression line to 3px and line color to red
plt.plot(cars['mpg'], m * cars['mpg'] + b, color="red", linewidth=3)
plt.show()