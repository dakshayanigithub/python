#write a python pr1ogram to print sum of odd numbers in a range
n=int(input())
m=int(input())
l=[i for i in range(n,m+1) if i%2!=0]
print(sum(l))
