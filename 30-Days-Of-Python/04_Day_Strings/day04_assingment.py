# Task 1: Basic String Operations
# 1. Create a variable 'letter' with value 'P'
letter="P"

# 2. Print the letter
print(letter)

# 3. Print the length of the letter
print(len(letter))
# 4. Create a variable 'greeting' with value "Hello, Python!"
greeting="Hello, Python!"
# 5. Print the greeting
print(greeting)
# 6. Print the length of the greeting
print("greeting lenght is :",len(greeting))
# 7. Create a variable 'sentence' with "I am learning Python programming"
sentence="I am learning Python programming"
# 8. Print the sentence
print( "the sentece is :",sentence)
# 9. Print the third character of the sentence
index3=sentence[2]
print('third character in sentence is :',index3)
# 10. Print the last character using negative indexing
last_character=len(sentence) -1
print('the last character in sentence is :',last_character)


# Task 2: Multiline Strings
# 1. Create a multiline string variable 'about_me' describing yourself in 3 lines using triple quotes
about_me=''' this is sample  multiple line variable 
it has been created to describe myself in a variale name about_me
it can extend to as many lines as possible'''

# 2. Print 'about_me'
print("this is the about me message sturedm::",about_me)


# Task 3: String Concatenation
# 1. Create variables 'first_name' and 'last_name'
first_name="loream"
second_name="Ipsum"


# 2. Concatenate them with a space in between to create 'full_name'
full_name=first_name +" "+second_name
# 3. Print 'full_name'
print("full name is :",full_name)
# 4. Print the total number of characters in 'full_name' using len()
lenght=len(full_name)
print("The lenght of full name is :",lenght)


# Task 4: String Indexing and Slicing
# 1. Set 'language' = "Python"
language="Pyrhon"
# 2. Print the first character
print("first index character is ::",language[0])
# 3. Print the last character
print( "last index character in this word is ::",language[-1])
# 4. Print "Pyt" using slicing
first_3=language[0:3]
print(" first 3 characters by slicing are",first_3)
# 5. Print "hon" using negative slicing
last_3=language[-3:]
# 6. Print every second letter in "Python"
print("second letter in python is :",language[1])


# Task 5: Escape Sequences
# 1. Print the table below using \n and \t
# Day   Topics   Exercises
# 1     Strings   5
# 2     Lists     4
# 3     Loops     6
print('Day\tTopics\tExercises\n1\tStrings\t5\n2\tLists\t4\n3\tLoops\t6')

# Task 6: String Methods
# 1. Create a variable 'text' = "thirty days of python"
test="thirty days of Python currently day four"
# 2. Capitalize the first letter
print(test.capitalize())
# 3. Count how many times 'y' appears
print(test.count("y"))
# 4. Check if it ends with "on"
print(test.endswith("on"))
# 5. Find the position of 'd'
print(test.find("d"))
# 6. Replace "python" with "coding"
print(test.replace('Python','coding'))

# 7. Convert all characters to uppercase
print(test.upper())
# 8. Convert all characters to lowercase
print(test.lower())

# 9. Swap letter cases
print(test.swapcase())
# 10. Check if all characters are alphabetic
print(test.isalpha())
# 11. Split the string into words
print(test.split())


# Task 7: Format Strings
# 1. Use .format() to print: "My name is John Doe. I am a student. I live in Kenya."


# Define the variables
name = "John Doe"
occupation = "student"
country = "Kenya"

# Use the .format() method to insert the variables into the string
sentence = "My name is {}. I am a {}. I live in {}.".format(name, occupation, country)

# Print the result
print(sentence)

# Task 8: Practice Challenge

# 1. Ask the user to input their favorite word
fav_word = input("Input your favorite word: ")

# 2. Print the word in uppercase
print("\nUppercase:", fav_word.upper())

# 3. Print the word in lowercase
print("Lowercase:", fav_word.lower())

# 4. Print the number of letters in the word
print("Length of word is:", len(fav_word))

# 5. Check if the word starts with a vowel (A, E, I, O, U)

# Convert the entire word to lowercase for a reliable check.
# This ensures we only check against 'a', 'e', 'i', 'o', 'u'.
first_letter_lower = fav_word[0].lower()

# Define the set of vowels
vowels = 'aeiou'

# Check if the lowercase first letter is IN the vowels string
if first_letter_lower in vowels:
    print(f"\nStarts with Vowel: Yes, '{fav_word}' starts with a vowel.")
else:
    print(f"\nStarts with Vowel: No, '{fav_word}' does not start with a vowel.")
