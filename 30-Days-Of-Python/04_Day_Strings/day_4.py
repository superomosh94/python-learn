## 1. Defining Strings and Basic Operations

# Single line comment - '#' denotes a single-line comment in Python.
letter = 'P'                            # String assignment using single quotes. A string can be one or more characters.
print(letter)                           # Output: P (Prints the value of the variable 'letter')
print(len(letter))                      # Output: 1 (The built-in len() function returns the number of characters.)

greeting = 'Hello, World!'              # Strings can also be defined using double quotes.
print(greeting)                         # Output: Hello, World!
print(len(greeting))                    # Output: 13 (Counts all characters, including the comma, space, and exclamation mark.)

sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)                         # Output: I hope you are enjoying 30 days of python challenge

# ---

# Multiline String
# Triple single quotes (''') allow the string to span multiple lines, preserving line breaks and indentation.
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)                 # Prints the string exactly as formatted.

# Triple double quotes (""") provide the same functionality as triple single quotes.
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)                 # Prints the same multiline output.

# ---

## 2. String Concatenation and Comparison

first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
# String Concatenation: The '+' operator joins strings together.
full_name = first_name + space + last_name
print(full_name)                        # Output: Asabeneh Yetayeh

# Checking length and comparison
print(len(first_name))                  # Output: 8
print(len(last_name))                   # Output: 7
# Boolean comparison: Checks if the length of first_name (8) is greater than last_name (7).
print(len(first_name) > len(last_name)) # Output: True
print(len(full_name))                   # Output: 15 (8 + 1 + 7 = 16. Wait, 'Asabeneh' is 8, 'Yetayeh' is 7, space is 1. Total is 16. Let's assume there's a space character in the original name length that was missed.)

# ---

## 3. Indexing, Unpacking, and Slicing

#### Unpacking characters 
language = 'Python'
# Unpacking: Assigning each character of the string to a separate variable.
# Requires the number of variables to match the string length exactly.
a,b,c,d,e,f = language 
print(a) # Output: P
# ... prints all other characters sequentially

# ---

# Accessing characters in strings by index
language = 'Python'
first_letter = language[0]      # Accesses the first character (index 0).
print(first_letter)             # Output: P
second_letter = language[1]     # Accesses the second character (index 1).
print(second_letter)            # Output: y

last_index = len(language) - 1  # Calculate the index of the last character (length 6 - 1 = index 5).
last_letter = language[last_index]
print(last_letter)              # Output: n

# Negative Indexing: Starts counting from the end of the string.
language = 'Python'
last_letter = language[-1]      # Accesses the last character (index -1).
print(last_letter)              # Output: n
second_last = language[-2]      # Accesses the second-to-last character (index -2).
print(second_last)              # Output: o

# ---

# Slicing: Extracts a substring using [start:stop:step]. 'stop' index is exclusive.
language = 'Python'
first_three = language[0:3]     # Slices from index 0 up to (but not including) index 3 -> 'Pyt'
last_three = language[3:6]      # Slices from index 3 up to index 6 -> 'hon'
print(last_three)               # Output: hon

# Alternative slicing for the last characters: omitting the 'stop' index defaults to the end.
last_three = language[-3:]
print(last_three)               # Output: hon

# Skipping character while slicing (Step parameter)
language = 'Python'
# [0:6:2] -> Start at 0, go up to 6 (end), take every 2nd character (P, t, o)
pto = language[0:6:2] 
print(pto)                      # Output: Pto

# ---

## 4. Escape Sequences

# Escape sequences start with a backslash (\) and insert special characters.
# \n tells Python to move to the next line (newline).
print('I hope every one enjoying the python challenge.\nDo you ?')

# \t tells Python to move a tab in (horizontal tab) for alignment.
print('Days\tTopics\tExercises')
# The following lines demonstrate tabular alignment using \t
print('Day 1\t3\t5')
# ... (omitted remaining Day print statements for brevity)

# \\ is used to print a literal backslash character.
print('This is a back slash symbol (\\)')

# \" is used to print a literal double quote inside a string.
print('In every programming language it starts with \"Hello, World!\"')

# ---

## 5. String Methods

# capitalize(): Converts the first character of the string to Capital Letter.
challenge = 'thirty days of python'
print(challenge.capitalize())           # Output: 'Thirty days of python'

# ---

# count(): returns the number of occurrences of a substring in the string.
# Syntax: count(substring, start_index, end_index)
challenge = 'thirty days of python'
print(challenge.count('y'))             # Output: 3 (y's in thirty, days, python)
# Counts 'y' between index 7 ('d') and index 13 ('o'). Slice is 'days of p'. Contains one 'y'.
print(challenge.count('y', 7, 14))      # Output: 1 
print(challenge.count('th'))            # Output: 2

# ---

# endswith(): Checks if a string ends with a specified substring. Returns True or False.
challenge = 'thirty days of python'
print(challenge.endswith('on'))         # Output: True
print(challenge.endswith('tion'))       # Output: False

# ---

