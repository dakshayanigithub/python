first_tv=int(input("Enter a number"))
second_tv=int(input("Enter a nuber"))
discount_first_tv=int(input("Enter a number "))
discount_second_tv=int(input("Enter a number "))
a=first_tv - discount_first_tv
b=second_tv - discount_second_tv
if a<b:
    print("first")
elif a>b:
    print("second")
else:
    print("any")


