# Break

for i in range(1,10,1):
    print(i ,end=" ")
    if(i==5):
        break
    else:
        print("Keep Moving")
print("Understood Break ")

i = 0
while True:
  print(i)
  i = i + 1
  if(i%10 == 0):
    break

# Continue

for i in [2,3,4,6,8,12]:
    if (i%2!=0):
        continue
    print(i)


def even_odd(number):
    if number%2==0:
        return  f"{number} is even"
    else:
        return f"{number} is odd"
if __name__ == "__main__":
    try:
        user_input=input("enter a number")
        if user_input:
            user_input=int(user_input)
            result= even_odd(user_input)
            print(result)
        else:
            print("No inupt provided")
    except ValueError:
        print("Enter a valid integer")
    except EOFError:
        print("No input detected")
