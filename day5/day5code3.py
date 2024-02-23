d={}
n,m=map(int,input().split())
for i in range(n):
    k,v=map(str,input().split())
    d[k]=v
for i in range(m):
    k1,v1=map(str,input().split())
    for i in d:
        if d[i]==v1[:-1]:
            print(f"{k1} {v1} #{i}")
