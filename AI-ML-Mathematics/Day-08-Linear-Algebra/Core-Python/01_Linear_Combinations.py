v1 = [1, 2]
v2 = [3, 1]

a = 2
b = 3

result = []

for i in range(len(v1)):
    result.append(a * v1[i] + b * v2[i])

print("Linear Combination:", result) 
