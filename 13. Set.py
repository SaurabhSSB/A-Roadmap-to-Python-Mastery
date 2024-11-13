# Set is an unordered collection of data, it stored multiple entries in a single variable.
# Seperated by Commas and enclosed within {}
# Sets are immutable. 
# Sets do not contain Duplicate Items.

a=set()
b={2,3,4,5,2,"Tenacious",True,2.0}
print(type(a))
print(b)

for i in b:
    print(i,end=",")
print("end")

if 2 in b:
    print(f"Yes {2*1} is present in b")
else:
    print(f"No {2*1} is not present in b")
    
# Manipulation

a1= {23, 22, 45, 56}
a2= {1, 2, 3, 4, 5, 6}
a1.update(a2)
a1.difference_update(a2)
a3=a1.difference(a2)
print(a3)
print(a1)
print(a1.union(a2),a1.intersection(a2))
a1.update(a2)
a3= a1.symmetric_difference(a2)
a1.intersection_update(a2)
print(a1)
print(a3)

'''
union()
update()
intersection
intersectin_update()
symmetric_difference
symmetric_difference_update()
difference()
difference_update()
'''

# IN- Built Methods
print(a1.isdisjoint(a3))
print(a1.isdisjoint(a2))
print(a1.issuperset(a2))
print(a1.issubset(a2))

a1.add(11)
a1.remove(3)
a1.discard(21)# No Error
print(a1)
a10= a1.pop()
print(a10)
del a10
a3.clear()
print(a3)