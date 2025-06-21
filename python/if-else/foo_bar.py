# FOO-BAR
"""
User input (number)
if divisible by 3: FOO
Divisible by 5: BAR
divisible by 3 and 5 : FOOBAR
FOOFOOBARBAR
"""
a: int = int(input("Enter The Number: "))
if a % 3 == 0:
    print("FOO")
elif a % 5 == 0:
    print("BAR")
elif a % 3 == 0 and a % 5 == 0:
    print("FOOBAR")
else:
    print("FOOFOOBARBAR")

a: int = int(input("Enter The Number: "))
if a % 3 == 0 and a % 5 == 0:
    print("FOOBAR")
elif a % 3 == 0:
    print("FOO")
elif a % 5 == 0:
    print("BAR")
else:
    print("FOOFOOBARBAR")
