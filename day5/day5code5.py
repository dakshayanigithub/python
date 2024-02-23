d={}
for i in range(2):
    k,v=map(str,input().split())
    d[k]=v
print(d)
l=list(d.values())
if len(l[0]) == len(l[1]):
    if sorted(list(l[0])) == sorted(list(l[1])):
        print(True)
    else:
        print(False)
else:
        print(False) 
