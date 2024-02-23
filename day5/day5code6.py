l,d=map(int,input().split())
lst=list(map(int,input().split()))
flag=0
for i in lst:
    for j in lst:
        if i-j==d:
            flag=1
x=True if flag==1 else False
print(x)

"""
l,d=map(int,input().split())
lst=list(map(int,input().split()))
flag=0
for i in lst:
    for j in lst:
        if i+j==d:
            flag=1
x=True if flag==1 else False
print(x)

l,d=map(int,input().split())
lst=list(map(int,input().split()))
flag=0
for i in lst:
    for j in lst:
        if i*j==d:
            flag=1
x=True if flag==1 else False
print(x)"""
