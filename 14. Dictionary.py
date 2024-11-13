# Dictionary is an ordered collection of data that stores multiple values
# Key- Value Pair having , in between and enclosed in {}

a={
    "Ram": "Mediator",
    "Dhoni": "Marketing",
    "Shyam": "Client"
}

print(a["Dhoni"])
print(a.get("Ram"))# Does not give error in case of controversy
print(a.keys())
print(a.values())
print(a.items())
a.pop("Shyam")
a.popitem()
del a["Ram"]

for x,y in a.items():
    print(f"The way to print {x} along with the right {y} consistency is key.")

b={
    "Hari":"Task",
    "Mohan":"Analyst"
}
a.update(b)
print(a)
b.clear()
print(b)
del b