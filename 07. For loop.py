name = 'Saurabh'
for i in name:
    print(i, end=", ")

Directions= ["North ", "South", "East ", "West"]
for i in Directions:
    print("Direction", i, end= ",")

for x in range(5):
    print(x)

for k in range(2,8):
    print(k)

for i in range(5):
    print("Cool")
else:
    print("Warm")

# Enumerate 

a=[10,22,3,45,56,27.11]
for a,b in enumerate(a, start= -1):
    print(b)
    if(a==3):
        print("Enumerated Successfully")
