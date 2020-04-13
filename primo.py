num = (input("Please enter a number: "))
while True:
     try:
         number = int(num)
         break
     except ValueError:
        print("Input it's not an integer number, try again")
        num = (input("Please enter a number: "))
number = int(num)
bool = True
def VerifyPrimeNumber(number):
  if number > 1:
    for x in range(2, number):
        if (number % x) == 0:
          return (not bool)
    else:
      return bool
  else:
    (not bool)
if (VerifyPrimeNumber(number)):
  print (number, "It's a prime number")
else: 
  print (number, "It´s not a prime number")
