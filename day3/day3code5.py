#insert digit
s,d=map(str,input().split())
for i in range(len(s)):
    if int(s[i]) <= int(d):
        print(s[:i]+d+s[i:])
        break
else:
    print(s+d)
