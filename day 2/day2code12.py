#write a python program to remove duplicate in a given strings
s=input()
s1=""
for i in s:
    if i not in s1:
        s1+=i
print(s1)
