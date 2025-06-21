"""
Q1. Use a while loop to calculate the sum of the first 10 natural numbers.

def sumOfFirst10NaturalNumber(a: int) -> int:
    i: int = 1
    total: int = 0
    while i <= a:
        total += i
        # print(total, end=" ")
        i += 1
        # print(i, end=" ")
    return total


sum: int = sumOfFirst10NaturalNumber(10)
print(sum)
"""

"""
Q2. Ask a positive number from user. Print all the numbers from positive number to 1.
Example n = 7
Output: 7 6 5 4 3 2 1

def printPositiveNumberFromUserInput(num: int):
    i = num
    # print(i)
    while i >= 1:
        print(i, end=" ")
        i -= 1


# num: int = int(input("Enter Any Positive Number To 1 : "))
printPositiveNumberFromUserInput(6)
"""

"""
Q3. Print this pattern using while loop. 1 8 15 22 29 36 43 50 57 64 71 78 85 92 99

def printNumber(num) -> int:
    i = 1
    while i <= num:
        print(i, end=" ")
        i += 7

printNumber(99)
"""

"""
Q4. Print all odd numbers less than 15 using a while loop

def printOddNumber(num) -> int:
    i = 1
    while i <= num:
        # print(i, end=" ")
        if i % 2 != 0:
            print(f"{i}", end=" ")
        i += 1

printOddNumber(15)
"""

"""
Q5. Calculate the factorial of a given number using a while loop.
Example, n = 5
5 x 4 x 3 x 2 x 1
Output: 120

"""


def factorialFuncation(n):
    i = 1
    while n > 0:
        i *= n
        n -= 1


factorialFuncation(5)

# n = int(input("Enter a number: "))
# factorial = 1

# while n > 0:
#     factorial *= n
#     n -= 1

# print(f"The factorial of the given number is: {factorial}")
