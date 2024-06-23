def factorial(n):#function creation
 if n == 1:
   return n
 else:
   return n*factorial(n-1) #recursive technique
num=int(input("enter the number: "))#assigning runtime value
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num==0:
   print("The factorial of 0 is 1")
elif num > 0:
   print("The factorial of ",num," is ", factorial(num))
   #print("The factorial of ", 5, " is ", 120)
