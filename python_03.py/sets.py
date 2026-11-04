"""
Sets : is a collection of unordered items written in curly brackets { } 
Each element must be unique: repeated values are stored only once
Each element must be immutable (numbers, strings, tuples). Lists cannot bestored in a set.
Sets have no index, so nums[0] does not work.

"""


# Ex

nums = {1, 2, 3, 4}
set2 = {1, 2, 2, 2}         # repeated elements stored only once


print(nums)
print(set2)
print(len(set2))


# An empty set is created with set() . Writing {} creates an empty dictionary, not a set.

null_set = set()

print(type(null_set))           # type - set
print(type({}))                 # type - dict


# set methods


nums = {1, 2, 3}
 
nums.add(4)                    # Adds an element
nums.add(2)                    # already present: no change
print(nums)

nums.remove(3)                 # Removes the element (error if it is not in the set)
print(nums)
 
nums.clear()                   # Empties the set
print(nums)

nums = {1, 2, 3}

nums.pop()
print(nums)                    # Removes and returns a random value


set1 = {1, 2, 3}
set2 = {2, 3, 4}
 
print(set1.union(set2))           # Combines the values of both sets and returns a new set
print(set1.intersection(set2))    # Returns a new set with only the common values

