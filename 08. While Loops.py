# While Loops 

number= 5
while (number > 0):
  print(number)
  number= number - 1

# Else with While Loop

x =10
while (x > 2):
    print(x)
    x = x - 1
else:
    print('counter is 0')

# Do- While loop

while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break