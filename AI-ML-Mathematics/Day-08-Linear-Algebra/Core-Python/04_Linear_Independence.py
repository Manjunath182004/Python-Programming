def check_independence_2d(v1, v2):
    determinent = v1[0] * v2[1] - v1[1] * v2[0]

    if determinent != 0:
        return "Linearly Independent"
    else:
        return "Linearly dependent"

v1 = [1, 2]
v2 = [2, 4]    

print(check_independence_2d(v1, v2))    

v1 = [1, 0]
v2 = [0, 1]

print(check_independence_2d(v1, v2)) 