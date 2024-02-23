#write a pythton program to print average of each student marks given a student database using Neasted dictionary.
n=int(input("Enter no of students:"))
m=int(input("Enter no of students:"))
d={}
for i in range(n):
    k=input("Enter rollno: ")
    v={}
    for j in range(m):
        sub=input("Enter Subject name: ")
        marks=int(input("Enter marks: "))
        v[sub]=marks
    d[k]=v
for i in d:
    l=list(d[i].values())
    print(f"{i} : {sum(l)/m}")
