'''
General Syntax for Match- Case
match value:
    case pattern1:
        # Code to execute if value matches pattern1
    case pattern2:
        # Code to execute if value matches pattern2
    case _:
        # Code to execute if value doesn't match any previous patterns 

'''
x = int(input("Enter Number: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 8 if x % 2 == 0:
        print("x % 2 == 0 and case is 8")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    case _ if x!=90:
        print(x, "is not 90")
    case _ if x%3!=0:
        print(x, "is not 80")
    case _: # It is basically an else.
        print(x)
