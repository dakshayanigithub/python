#write a python program to print keys and values of a dictionary.
n=int(input("Enter no of items:"))
d={}
for i in range(n):
    key=input("key:")
    value=input("value:")
    d[key]=value
for i in d:
    print("key:",i,"","value:",d[i])
for i in d.keys():
    print(i)
for i in d.values():
    print(i)



"""n=int(input("Enter no of items:"))
d={}
for i in range(n):
    key=input("key:")
    value=input("value:")
    d[key]=value
for i in d:
    print("key:",i,"","value:",d[i])
    print(f"key:{i} value:{d[i]}")
    print("key:{} value:{}".format(i,d[i]))
for i in d.keys():
    print(i)"""
for i in d.values():
    print(i)
