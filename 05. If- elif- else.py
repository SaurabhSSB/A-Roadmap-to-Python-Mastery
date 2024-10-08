'''
An if-else loop is a conditional statement in programming that allows you to execute different code blocks based on 
whether a specified condition is true or false. It's a fundamental control flow structure that enables your program to
make decisions and perform actions accordingly.
'''

# If Loop

a= input("Enter name:- ")
b= "power"
if(type(a)== type(b)):
   print("String ")

# If- else Loop

a= int(input("Enter your age:- "))
if(a>18):
  print("You can Vote")
else:
  print("You cannot Vote")

# If- elif Loop

Selling_Price = int(input("Enter Selling Price of Your Product:- "))
Cost_Price = int(input("Enter Cost Price of Your Product:- "))
if (Selling_Price< Cost_Price):
    print("Profit ")
elif(Selling_Price== Cost_Price):
    print("Nothing Gained")
else:
    print("Loss")

# Nested If Loop

number = int(input("Enter any number:- "))
if (number < 0):
    print("Negative Number")
elif (number > 0):
    print("Positive Number")
    if (number <= 10):
        print("Number in range 1-10")
    elif (number > 10 and number <= 20):
        print("Number in range 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")