def is_on_x_axis(vector):
    return vector[1] == 0

v1 = [2, 0]
v2 = [3, 0]

zero = [0, 0]

addition = [
    v1[0] + v2[0],
    v1[1] + v2[1]
]

scalar = 3

mul = [
    scalar * v1[0],
    scalar * v1[1]
]

print("Contains zero:", is_on_x_axis(zero))
print("Addition result:", addition)
print("Addition remains in subset:", is_on_x_axis(addition))
print("Scalar result:", mul)
print("Scalar result remains in subset:", is_on_x_axis(mul))