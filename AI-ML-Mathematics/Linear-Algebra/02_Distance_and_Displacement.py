
# Distance = Total path travelled.
# Displacement = Straight-line change from starting point to ending point.

"""
Suppose a person:
1. Travels 10 km north.
2. Travels 20 km east.
3. Travels 5 km south.

then Total Distance and Displacement

"""

# Try To Slove Every Problem in your Own then apply to proogram

import math

movements = [10, 20, 5]

total_sitance = sum(movements)

x = 20      # 20 km East
y = 10 - 5   # 10 km North ,  5 km South

displacement = math.sqrt(x**2 + y**2)

print("Total distance: ", total_sitance, "Km")
print("Displacement components [X, Y]: ", [x, y])
print("Displacement Maganitude: ", round(displacement, 2), "km")


# using numpy

import numpy as np

displacement = np.array([20, 5])

magnitude = np.linalg.norm(displacement)

print("Displacement: ", displacement)
print("Maganitude: ", magnitude)



# Some More Example

movements = [

    np.array([10, 0]),  # 10 km east
    np.array([-4, 0]),  # 4 km west
    np.array([0, 6]),   # 6 km north
    np.array([0, -2])   # 2 km south 
]

total_sitance = sum(np.linalg.norm(move) for move in movements)

final_displacements = np.sum(movements, axis=0)

print("Total distance:", total_sitance)
print("Final displacement:", final_displacements)
print("Displacement magnitude:", np.linalg.norm(final_displacements))