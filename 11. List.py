# List is an ordered collection of data that stores mutiple values.
# Elements of List are called List Items and are seperated by commas and enclosed within [].
# List is Mutable

a=["Tungsten",53,True]
print(a)
print(type(a))
print(a[1])
print(a[-1])

if 't' in a[0]:
    print("Present")
else:
    print("Absent")

for i in a[0:3:2]:
    print(i,end='.')

j=2
x=[i+j for i in range(6) if i<5]
print(x)
print(2*2)

# List Manipulation
a=x.copy()
a.append(15)
a[1]=18
a.insert(0,127)
a.reverse()
a.sort(reverse= True)
print(a[4])
print(a.index(15))
print(a.count(29))
z=[57,24]
a.extend(z)
print(a)

# Concatenation
y=a+x
print(y)

#Replication
print(z*2)
