#write a pyhton program to print factiorial using class and methods.
"""class Factorial:
    def _init_(self, number):
        self.number = number
    def calculate_factorial(self):
        factorial_result = 1
        for i in range(1, self.number + 1):
            factorial_result *= i
        return factorial_result
# Taking input from the user
num = int(input("Enter a number to calculate its factorial: "))
# Creating an instance of the Factorial class
factorial_calculator = factorial(num)
# Calculating factorial using the method of the Factorial class
result = factorial_calculator.calculate_factorial()
print(f"The factorial of {num} is: {result}")"""

"""class day6:
    def fact(self,n):
        f=1
        for i in range(1,n+1):
             f*=i
        print(f)
obj=day6()
obj.fact(int(input()))"""

class day6:
    def __init__(self,data):
        self.data=data
        self.fact(data)
    def fact(self,n):
        f=1
        for i in range(1,n+1):
             f*=i
        print(f)
obj=day6(int(input()))
