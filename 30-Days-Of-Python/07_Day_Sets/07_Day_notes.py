# =====================================================================
# 30 Days Of Python: Day 7 - Sets
# =====================================================================

# Initial data provided for the exercises
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# =====================================================================
# Exercises: Level 1
# =====================================================================

print("--- Level 1 Exercises ---")

# 1. Find the length of the set it_companies
print(f"1. Length of it_companies: {len(it_companies)}")

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(f"2. it_companies after adding 'Twitter': {it_companies}")

# 3. Insert multiple IT companies at once to the set it_companies
new_companies = ['Tencent', 'Netflix', 'Salesforce']
it_companies.update(new_companies)
print(f"3. it_companies after update: {it_companies}")

# 4. Remove one of the companies from the set it_companies
# We will use .remove() here, assuming 'Netflix' is in the set
it_companies.remove('Netflix')
print(f"4. it_companies after remove('Netflix'): {it_companies}")

# 5. What is the difference between remove and discard
print("\n5. Difference between remove() and discard():")
print("   - remove(): Removes the specified item. If the item is NOT found, it raises a KeyError.")
print("   - discard(): Removes the specified item. If the item is NOT found, it does nothing (no error is raised).")

# Example of discard (will not raise an error even if the item is not present)
it_companies.discard('NonExistentCompany')
print("   - Tried discard('NonExistentCompany'): No error raised.")

# Example of remove (would raise a KeyError if uncommented and run again)
# it_companies.remove('Netflix') # This company was already removed above, so running this would cause an error
# print("   - remove('Netflix') would raise a KeyError here.")


# =====================================================================
# Exercises: Level 2
# =====================================================================

print("\n--- Level 2 Exercises ---")

# 1. Join A and B
# Using union() to create a new set with all unique elements from A and B
C = A.union(B)
print(f"1. A union B (C): {C}")

# 2. Find A intersection B
# Intersection returns items common to both A and B
intersection_AB = A.intersection(B)
print(f"2. A intersection B: {intersection_AB}")

# 3. Is A subset of B
# Checks if all items in A are also present in B
is_subset = A.issubset(B)
print(f"3. Is A subset of B? {is_subset}") # True

# 4. Are A and B disjoint sets
# Checks if the two sets have NO items in common
is_disjoint = A.isdisjoint(B)
print(f"4. Are A and B disjoint sets? {is_disjoint}") # False (they have many common items)

# 5. Join A with B and B with A
# Note: update() modifies the set in place. We will use copies to preserve original A and B.
A_copy = A.copy()
B_copy = B.copy()

A_copy.update(B) # Joins B into A_copy
B_copy.update(A) # Joins A into B_copy
print(f"5. A joined with B (using update on A_copy): {A_copy}")
print(f"5. B joined with A (using update on B_copy): {B_copy}")
# Since they are sets, the results A_copy and B_copy will be the same (union).

# 6. What is the symmetric difference between A and B
# Symmetric difference returns elements that are in A OR B, but NOT in both
symmetric_diff = A.symmetric_difference(B)
print(f"6. Symmetric difference between A and B: {symmetric_diff}")

# 7. Delete the sets completely
del A
del B
# Trying to print A or B now would result in a NameError.
print("7. Sets A and B have been deleted using 'del'.")


# =====================================================================
# Exercises: Level 3
# =====================================================================

print("\n--- Level 3 Exercises ---")

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_list_len = len(age)
age_set = set(age)
age_set_len = len(age_set)

print(f"1. Original age list: {age}")
print(f"   Length of list: {age_list_len}")
print(f"   Ages converted to set: {age_set}")
print(f"   Length of set: {age_set_len}")
print(f"   Comparison: The list (Length {age_list_len}) is bigger/longer than the set (Length {age_set_len}) because the set removes duplicate items.")

# 2. Explain the difference between the following data types: string, list, tuple and set
print("\n2. Data Type Differences:")
print("   - String (str): IMMUTABLE sequence of characters, used for text.")
print("   - List (list): MUTABLE sequence of items (can be mixed types). Ordered and indexed. Uses [].")
print("   - Tuple (tuple): IMMUTABLE sequence of items. Ordered and indexed. Uses ().")
print("   - Set (set): MUTABLE collection of UNIQUE items. Unordered and un-indexed. Used for membership testing and eliminating duplicates. Uses {}.")

# 3. How many unique words have been used in the sentence?
# Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people.'
# Clean the sentence: remove the period and convert to lowercase
cleaned_sentence = sentence.replace('.', '').lower()
# Split the sentence into a list of words
words_list = cleaned_sentence.split()
# Convert the list of words to a set to get unique words
unique_words = set(words_list)
unique_word_count = len(unique_words)

print(f"\n3. Sentence: '{sentence}'")
print(f"   List of words: {words_list}")
print(f"   Set of unique words: {unique_words}")
print(f"   Total unique words used: {unique_word_count}")

# =====================================================================
# END OF DAY 7 CHALLENGES
# =====================================================================