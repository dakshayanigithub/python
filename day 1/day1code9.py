nc,cd=map(int,input().split())
if cd >= nc:
    np=0
else:
    c=nc-cd
    if c%4==0:
        np=c//4
    else:
        np=(c//4)+1
print(np)
