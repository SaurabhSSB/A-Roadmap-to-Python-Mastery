# Built- In Module for time related operations
import time

def sum(x, y):
    print(x+ y)

def product(x, y):
    print(x*y)

t= time.time()
sum(10,11)
t2=time.time()- t
t1= time.time()
product(4,6)
print(t2)
print(time.time()-t1)

# lambda addition
a= time.time()
add= lambda x, y: x+ y
add(4,6)
a1=time.time()- t
print(a1)

print("Saurabh Singh Bhandari")
time.sleep(6)

print("Is a wonderful person.")
x= time.localtime()
f= time.strftime("%Y-%M-%D  %H:%M:%S", x)
print(f)