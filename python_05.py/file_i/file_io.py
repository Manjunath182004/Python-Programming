"""
File I/O in Python

Python can be used to perform operations on a file: reading data from it and
writing data to it.

Data in variables is lost when a program ends; files store it
permanently.

Types of files:
Text files: store plain text, like .txt , .log , .csv , .py .
Binary files: store data in binary form, like .mp4 , .mov , .png , .jpeg .

Note: a Word file ( .docx ) is actually stored as a binary file, even though it contains text.

"""

# Open, Read and Close a File
"""
f = open("file_name", "mode")
data = f.read()
f.close()

file Modes:

'r' Open for reading (default)
'w' Open for writing: erases the file first (creates it if missing)
'x' Create a new file and open it for writing (error if it already exists)
'a' Open for writing: adds to the end of the file (creates it if missing)
'b' Binary mode
't' Text mode (default)
'+' Open for updating (reading and writing)

Note: Modes can be combined: rb reads a binary file, r+ reads and writes.

"""

# Reading a File

f = open("sample.txt", "r")    #  If the text file is inside a DIFFERENT folder, you MUST use the full path
data = f.read()             
print(data)
f.close()


f = open("sample.txt", "r")
line1 = f.readline()
line2 = f.readline()

print(line1, end="")
print(line2, end="")


# writing to a file

f = open("demo.txt", "w")     # mode overwrites the entire file
f.write("This is a New File")
f.close()


f = open("demo.txt", "a")
f.write("\nthis line is added")
f.close()

f = open("demo.txt", "r")
print(f.read())
f.close()


# With Syntax 

# With with , Python closes the file automatically when the block ends, so we don't need f.close() .

with open("demo.txt", "r") as f:
    data = f.read()

print(data)    


with open("demo.txt", "w") as f:
    f.write("new data")

# Deleting a File

import os

os.remove("demo.txt")             # remove file name "demo.txt"