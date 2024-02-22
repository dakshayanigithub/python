#write a python program to print avg value in a matrix.
"""r=int(input("Rows: "))
c=int(input("columns: "))
t=[]
for i in range (r):
    t.append(tuple(map(int,input().split())))
#print(t)
t=[element for r in t for element in r]
avg_value=(sum(t)/len(t))
print (avg_value)"""

r=int(input("Rows: "))
c=int(input("columns: "))
l,sum=[],0
for i in range (r):
    l.append(tuple(map(int,input().split())))
for i in l:
    for j in i:
        sum+=j
print (sum/(r*c))

