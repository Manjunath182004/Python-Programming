v1 = [1, 2]
v2 = [1, 2, 3]
v3 = [1, 2, 3, 4]

print("v1 Dimensions: ", len(v1))
print("v2 Dimensions: ", len(v2))
print("v3 Dimensions: ", len(v3))


# by creating function 

def same_dimension(v1, v2):
    return len(v1) == len(v2)

print(same_dimension([1, 2], [3, 4]))
print(same_dimension([1, 2], [3, 4, 5]))