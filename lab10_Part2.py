import numpy as np
import pandas as pd
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