# Create a new file "practice.txt" using Python and add the following data in it

"""
Hi everyone
we are learning File I/O
using Java.
I like programming in Java.

"""

with open("practice.txt", "w") as f:
    f.write("Hi Everyone\nwe are Learning File I/O\n")
    f.write("using Java.\nI Like Programming in Java.")


#  Write a function that replaces all occurrences of "java" with "python" in the above file.

def replace_java():
    with open("practice.txt", "r") as f:
        data = f.read()

    new_data = data.replace("Java", "Python")

    with open("practice.txt", "w") as f:
        f.write(new_data) 

replace_java() 

with open("practice.txt", "r") as f:                # You can open and see the Java word Replaces -> with python
    print(f.read())


# Search if the word "learning" exists in the file or not.

word = "learning"

with open("practice.txt", "r") as f:
    data = f.read()

if word in data:
    print("Found")
else:
    print("Not Found")



# Write a function to find in which line of the file the word "learning" occurs first. Print -1 if not found.
      
def check_line(word):
    line_no = 1
    with open("practice.txt", "r") as f:
        for line in f:    
            if word in line:                # reads one line at a time
                return line_no
            line_no += 1
    return -1

print(check_line("Learning"))   
print(check_line("hello"))


#  From a file containing numbers separated by commas, print the count of even numbers.

count = 0

with open("number.txt", "r") as f:
    data = f.read()

nums = data.split(",")       # list of strings
for num in nums:
    if int(num) % 2 == 0:
        count += 1


print("Even Numbers: ", count)
