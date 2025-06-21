"""
Q1. Write a program that takes two numbers as input and checks if the first number is divisible by the second.

a: int = int(input("Enter The First Number : "))
b: int = int(input("Enter The Second Number : "))

if a % b == 0:
    print(f"the first number is divisible by the second")
else:
    print(f"the first number is not divisible by the second")
"""

"""
Q2. A student will not be allowed to sit in exam if his/her attendance is less than 75%.
	Take following input from user
		Number of classes held
		Number of classes attended.
	1. Print percentage of class attended
	2. Print Is student is allowed to sit in exam or not.

a: int = int(input("Number of classes held : "))
b: int = int(input("Number of classes attended : "))
percentage = (b / a) * 100
print(f"your percentage is {percentage}%")
if percentage >= 75:
    print(f"you are allowed to sit in exam")
else:
    print(f"you are not allowed to sit in exam")
"""

"""
Q3. Write a program to check if number is divisible by 2 and 3 but not 8.

a: int = int(input("Enter A Number : "))
if a % 2 == 0 and a % 3 == 0 and a % 8 != 0:
    print(f"Number {a} is divisible by 2 and 3 but not by 8")
else:
    print(f"Number {a} is not matched by conditions")
"""

"""
Q4. Write a Python program that takes a student's score as input and prints the corresponding grade. Use the following grading scale:
	A: 90-100
	B: 80-89
	C: 70-79
	D: 60-69
	F: Below 60

a: int = int(input("Please input your obtain Marks : "))
if a >= 90 and a <= 100:
    print(f"A")
elif a >= 80 and a <= 89:
    print(f"B")
elif a >= 70 and a <= 79:
    print(f"C")
elif a >= 60 and a <= 69:
    print(f"D")
elif a <= 60:
    print(f"F")
else:
    print(f"Invaild Input")
"""

"""
Q5. Write a program to calculate bill. Ask the final amount from the user. You have to give discount and print the final bill after discount.
	50000 above - 30% discount
	40000 - 49999 - 25% discount
	30000 - 39999 - 20% discount
	10000 - 29999 - 10% discount
	1 - 9999 - No discount
Print the discount and the final amount to be paid.
	Example 1
		Enter bill amount = 80000
		You got 30% discount
		Your final bill is Rs. 56000

a: float = float(input("Enter Your Total Bill Ammount : "))
discount = 0
if a >= 50000:
    discount = 30
elif a >= 40000 and a <= 49999:
    discount = 25
elif a >= 30000 and a <= 39999:
    discount = 20
elif a >= 10000 and a <= 29999:
    discount = 10
elif a >= 1 and a <= 9999:
    discount = 0

discount_price = (discount * a) / 100
print(f"yout discount price {discount_price}")
final_bill = a - discount_price

print(f"you got {discount}% discount")
print(f"Your final bill is Rs. {final_bill:.2f}")

"""
"""
Q6. Ask 4 numbers from user. Make sure all the numbers entered by user are different. Print which number is the smallest.

a: int = int(input("Enter The first Number : "))
b: int = int(input("Enter The second Number : "))
c: int = int(input("Enter The thrid Number : "))
d: int = int(input("Enter The fourth Number : "))

smallest_num = a

if b <= smallest_num:
    smallest_num = b
if c <= smallest_num:
    smallest_num = c
if d <= smallest_num:
    smallest_num = d
print(f"The smallest num is {smallest_num}")

# we are not using elif thing here becuse in elif any one condition is true other code will exits and provide worng output
"""
"""
Q7. Take Salary as input from User and Update the salary of an employee.
	salary less than 10,000, 5 % increment
	salary between 10,000 and 20, 000, 10 % increment
	salary between 20,000 and 50,000, 15 % increment
	salary more than 50,000, 20 % increment

a: int = int(input("Enter Your Salary : "))
if a >= 50000:
    increment = 20
elif a >= 20000 and a <= 50000:
    increment = 15
elif a >= 10000 and a <= 20000:
    increment = 10
elif a <= 10000:
    increment = 5

increment_ammount = (increment * a) / 100
increment_salary = increment_ammount + a

print(f"your salary is : {a}")
print(f"Your increment is {increment_ammount}")
print(f"your new salary is {increment_salary}")
"""
"""
Q8. An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. A leap year contains a leap
day.
These are the conditions used to identify leap years:
	if the year can be evenly divided by 4, it is then a leap year
	but if the year is evenly divided by 4 and also by 100, then it is NOT a leap year
	but if the year is evenly divided by 4 and also by 400, then it is a leap year
This means the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Ask a year input from user. And tell if the year entered by user is leap or not.
"""
a: int = int(input("Enter The year to check leap year or not : "))
if a % 400 == 0:
    print(f"year {a} leap year")
elif a % 4 == 0 and a % 100 == 0:
    print(f"year {a} is not leap year")
elif a % 4 == 0:
    print(f"year {a} leap year")
else:
    print("Invaild Input")
