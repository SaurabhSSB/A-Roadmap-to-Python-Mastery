'''
Function:- A function is a block of code that performs a specific task whenever it is called.
Two Types :- 
Built-in Functions:- The functions that are pre-defined and pre-coded in python.
min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print().
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

'''
Default Argument:- We provide a default value while creating a function.
'''

def Add(a= 5, b= 7): 
  print("Sum is:- ",a+b)
Add()

'''
Keyword Arguemnts:- Arguments with key = value.
By this the interpreter recognizes the arguments by the parameter name.
So the order in which the arguments are passed is not relevant.
'''

def Multiplication(a, b, c):
    print("a= ", a, "b= ", b, "c= ", c)
    print("Product is ", a*b*c)
Multiplication(c= 12, b= 15, a= 11)

'''
 Variable-length arguments:- Used to pass more arguments than defined in the actual function.
'''
# Arbitrary Arguments

def name(*credit):
    print("Hi,\n", credit[0], credit[1], credit[2])
name("Roshan ", "Rihan ", "Reetha ")

# Keyword Arbitrary Arguments

def name(**debit):
    print("Hi,\n", debit["debitor1"], debit["debitor3"], debit["debitor3"])
name(debitor1 = "Yamla ", debitor2 = "Pagla ", debitor3 = "Deewana ")

'''
Required Arguments:- Conventionally, it is necessary to pass the arguments in the correct positional order 
and the number of arguments passed should match with arguments of function .
'''

def Student(Name, Class, Roll_No):
    print("Hello,\n", Name, Class, Roll_No)
Student(Name= "Hermione Granger", Class= "First-Year Magic Student ", Roll_No= 3)

# Return Statement 

''' 
2 Uses - 1. End the function, 2. Send Value Back to the program
'''

def Advice(a):
  return "Honesty is the best " + a + "!"

Saying = Advice("Policy")
print(Saying) 