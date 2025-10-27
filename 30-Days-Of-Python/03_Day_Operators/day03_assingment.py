# # Task 1: Create two variables x = 15 and y = 4
# # Print their addition, subtraction, multiplication, division, floor division, modulus, and exponentiation results.
# x=15
# y=4


# print("Addition :",x+y)
# print("Subtraction :",x-y)
# print("multiplication :",x*y)
# print("Division :",x/y)
# print("floor division :",x//y)
# print("Modulus :",x%y)
# # print("exponentiation result :",x+y)



# # Task 2: Calculate the area of a triangle

# # Use base = 12 and height = 8
# # Formula: area = 0.5 * base * height
# base=12,height=8
# print("area of triangle :",0.5*base*height)

# # Task 3: Calculate the perimeter of a rectangle
# # Use length = 25 and width = 10
# # Formula: perimeter = 2 * (length + width)

# lenght=25,width=10,
# perimeter=2*(lenght+width)
# print("perimeter is :",perimeter)


# # Task 4: Calculate weight using user input
# # Ask the user for mass in kilograms and use gravity = 9.81
# # Formula: weight = mass * gravity
# mass=input("enter mass in KGs")
# gravity=9.81
# weight=mass*gravity
# print("calculated weight is ", weight)


# # Task 5: Calculate area and circumference of a circle
# # Use radius = 7
# # Formulas:
# # area = 3.14 * radius ** 2
# # circumference = 2 * 3.14 * radius
# PI=3.14
# radius=input("input radius to calculate the area of the circle ")
# area=PI*radius**2
# print("the area from the radius input is ",area)



# # Task 6: Compare two numbers a = 10, b = 7
# # Print results for >, <, ==, !=, >=, and <= comparisons.

# a=10,b=7,
# print(a>b)
# print(a==b)
# print(a<b)
# print(a>=b)
# print(a!=b)
# print(a<=b)
# # print(a>b)
# # print(a>b)


# # Task 7: Compare the lengths of "banana" and "mango"
# # Use len() to check which one is longer.
# len("banana") > len("mango")
# len("banana") < len("mango")
# len("banana") = len("mango")

# # Task 8: Check membership and identity
# # 'P' in 'Python'
# # 'p' in 'Python'
# # 'on' in 'Python'
# # 1 is 1
# # 2 is not 3


# # Task 9: Boolean checks
# # True and False
# # True or False
# # not True
# # not (3 > 1)


# # Task 10: Mini Challenge
# # Ask the user for a number
# # Print whether it is positive or negative
# # Then print whether it is even or odd

# num=float(input("input a number ??"))
# if num>0:
#     print("positive number")
# elif num<0:
#     print("negative number")
# else:
#     print("zero")
# Task 1: Arithmetic operations
x = 15
y = 4

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulus:", x % y)
print("Exponentiation:", x ** y)  # Fixed this line

# ---------------------------------------------------------

# Task 2: Area of a triangle
base = 12
height = 8
area_triangle = 0.5 * base * height
print("Area of triangle:", area_triangle)

# ---------------------------------------------------------

# Task 3: Perimeter of a rectangle
length = 25
width = 10
perimeter = 2 * (length + width)
print("Perimeter of rectangle:", perimeter)

# ---------------------------------------------------------

# Task 4: Calculate weight using user input
mass = float(input("Enter mass in KGs: "))
gravity = 9.81
weight = mass * gravity
print("Calculated weight is:", weight)

# ---------------------------------------------------------

# Task 5: Area and circumference of a circle
PI = 3.14
radius = float(input("Input radius to calculate the area of the circle: "))
area = PI * radius ** 2
circumference = 2 * PI * radius
print("Area of circle:", area)
print("Circumference of circle:", circumference)

# ---------------------------------------------------------

# Task 6: Comparison between two numbers
a = 10
b = 7
print("a > b:", a > b)
print("a == b:", a == b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a != b:", a != b)
print("a <= b:", a <= b)

# ---------------------------------------------------------

# Task 7: Compare lengths of two words
print("Is 'banana' longer than 'mango'?", len("banana") > len("mango"))
print("Is 'banana' shorter than 'mango'?", len("banana") < len("mango"))
print("Are they equal in length?", len("banana") == len("mango"))  # Fixed '=' to '=='

# ---------------------------------------------------------

# Task 8: Membership and identity
print("'P' in 'Python':", 'P' in 'Python')
print("'p' in 'Python':", 'p' in 'Python')
print("'on' in 'Python':", 'on' in 'Python')
print("1 is 1:", 1 is 1)
print("2 is not 3:", 2 is not 3)

# ---------------------------------------------------------

# Task 9: Boolean checks
print("True and False:", True and False)
print("True or False:", True or False)
print("not True:", not True)
print("not (3 > 1):", not (3 > 1))

# ---------------------------------------------------------

# Task 10: Positive/Negative and Even/Odd check
num = float(input("Input a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")20
else:
    print("Zero")

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
