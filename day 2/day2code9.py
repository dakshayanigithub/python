#write a python program to print prime number ina range uusing functions
def prime_numbers(n,m):
    for i in range(n,m+1):#100-1001
        c=0
        for j in range (1,i+1):
            if i%j==0:
                c+=1
        if c == 2:
            print(i)
n=int(input())#100-1000
m=int(input())#100-1000
prime_numbers(n,m)
