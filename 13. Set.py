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

