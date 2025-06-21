"""
i = 1
while i <= 10:
    print("hello wolrd")
    i += 1  # i = i + 1
"""

"""
i = 1
while i <= 10:
    i += 15
    print(i)
    # i += 1
"""

"""
a: int = int(input("Enter A Number : "))
i = 1
while i <= a:
    print(i)
    i += 1
"""

"""
def printHello(a):
    i = 1
    while i <= a:
        print(i, end=" ")
        i += 1
    print()


a: int = int(input("Enter The Number : "))
printHello(a)
# printHello(-5)
"""

"""
def printNumber(start, e):
    i = start
    while i <= e:
        print(i, end=" ")
        i += 1
    print()


start: int = int(input("Enter The Start Number : "))
e: int = int(input("Enter The End Number : "))
printNumber(start, e)
"""

"""
i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print(total)
"""

"""
def sumOfNumber():
    i = 1
    total = 0
    while i <= 10:
        total += i
        i += 1
    return total


x = sumOfNumber()
print(x)
"""


def sumOfEvenNumber(start, e):
    i = start
    total = 0
    while i <= e:
        if i % 2 == 0:
            total += i
        i += 1
    return total


start: int = int(input("Enter The Start Number : "))
e: int = int(input("Enter The End Number : "))
x = sumOfEvenNumber(start, e)
print(x)
