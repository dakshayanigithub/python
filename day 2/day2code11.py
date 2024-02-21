def strong_number(n,m):
    for i in range(n,m+1):
        x,sum=i,0
        while i> 0:
            digit=i%10
            fact=1
            for j in range(1,digit+1):
               fact*=j
            sum+=fact
            i//=10
        if sum == x:
            print(x)
n=int(input())
m=int(input())
strong_number(n,m)
