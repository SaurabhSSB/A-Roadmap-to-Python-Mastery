def Increment(x):
    return(x+1)

a={12, 10, 11, 14, 19, 21, 42}
b=list(map(Increment, a))
print(b)