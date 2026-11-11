# Scalars & Vectors

# in python 

# scalar values 

distance = 10
speed = 60
temperature = 30
age = 25

print("Distance: ", distance)
print("speed: " , speed)
print("temperature: ",  temperature)
print("ditance: " , distance)

print(type(distance))
print(type(speed))

# Using NumPy - we will see basic Things of NumPy here While practicing problems and we enter detail in NumPy section

import numpy as np

distance = np.array(10)    # creates single dimesnsional array or scalar array
speed = np.array(60)

print(distance)
print(speed)

print("distance dimesnsion: ", distance.ndim)
print("speed dimesnsion: ", speed.ndim)


# Vector

"""
have both direction and maganitude

Ex: np.array(10) - Scalar 

    np.array([10, 20, 30])  - 1D vector
    np.array([[1, 2], [3, 4]]) - 2D vector
    np.array([[[1], [2]], [[3], [4]]])  - 3D vector

"""

# vector represented using list

vector = [3, 4]

print("vector:", vector)
print("X component: ", vector[0])
print("Y component: ", vector[1])
print("Number of Components: ", len(vector))


# In NumPy

vector = np.array([3, 4])

print("Vector:", vector)
print("Dimensions:", vector.ndim)
print("Shape:", vector.shape)
print("Size:", vector.size)
print("Data type:", vector.dtype)
