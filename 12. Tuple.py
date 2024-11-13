# Tuple is an ordered collection of data that stores mutiple values.
# Elements of Tuple are called Tuple Items and are seperated by commas and enclosed within ().
# Tuple is Immutable

x=(36)
a=(27,)
print(type(x))
print(type(a))
#a[0]=10 Tuples are Immutable
a=(14,35,64,27,54,74,27,52,43,27)
print(a[0],a.index(27))
z=a.index(27,4,8)
print(z)

# Type Casting
b=list(a)
print(type(b),b)

# Concatenation
d=(23,45,54,29,66)
z=a+d
print(z)

# Replication
e= d*2
print(e)

# Count
f=e.count(29)
print(f)
