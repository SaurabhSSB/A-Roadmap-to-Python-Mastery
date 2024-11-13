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

for a,b in a.items():
    print(f"The way to print {a} along with the right {b} consistency is key.")
