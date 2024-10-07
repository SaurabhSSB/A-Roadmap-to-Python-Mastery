# Operators:- signs or keywords used to perform specific operation on multiple values or variables.
# Types of Operators:-
# Arithmetic Operators- +, -, *, /, **, //, %
# Comparison Operators- <, >, <=. >=, ==, !=
# Assignment Operators- =, +=, -=, *=, %=
# Logical Operators- AND, OR, NOT
# Bitwise Operators- &, |, <<, >>, -, ^

# Arithmetic Operators
a=3
b=4
c=6
print(a+b, " ", a-b, " ", a*b, " ", c/b, " ", b**a, " ", c//b, " ", c%b)

x= "Lord "
y= "Voldemort "

# Concatenation of Strings
z= x+y 
print(z)

# Replication of String
print(z*a) 

# Comparison Operators

print(a>b, " ", a<b, " ", a==b, " ", a!=b, " ", a>=b, " ", a<=b)

# Assignment Operators

d= 16
print(d)
a+= 3
print( a)
b-= 2
print( b)
c*= 2
print( c)
c%= 5
print( c)
a/=2
print( a)

# Logical Operators

if( a>1 and b==2):
    print(" And is working")

if( a>1 or b<2):
    print(" If is working")

if (not( a<1 and b>2)):
    print(" Not is working")

# Bitwise Operators

x = 5  # Binary: 0101
y = 3  # Binary: 0011
result = x & y  # Binary: 0001
print(result)  
x = 5  # Binary: 0101
y = 3  # Binary: 0011
result = x | y  # Binary: 0111
print(result)  
x = 5  # Binary: 0101
y = 3  # Binary: 0011
result = x ^ y  # Binary: 0110
print(result) 
x = 5  # Binary: 0101
result = ~x  # 2's complement
print(result)  
x = 5  # Binary: 0101
result = x << 2 
print(result) 
x = 5  # Binary: 0101
result = x >> 2  # Binary: 0001
print(result)