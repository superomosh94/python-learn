# Create a new file named **`day1_assignment.py`** and complete the following:

# #### **Part 1: Arithmetic Operators**

print("Day 1 Assignment")
print("addoition ", 12+8 )
print ("subtraction ", 50-25)
print ("maltiplication", 9*7)
print ("remainder" ,19%5)
print ("floor division",45//6)
print ("power",3**4)


# 1. Write Python statements that:

#    * Add 12 and 8
#    * Subtract 25 from 50
#    * Multiply 9 by 7
#    * Divide 45 by 6
#    * Find the remainder when 19 is divided by 5
#    * Use floor division for 45 divided by 6
#    * Raise 3 to the power of 4

#    **Print** the results with short explanations like:

#    ```python
#    print("Addition:", 12 + 8)
#    ```

# ---

# #### **Part 2: Data Type Identification**

# 2. Create and print the type of each of these:

#    * An integer
print(type(67))
print(type(9.6))
print(type(5+5j))
#    * A float
#    * A complex number
#    * A string (your name)
print(type("mato"))
#    * A list of three fruits
print (type(["mango","apple","banana","orange"]))
#    * A tuple of three numbers
print (type((3,6,9)))
#    * A dictionary with keys `name`, `age`, and `country`
print (type({"name":"mato","age":24,"country":"kenya"}))    
#    * A set containing 3 unique numbers
print (type({2,4,6}))
#    * A boolean that checks if 7 is greater than 3
print (type(7>3))

#    Example:

#    ```python
#    print(type(7))
#    ```

# ---

# #### **Part 3: Apply Your Knowledge**

# 3. Write a short Python program that:

#    * Stores your **age**, **height**, and **is_student** (boolean).
age=20
height=1.75
is_student=True

print("age :",age,type(age))
print("height :",height,type(height))
print("is_student :",is_student,type(is_student))


if age>18:
    print ("true")
else:
    print("false")



#    * Prints all values and their data types.
#    * Prints whether your age is greater than 18 using a comparison.

# ---

# ### **Expected Output Example**

# ```
# Addition: 20
# Subtraction: 25
# Multiplication: 63
# Division: 7.5
# Remainder: 4
# Floor Division: 7
# Exponent: 81
# <class 'int'>
# <class 'float'>
# <class 'complex'>
# <class 'str'>
# <class 'list'>
# <class 'tuple'>
# <class 'dict'>
# <class 'set'>
# <class 'bool'>
# Age: 19 <class 'int'>
# Height: 1.75 <class 'float'>
# Is student: True <class 'bool'>
# Adult: True
# ```

# ---

# **Goal:**
# Test your understanding of:

# * Arithmetic operations
# * Data types
# * Boolean expressions
# * The `type()` function
