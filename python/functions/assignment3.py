"""
Q1. Write a Python function to find the Maximum and minimum of three numbers. Use 3 parameters. Make 2 different functions named as maxi and mini.

def maxi(a: int, b: int, c: int):
    maxNum = a
    if b >= maxNum:
        maxNum = b
    if c >= maxNum:
        maxNum = c
    print(f"maximum number is {maxNum}")


def mini(a: int, b: int, c: int):
    minNum = a
    if b <= minNum:
        minNum = b
    if c <= minNum:
        minNum = c
    print(f"maximum number is {minNum}")


a: int = int(input("Enter 1st Number : "))
b: int = int(input("Enter 2nd Number : "))
c: int = int(input("Enter 3rd Number : "))

maxi(a, b, c)
mini(a, b, c)

"""

"""
Q2. Attempt the same leap year question (Week 1 - Assignment 2 - Q8) but using function. Try calling function with different years as a parameter and check the output.
Q3. Attempt the same bill calculator question (Week 1 - Assignment 2 - but using function. Try calling function with different bill amount as a parameter and check the output.
Q4. Attempt Week 1 - Assignment 2 (Q6) and Week 1 - Assignment 2 (Q7) using function.
Q5. Write a function named personal_greet that takes a name as a parameter and prints a greeting message with that name. For example, personal_greet("Alice") should print "Hello, Alice!".

def personal_greet(name: str):
    print(f"hello,{name}!")


name: str = str(input("Enter Your Name : "))
personal_greet(name)
"""

"""
Q6. Write a function named is_even that takes a number as a parameter and prints "Even" if the number is even and "Odd" if the number is odd.
Q7. Write a function named celsius_to_fahrenheit that converts Celsius to Fahrenheit and prints the result. (Formula: (Celsius * 9/5) + 32 = Fahrenheit)
Q8. Create a function named simple_calculator that takes three parameters: two numbers and an operation (addition or subtraction represented by '+' or '-'), and prints the result of the operation.
Q9. Write a function named check_number that takes a number and prints whether it is positive, negative, or zero.
Q10. Write a function named is_odd_even that determines if a number is odd or even without using the modulo operator (%). Hint: Use division or subtraction.
Q11. Write a function named calculate_interest that takes the principal, rate of interest, and time as parameters and prints the simple interest calculated.
"""
