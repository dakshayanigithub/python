#write a python program to make encryption and decryption with a key value write a functions.
def encryption(s,k):
    s1=""
    for i in s:
        x=ord(i)+k
        s1+=chr(x)
    print(s1)
def decryption(s,k):
    s1=""
    for i in s:
        x=ord(i)-k
        s1+=chr(x)
    print(s1)
k=int(input("Enter key value: "))
s=input("Enter string: ")
op=input("Select operation: ")
if op=="encrypt" :
      encryption(s,k)
elif op=="decrypt":
    decryption(s,k)
else:
    print("inproper operation")
