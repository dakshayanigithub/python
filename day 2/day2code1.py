n,x=map(int,input().split())
ns=n*x
#print(ns)
if ns%4==0:
    np=ns//4
else:
        np=(ns//4)+1
print(np)
