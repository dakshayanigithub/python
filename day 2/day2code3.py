#write a python program to print the number which are not divisible by 6,7,8 in a given range
n,m=int(input("Enter a number")),int(input("Enter a nuber"))
i=n
while i <= m:
    if i%6!=0 and i%7!=0 and i%8!=0:
        print(i)
        i+=1
        
        
