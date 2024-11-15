a=[2,3,4]
b=int(input("Enter the number:-"))
if(b<0 or b>2):
    raise IndexError("Index not available")
print(5*a[b])
    