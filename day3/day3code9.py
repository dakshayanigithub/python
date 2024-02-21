#write a python program to print the factorial of given number
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
result=int(input())
print("factorial is",fact(result))
