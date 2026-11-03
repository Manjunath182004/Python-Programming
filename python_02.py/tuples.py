"""
tuples - stores the collection of values in ()

A tuples can store elemnets of differents types(int, float, str..etc)

tuples are immutable 


"""

tup = (87, 64, 33, 95, 76)

print(tup[0])
print(tup[1:3])
print(len(tup))


tup1 = ()                             # empty tuple
tup2 = (1,)                           # single element: the comma is required
tup3 = (1, 2, 3)

print(type(tup2))
print(type((1)))                      # without comma, it is just an int



# tuples methods

tup = (2, 1, 3, 1)

print(tup.index(1))                    # Returns the index of the first occurrence

print(tup.count(1))                    # Counts the total occurrences