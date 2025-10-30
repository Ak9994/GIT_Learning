#initialize numbers
no = int(input("enter range:"))
temp = 0
#find prime numbers
for i in range(int(no)):
  if (n%i == 0):
    print(f"{i} is a prime no")
  else:
    i = i+1
