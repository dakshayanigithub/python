#write a python to print the revers of the number using while loop
n=int(input())
rev = 0
while n > 0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)
