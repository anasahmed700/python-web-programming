# User input & output
name = input("Enter your name: ")
print("Hello, {name}!")

# variables
i = 23 # integer
print("i is", i)
f = 12.43 # float
print("f is", f)
b = True # boolean
print("b is", b)
n = None # none
print("n is", n)

# conditional
x = int(input("enter a number to find its sign: "))
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

# sequences 
name = "Ahmed" # string
coordinates = (10.0, 20.0) # tuple
names = ["Ali", "Umar", "Ahmed"] # list

# loops
print("\n----loops----")
for name in names:
    print(names.index(name), name)

# unique sets of data 
s = set()
s.add(1)
s.add(3)
s.add(5)
s.add(3) # won't be added
print(s)

# dictionary
ages = {"Anas": 25, "Ali": 20}
ages["Ahmed"] = 30 # adding data in dict
ages["Anas"] += 1 # updating
print(ages)