"""
Dictionaries Store Data In Key:Value pairs , Inside Curly Brackets {}

Dictionaries are Mutable
No duplicate keys 
Values can be of any type: string, number, list, even another dictionary.

"""

# EX:

info = {
    "name" : "Manjunath",
    "age"  : 23,
    "marks" : [98, 97, 95]

}

print(info["name"])
print(info["age"])
print(info["marks"])


# Use dict["key"] = value to change an existing value or add a new pair

info = {
    "name" : "Manju",
    "cgpa" : 9.8
}

info["cgpa"] = 9.6                 # changes the value
info["city"] = "Bangalore"         # adds a new key
print(info)


# Nested Dictionaries

student = {
    "name" : "Manju",
    "score" : {
        "phy" : 89,
        "chem" : 90,
        "Bio" : 99,
        "Math" : 100
    }
}

print(student["score"])
print(student["score"]["Math"])



# Dictionary Methods

info = {
    "name" : "Manjunath",
    "age"  : 23,
    "marks" : [98, 97, 95]

}

print(info.keys())                 # Returns all keys

print(info.values())               # Returns all values

print(info.items())                # Returns all (key, value) pairs as tuples

print(list(info.keys()))             # convert to a normal list

print(info.get("name"))            # Returns the value for the key

print(info.get("id"))              # key missing: returns None

# print(student["id"])             # key missing: KeyError


info.update({"city": "Bangalore", "age":24, "name": "Abhi"})
print(info)