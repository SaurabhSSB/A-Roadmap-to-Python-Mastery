# Anything that is between single or double quotation marks is string. 
# It is basically a collection of Characters.

name = "Batman" # Batman is string
print("Hello "+name) # Hellow is string
b= "mohan's life is pretty lavish!!!"
d="PETROL136"
e=" Ranger "
print(b)

# Multi-line String 

a= """
An Apple a day keeps the doctor away 
But what if i am the doctor and 
i eat an Apple everyday,
Will i be seperated from myself?
Sounds interesting!
"""
print(a)

# length of String

x= len(a)
print('length of a is:- ',x)

# Accessing Specific Characters of String

print(name[3])

# Slicing
print(a[22:25])
print(a[:5])
print(a[-8:])
print(a[-14:148])
print(a.upper())
print(a.lower())
print(a.replace("Apple", "doctor"))
print(a.split(" "))
print(a.count("Apple"))
print(a.find("i"))
print(a.index("i")) # Raises error when the value is not found

print(b.rstrip("!"))
print(b.capitalize())
print(b.center(50,"."))
print(b.endswith("."))
print(b.islower())
print(b.istitle())
print(b.title())

print(d.isalnum())
print(d.isupper())

print(e.strip())

print(name.swapcase())
print(name.isalpha())