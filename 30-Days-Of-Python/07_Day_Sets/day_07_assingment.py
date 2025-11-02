# ---------------------------------------------------------------------
# LEVEL 1 ASSIGNMENT
# ---------------------------------------------------------------------

# 1. Create an empty set named 'my_set'
# (Hint: use set() constructor, not {} because that creates a dictionary)
my_set = set()

# 2. Add your name, age, and country as separate elements into the set
# (Remember: sets can hold mixed data types)
# Example: my_set.add('Kenya')
# Add your own data below
my_set.add("Martin")
my_set.add(20)
my_set.add("Kenya")

# 3. Add multiple items at once using update()
# Example: my_set.update(['Python', 'JavaScript', 'C++'])
my_set.update(["Mato",19,"Uganda",'C++'])


# 4. Remove one element from the set using remove()
# Example: my_set.remove('C++')
my_set.remove('C++')

# 5. Use discard() to delete an element that may not exist in the set
# Example: my_set.discard('PHP')  # should not raise an error
my_set.discard('PHP')

# ---------------------------------------------------------------------
# LEVEL 2 ASSIGNMENT
# ---------------------------------------------------------------------

# Given sets for numerical operations
X = {1, 2, 3, 4, 5}
Y = {4, 5, 6, 7, 8}

# 1. Find the union of X and Y and store it in 'union_XY'
union_XY = X.union(Y)  # or X | Y
print(f"1. Union (X | Y): {union_XY}")

# 2. Find the intersection of X and Y and store it in 'intersection_XY'
# Correction: The variable name was mistyped as 'y' instead of 'Y' in your original code.
intersection_XY = X.intersection(Y)  # or X & Y
print(f"2. Intersection (X & Y): {intersection_XY}")

# 3. Check if X is a subset of Y and store result in 'is_subset'
is_subset = X.issubset(Y)
print(f"3. Is X a subset of Y? {is_subset}")

# 4. Find elements that exist only in X or only in Y (symmetric difference)
symmetric_difference = X.symmetric_difference(Y)  # or X ^ Y
print(f"4. Symmetric Difference (X ^ Y): {symmetric_difference}")

# 5. Delete both X and Y sets from memory after printing their contents
# Print contents before deletion
print(f"5. Deleting sets. X before: {X}, Y before: {Y}")
del X
del Y
# Note: Trying to print X or Y now would raise a NameError.

# ---------------------------------------------------------------------
# LEVEL 3 ASSIGNMENT
# ---------------------------------------------------------------------

# 1. Convert this list into a set and print both lengths
ages = [21, 23, 25, 21, 23, 27, 29, 25]
# Compare the length of the list and the new set.
# Which one is larger and why?

print("list is larger because it allows for duplicates to be stored in /n it and the tuple only allows the storage of non duplicate fields")

age_set=set(ages)
print ("the lengt of list ages is ",len(ages))
print ("the lengt of list converted to tupple ages  is ",len(age_set))

# print("Lenght is list > set ",len(ages)>len(age_set))
# 2. Create a sentence and count how many unique words appear
# done with the help of ai
sentence = 'Data science is fun and data analysis is powerful.'

# Use lower() and split()
words_list = sentence.lower().split()

# Convert to set and count unique words
unique_words_set = set(words_list)
unique_word_count = len(unique_words_set)

print(f"Original sentence: '{sentence}'")
print(f"List of all words: {words_list}")
print(f"Set of unique words: {unique_words_set}")
print(f"Total unique words: {unique_word_count}")


# ---------------------------------------------------------------------
# LEVEL 3 ASSIGNMENT - PART 3
# ---------------------------------------------------------------------

# 3. Write a short note (as comments) explaining:
#    - When to use a list
#    - When to use a tuple
#    - When to use a set

# --- List Use Case ---
# Use a **list** when you need a sequence of items that requires ordering 
# (indexed data) and needs to be **mutable** (able to add, remove, or change elements).
# Lists are best for collections where duplicates are allowed and the order matters, 
# such as a shopping cart or a queue of tasks.

# --- Tuple Use Case ---
# Use a **tuple** when you need a fixed collection of items that should be **immutable** # (read-only and cannot be changed after creation). 
# Tuples are often used for coordinates (x, y), database records, or returning multiple 
# values from a function, as their fixed nature makes them safer and faster than lists.

# --- Set Use Case ---
# Use a **set** when you need a collection of items that must be **unique** (no duplicates) 
# and **unordered**. 
# Sets are ideal for quickly checking for membership, eliminating duplicate entries 
# from a list, or performing mathematical operations like union and intersection.


# =====================================================================
# END OF ASSIGNMENT
# =====================================================================
