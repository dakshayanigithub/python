#write a python program to print sum of the given matrix.
"""r=int(input("Rows: "))
c=int(input("columns: "))
l=[]
for i in range (r):
    l.append(list(map(int,input().split())))
print(l)"""

r=int(input("Rows: "))
c=int(input("columns: "))
l=[]
for i in range (r):
    l.append(list(map(int,input().split())))
#print(l)
summ=0
for i in l:
    print(i)
    summ+=sum(i)
print(summ)
