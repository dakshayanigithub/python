#write a python program to print sum of the elements in last column.
r=int(input("Rows: "))
c=int(input("columns: "))
l,sum=[],0
for i in range (r):
    l.append(tuple(map(int,input().split())))
for i in l:
    sum+=i[c-1]
print(sum)


