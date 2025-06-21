"""
Q1. Create a function that takes three numbers as parameters and returns the largest among them. 
Also if no arguments are passed, make sure the parameters take default value as None and return answer as -1.
"""


def max(a: int, b: int, c: int) -> int:
    if a == "" and b == "" and c == "":
        return -1
    maxNum = a
    if b >= maxNum:
        maxNum = b
    if c >= maxNum:
        maxNum = c
    return maxNum


a: int = input("Enter The 1st Number : ")
b: int = input("Enter The 2nd Number : ")
c: int = input("Enter The 3rd Number : ")
maxi = max(a, b, c)
print(maxi)


"""
Q2. Implement a function that takes two parameters, base and exponent, 
and returns the result of raising the base to the power of the exponent.

def power(base: int, exponent: int) -> int:
    # return pow(base, exponent)
    return base**exponent


b: int = int(input("Enter The Base Value : "))
e: int = int(input("Enter The Exponent Value : "))
print(power(b, e))
"""
"""
Q3. Ask 3 numbers from user. Make a function which returns the middle of those 3 numbers. 
Then make a function to check if that middle number is divisible by both 3 and 4. Make 2 functions for reusability.

Q4. Write a Python program that takes four numbers from the user. Implement a function to find the average of the first three numbers. 
Then, create another function to check if the average is greater than or equal to the fourth number. 
Make sure to use these two functions to determine and print whether the average is greater than or equal to the fourth number or not.
"""


def calculateAvg(a: int, b: int, c: int) -> int | float:
    return (a + b + c) / 3


def checkFourthNumberIsEqalToOrGreaterThenAvg(avg: float, d: int) -> str:
    if avg <= d:
        return "Is Not Greater Than Or Equal To The"
    return "Is Greater Than Or Equal To The"


num1: int = int(input("Enter The 1st Number : "))
num2: int = int(input("Enter The 2nd Number : "))
num3: int = int(input("Enter The 3rd Number : "))
num4: int = int(input("Enter The 4th Number : "))

avg = calculateAvg(num1, num2, num3)

output = checkFourthNumberIsEqalToOrGreaterThenAvg(avg, num4)

print(
    f"The Avrage Of {num1} and {num2} and {num3} is : {avg} and Avrage Of First 3 Number {output} Fourth {num4} Number"
)
