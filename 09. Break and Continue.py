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

