#check the number is prime or not
n=int(input("Enter a number"))
c=0
for i in range(2,n):
    if n%i==0:
         print("Not a prime")
         break
else