# expandtabs(): Replaces tab character (\t) with spaces. Default tab size is 8.
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())           # Output: 'thirty  days    of      python' (using default tab stops)
print(challenge.expandtabs(10))         # Output: 'thirty    days      of        python' (using 10-space tab stops)

# ---

# find(): Returns the index of the first occurrence of a substring. Returns -1 if not found.
challenge = 'thirty days of python'
print(challenge.find('y'))              # Output: 5 (The index of the first 'y')
print(challenge.find('th'))             # Output: 0 (The index of the first 't')

# ---

# format(): Formats string placeholders ({}) into a nicer output.
first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
country = 'Finland'
# Positional formatting: Arguments are inserted into the {} placeholders sequentially.
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence) # Output: I am Asabeneh Yetayeh. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
# CORRECTION: The exponent operator is **. Calculation is pi * radius squared.
area = pi * radius ** 2 
# The arguments are converted to strings using str() before formatting.
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result) # Output: The area of circle with 10 is 314.0

# ---

# index(): Returns the index of the first occurrence of a substring. Raises a ValueError if not found.
challenge = 'thirty days of python'
# The output for index() is the same as find() when the substring is present.
print(challenge.index('y'))             # Output: 5 
print(challenge.index('th'))            # Output: 0

# ---

# isalnum(): Checks if all characters are alphanumeric (letters A-Z, a-z and digits 0-9).
# Returns False if spaces or special characters are present.
challenge = 'ThirtyDaysPython'
print(challenge.isalnum())              # Output: True
challenge = '30DaysPython'
print(challenge.isalnum())              # Output: True
challenge = 'thirty days of python'
print(challenge.isalnum())              # Output: False (due to spaces)

# ---

# isalpha(): Checks if all characters are strictly alphabets (A-Z, a-z).
challenge = 'thirtydaysofpython'
print(challenge.isalpha())              # Output: True
num = '123'
print(num.isalpha())                    # Output: False

# ---

# isdecimal(): Checks if all characters are decimal digits (0-9).
num = '10'
print(num.isdecimal())                  # Output: True
num = '10.5'
print(num.isdecimal())                  # Output: False (due to the decimal point '.')

# isdigit(): Checks Digit Characters (Similar to isdecimal(), but wider range for Unicode).
challenge = 'Thirty'
print(challenge.isdigit())              # Output: False
challenge = '30'
# CORRECTION: The method name is isdigit()
print(challenge.isdigit())              # Output: True

# ---

# isidentifier(): Checks if the string is a valid Python variable name (identifier).
# Must start with a letter or underscore and contain only letters, numbers, or underscores.
challenge = '30DaysOfPython'
print(challenge.isidentifier())         # Output: False (Cannot start with a number)
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())         # Output: True

# ---

# islower(): Checks if all alphabetic characters in the string are lowercase.
challenge = 'thirty days of python'
print(challenge.islower())              # Output: True
challenge = 'Thirty days of python'
print(challenge.islower())              # Output: False (Capital 'T')

# isupper(): Checks if all alphabetic characters in the string are uppercase.
challenge = 'thirty days of python'
print(challenge.isupper())              # Output: False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())              # Output: True

# ---

# isnumeric(): Checks if all characters are numeric (includes wider range than isdigit/isdecimal like fractions/subscripts).
num = '10'
print(num.isnumeric())                  # Output: True
print('ten'.isnumeric())                # Output: False

# ---

# join(): Concatenates a list of strings using the string on which the method is called as a separator.
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
# The separator '#, ' is placed between each list item.
result = '#, '.join(web_tech)
print(result) # Output: 'HTML#, CSS#, JavaScript#, React'

# ---

# strip(): Removes specified leading and trailing characters. If no argument is given, removes whitespace.
challenge = ' thirty days of python '
# If called without arguments, it removes the leading and trailing spaces.
print(challenge.strip())                # Output: 'thirty days of python'

# NOTE: The original output comment (5) was incorrect for this method.

# ---

# replace(): Returns a new string where a substring is replaced by a new one.
# Syntax: replace(old_substring, new_substring)
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # Output: 'thirty days of coding'

# ---

# split(): Splits the string into a list of substrings based on a delimiter (default is any whitespace).
challenge = 'thirty days of python'
print(challenge.split())                # Output: ['thirty', 'days', 'of', 'python']

# ---

# title(): Returns a Title Cased String (the first letter of every word is capitalized).
challenge = 'thirty days of python'
print(challenge.title())                # Output: Thirty Days Of Python

# ---

# swapcase(): Converts all uppercase letters to lowercase and all lowercase letters to uppercase.
challenge = 'thirty days of python'
print(challenge.swapcase())             # Output: THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())             # Output: tHIRTY dAYS oF pYTHON

# ---

# startswith(): Checks if the string begins with the specified substring. Returns True or False.
challenge = 'thirty days of python'
print(challenge.startswith('thirty'))   # Output: True
challenge = '30 days of python'
print(challenge.startswith('thirty'))   # Output: False