#write a python program to print amstrong number in a range using function
def amstrong(n,m):
    for i in range(n,m+1):
        sum=0
        x=i
        while i > 0:
            temp = i%10
            sum+=temp**3
            i//=10
        if sum == x:
            print(x)
n=int(input("Enter a number"))
m=int(input("Enter a number"))
amstrong(n,m)
