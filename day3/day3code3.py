s1,s2=map(str,input().split())
s3=''
for i in s2:
    if i not in s1:
        s3+=i
print(s3)
