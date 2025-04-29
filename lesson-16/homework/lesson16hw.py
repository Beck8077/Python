import numpy as np

# 1. Convert List to 1D Array

def numpy_converter(lst):
    arr = np.array(lst)
    return arr

print(numpy_converter([12.23, 13.32, 100, 36.32]))

# 2. Create 3x3 Matrix (2?10)

def numpy_matrix(n):
    arr = np.arange(2, n)
    return arr.reshape(3, 3)

print(numpy_matrix(11))

# 3. Null Vector (10) & Update Sixth Value

lst = np.zeros(10)
lst[6] = 11

print(lst)

# 4. Array from 12 to 38

lst_array = np.arange(12, 38)

print(lst_array)

# 5. Convert Array to Float Type

def numpy_float(lst):
    arr = np.array(lst)
    return arr.astype(float)

print(numpy_float([1, 2, 3, 4]))


# 6. Celsius to Fahrenheit Conversion

def numpy_degrees(lst):
    arr = np.array(lst)
    celcius = (arr - 32) / 1.8
    return celcius

print(numpy_degrees([0, 12, 45.21, 34, 99.91]))

# 7. Append Values to Array (Do self-tudy)

lst = [10, 20, 30]
arr = np.array(lst)
arr = np.append(arr, np.arange(40, 100, 10))
print(arr)

# 8. Array Statistical Functions (Do self-tudy)

arr = np.random.randint(1,50,(10))
arr_mean = np.mean(arr)
arr_median = np.median(arr)
arr_std = np.std(arr)
print(arr_mean)
print(arr_median)
print(arr_std)

# 9 Find min and max

arr = np.random.randint(1, 200, (10,10))
arr_max = np.max(arr)
arr_min = np.min(arr)

print(arr)
print(arr_max)
print(arr_min)


# 10 Create a 3x3x3 array with random values.

arr = np.random.randint(1, 50, (3,3,3))

print(arr)