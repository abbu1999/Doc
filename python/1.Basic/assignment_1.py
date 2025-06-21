"""
Q1. There are two variables.
	a=5
	b=10
	What will be the output of following:
		a > 5 and b >= 10
		a >= 5 or not b > 10
		not ( a > 5 and b > 5)
		not ( a < 10 or not b < 10)
		not ( not a <= 5 or not b >= 10)

# a = 5
# b = 10
# print(a > 5) #false
# print(b >= 10) #true
# print(a >= 5 or not b > 10) # true => a is true or(either one is true) not(reverse the bool[T-F][F-T]) b is false (but due to not it is changing false into true) due to that it is output true.
# print(not ( a > 5 and b > 5)) # true => both a and b is false due to not it is showing false.
# print(not ( a < 10 or not b < 10)) # false => a is true or(either one is true) not(reverse the bool[T-F][F-T]) b is false (but due to not it is changing false into true) both condition is true but not change it into flase.
# print(not ( not a <= 5 or not b >= 10)) # true => a is true (but due to not it is changing true into false),  b is true (but due to not it is changing true into false) , false or false is flase and not changeing into true.
"""

"""
#Q2. Python program to convert kilometers to miles. Ask kilometer from User.

miles_value = 0.621371
km = int(input("input kilometers to convert into miles "))
miles = km * miles_value
print(f"if we convert {km} km into miles the ans is {miles}")
"""

"""
# Q3. Ask 3 numbers from User and Calculate the Average.

a = int(input("Enter First value: "))
b = int(input("Enter First value: "))
c = int(input("Enter First value: "))
avg = (a + b + c) / 3
print(f"avg of {a} and {b} and {c} is {avg}")
"""

"""
# Q4. Ask value in Rupees and Convert into Paise.

paise_value = 100
rupee = int(input("Enter Rupee To Convert Into Paise: "))
paise = rupee * paise_value
print(f"{rupee} rupee have {paise} paise")
"""

"""
# Q5. Calculate Area of Square by taking side from User.

side = int(input("Enter Area To convert Into Square: "))
square = side * side
print(f"The Square of {side} is {square} square")
"""

# Q6. Ask number of games played in a tournament. 
#Ask the user number of games won and number of games loss. 
#Calculate number of tie and total Points. (1 win= 4 points, 1 tie =2 points)
#win = 4
#tie = 2

"""
# Q7. Check if the number entered by User is divisible by 3 or not.

a = int(input("Enter Any Number To Check It Is Divisible By 3 Or not: "))
if a % 3 == 0:
    print(f"Number {a} is divisible by 3 ")
else:
    print(f"Number {a} is not divisible by 3 ")
"""

"""
# Q8. Ask a number from user. Print if the number is ODD or EVEN.

a = int(input("Enter Any Number To Check Number Is Even Or Odd: "))
if a % 2 == 0:
    print(f"Number {a} is Even ")
else:
    print(f"Number {a} is Odd ")
"""

# Q9. Take values of length and breadth of a rectangle from user and check if it is square or not.
a: float = float(input("Enter value of length: "))
b: float  = float(input("Enter value of breadth: "))

a = float(input("Enter value of length: "))
b = float(input("Enter value of breadth: "))
if a == b:
    print(f"The rectangle is square")
else:
    print(f"The rectangle is not square")