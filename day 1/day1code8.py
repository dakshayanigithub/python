#write the python program to check the year is leapyear or not
year=int(input("Enter a year:"))
if year%400==0 or (year%4==0 and year%100!=0):
    print("Leap Year")
else:
    print("Not a Leap Year")
