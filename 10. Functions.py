'''
Function:- A function is a block of code that performs a specific task whenever it is called.
Two Types :- 
Built-in Functions:- The functions that are pre-defined and pre-coded in python.
User Definded Functions:- The functions we create to perform specific tasks as per our needs.
Calling a function:- We call a function by the function name, followed by parameters (if any) inside the parenthesis.
'''
def Out():
  print("No Parameters Required")

def Add(a, b): # Here a and b are Parameters and Arguments are passed to these Parameters
  Sum = (a+b)
  print(Sum)

def Bigger(a, b):
  if(a>b):
    print("First Number is Bigger")
  else:
    print("Second number is Bigger")

def Small(a, b):
  if(a>b):
    print("Second Number is Smaller")
  else:
    print("First Number is Smaller")
  

a= 12
b= 89
Out()
Bigger(a, b)
Add(a, b)
c= 82
d= 7
Small(c, d)
Add(c, d)

'''
Arguments in Python are of four Types:
Default Arguments
Keyword Arguments
Variable Length Arguments
Required Arguments
'''
