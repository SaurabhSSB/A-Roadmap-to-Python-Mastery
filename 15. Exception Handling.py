a= input("Enter the number:- ")
print(f"The counting to {a} is:-")
try:
    for i in range(int(a)):
        print(i)
except Exception as a:
    print(a)

b= input("For Resetting:- ")
try:
    for i in range(5):
        print(int(b))
except:
    print("Wrong Input")
print("End of Code")

try:
    a=[2,3,4]
    b=int(input("Enter the number"))
    print(5*a[b])
except IndexError:
    print("Wrong Input")
except ValueError:
    print("Not an Integer")
finally:
    print("Terminate")