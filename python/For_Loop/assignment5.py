"""
Q1. Create a function named divs, which will take two parameters n1 and n2. Return the count of how many numbers from 1 to n1 are divisible by n2.

def divs(n1, n2):
    divisibleByTwo = 0
    for i in range(1, n1 + 1):
        if i % n2 == 0:
            divisibleByTwo += 1
    print(divisibleByTwo)

n1 = 20
n2 = 2
divs(n1, n2)
"""

"""
Q4. Create a function named pattern which takes an integer as an input and print the following pattern.
"""


def pattern(num):
    a = 0
    for i in range(1, num + 1):
        a += 10
        print(a, end=" ")


num: int = int(input("Enter The Number : "))
pattern(num)


# def pattern(num):
#     a = 0
#     for i in range(1, num + 1):
#         print(a, end=" ")
#         a += 2


# num: int = int(input("Enter The Number : "))
# pattern(num)
