import numpy
import numpy as np
my_list = [1,2,3,4,5,6,7,8]
my_numpy_list = np.array(my_list)
print(my_numpy_list[ 2:6 ]) # returns from index 2 to 6 (exclusive)
print(my_numpy_list[ :6 ]) # returns everything from index 0 to 6 (exclusive)
print(my_numpy_list[ 5: ]) # returns everything from index 5 to end of list
print(my_numpy_list[ -1 ]) # returns the value 0

type(my_numpy_list)
numpy.ndarray

my_2d_list = [ [1,2,3], [4,5,6], [7,8,9]]
my_2d_numpy_list = np.array(my_2d_list)
print(my_2d_numpy_list)

my_list = np.arange(10) # generate 10 digits from index 0 to 10
print(my_list)

my_list = np.arange(5,10)
print(my_list)

my_even_list = np.arange(0,11,2) # last arguments steps size and here have all even numbers
print(my_even_list)

my_zeros = np.zeros(5) # a list of 5 zeros
print(my_zeros)
my_ones = np.ones (5) # a list of 5 ones
print(my_ones)

my_2d_list = np.zeros( (2,5) )
print(my_2d_list)
my_2d_list = np.ones( (2,5) )
print(my_2d_list)

my_random_list = np.random.rand(4)
print(my_random_list)
my_random_list = np.random.rand(2,3)
print(my_random_list)

my_1d_list = np.random.rand(25)
print(my_1d_list)
my_2d_list = my_1d_list.reshape(5,5)
print(my_2d_list)

my_list = np.random.rand(11)
print(my_list)
print(my_list * my_list)
print(my_list - my_list)
print(my_list + my_list)
print(my_list / my_list)

print(np.sqrt(my_list))
print(np.exp(my_list))
print(np.sin(my_list))
print(np.cos(my_list))
print(np.log(my_list))
print(np.sum(my_list))
print(np.std(my_list))