 #write a python program to remove duplicates
l=list(map(int,input().split()))
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)
