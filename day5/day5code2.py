#write a python program to print Dict and map
n=int(input())
d={}
for i in range(n):
    k,v=map(str,input().split())
    d[k]=v
m=int(input("No of search items:"))
for i in range(m):
    s=input()
    if s in d:
        print(s,d[s])
    else:
        print("Not Found")

"""
n=int(input("Enter no of items:"))
d={}
for i in range(n):
    key=input("key:")
    value=input("value:")
    d[key]=value
def search_contact(i):
    if i in d:
        return(f"Name:{i},value:{d[i]}")
    else:
        return f"{i}"" not found in the phone book."
print(d)
search_key=input("Enter the name search: ")
result=search_contact(search_key)
print(result)
              """
