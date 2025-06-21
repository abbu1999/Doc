def greet():
    print("I Am Greet Function")


greet()


def greet():
    pass


greet()


# pram a b
def addition(a: int | str, b: int | str):
    total = a + b
    print(total)


# ARG 10 20
addition(10, 20)
addition("abhi", "abbu")


def marks(physics: float, chemistry: float, maths: float, english: float):
    total = physics + chemistry + maths + english
    print(f"Total marks scored = {total}")


# marks(59, 87, 81, 99)
# named pram
marks(english=99, physics=11, maths=34, chemistry=100)
marks(59, 88, english=11, maths=89)
marks(59, 88, english=11, maths=89)


# Defult Prem(where in pram have some default value)
def marks(physics: int, chemistry: int = 0, hindi: int = 0):
    print(f"Physics marks = {physics}")
    print(f"Chemistry marks = {chemistry}")
    print(f"Hindi marks = {hindi}")
    print(f"Total = {physics+chemistry+hindi}")


# marks(45, 43, 100)
marks(33, 99)


def marks(m1, m2):
    total = m1 + m2
    return total


x = marks(10, 20)
print(x)
print(marks(10, 50))


# def marks(m1, m2) -> int: #if we return and will provide data type after arrow
def marks(m1, m2) -> None:
    total = m1 + m2
    print(total)


x = marks(10, 20)
print(x)  # None
