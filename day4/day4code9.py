#write a python program to check whether the given string is panagram or not
import string
s=input()
s=s.lower()
s1=string.ascii_lowercase
if set(s) == set(s1):
    print("panagram")
else:
    print("Not a panagram")
