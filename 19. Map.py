# Map- Value Takes Function

def Increment(x):
    return(x+1)

a=[12, 10, 11, 14, 19, 21, 42]
b=list(map(Increment, a))
print(b)

c=list(map(lambda x:x+1,a))
print(c)

# Filter- True or False Takes Predicate
d=list(filter(lambda x: x<21, c))
print(d)

# Reduce- Single Value Takes Function
from functools import reduce

x=[11, 34, 5, 27, 53, 22]
y=reduce( lambda x1, x2: x1+ x2, x)
print(y)