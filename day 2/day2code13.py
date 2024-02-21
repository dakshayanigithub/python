#write a python program to remove consecutive duplicates in a given string
s=input()
s1=s[0]
for i in range(1,len(s)):
    if s [i-1]!=s[i]:
        s1+=s[i]
print(s1)
