# 30 DAYS OF PYTHON: DAY 6 - TUPLES
# Author: Asabeneh Yetayeh
# Source: Day 6 Notes (Tuples)

# ===============================================================================
## TUPLES - ORDERED AND IMMUTABLE COLLECTIONS
# ===============================================================================

# A tuple is a collection of different data types that is ORDERED and UNCHANGEABLE (immutable).
# Tuples are written with round brackets: ().
# Since tuples are immutable, they do NOT support methods like add, insert, or remove.

# -------------------------------------------------------------------------------
### Creating a Tuple
# -------------------------------------------------------------------------------

# Syntax 1: Using the tuple literal (preferred)
empty_tuple = ()

# Syntax 2: Using the tuple constructor
empty_tuple = tuple()

# Tuple with initial values (can hold different data types)
tpl = ('item1', 'item2', 'item3')
fruits = ('banana', 'orange', 'mango', 'lemon')
print("Example Tuple:", fruits)

# -------------------------------------------------------------------------------
### Tuple Length
# -------------------------------------------------------------------------------

# Use the len() built-in function to get the number of items in a tuple.
print("Length of fruits tuple:", len(fruits)) # Output: 4

# -------------------------------------------------------------------------------
### Accessing Tuple Items
# -------------------------------------------------------------------------------

# Positive Indexing (starts at 0)
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]
print("First item:", first_item) # Output: item1

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
last_index = len(fruits) - 1
last_fruit_pos = fruits[last_index]
print("Last item via positive index:", last_fruit_pos) # Output: lemon

# Negative Indexing (starts at -1 from the end)
tpl = ('item1', 'item2', 'item3', 'item4')
first_item_neg = tpl[-4] # The negative of the length refers to the first item
last_item_neg = tpl[-1]
print("First item via negative index:", first_item_neg) # Output: item1
print("Last item via negative index:", last_item_neg) # Output: item4

# -------------------------------------------------------------------------------
### Slicing Tuples
# -------------------------------------------------------------------------------

# Slicing extracts a sub-tuple: tpl[start:stop:step]. 'stop' index is exclusive.

# Range of Positive Indexes
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[0:4]   # All items
all_items_short = tpl[0:] # All items (omitting 'stop' defaults to the end)
middle_two_items = tpl[1:3] # Items at index 1 and 2 ('item2', 'item3')

fruits = ('banana', 'orange', 'mango', 'lemon')
orange_mango = fruits[1:3]
print("Sliced fruits (orange and mango):", orange_mango) # Output: ('orange', 'mango')

# Range of Negative Indexes
tpl = ('item1', 'item2', 'item3', 'item4')
all_items_neg = tpl[-4:] # All items
# Slices from -3 ('item2') up to (but not including) -1 ('item4')
middle_two_items_neg = tpl[-3:-1]
print("Sliced by negative index:", middle_two_items_neg) # Output: ('item2', 'item3')

orange_to_the_rest = fruits[-3:]
print("Sliced from -3 to end:", orange_to_the_rest) # Output: ('orange', 'mango', 'lemon')

# -------------------------------------------------------------------------------
### Changing Tuples to Lists (To enable modification)
# -------------------------------------------------------------------------------

# Tuples are immutable. To modify them (e.g., replace an item), they must be converted to a list first.
fruits_tpl = ('banana', 'orange', 'mango', 'lemon')
fruits_list = list(fruits_tpl)

# Modification is now possible on the list
fruits_list[0] = 'apple'
print("Modified List:", fruits_list) # Output: ['apple', 'orange', 'mango', 'lemon']

# Convert back to a tuple if needed
fruits_tpl = tuple(fruits_list)
print("Converted back to Tuple:", fruits_tpl) # Output: ('apple', 'orange', 'mango', 'lemon')

# -------------------------------------------------------------------------------
### Checking an Item in a Tuple
# -------------------------------------------------------------------------------

# Use the 'in' operator; it returns a boolean (True or False).
tpl = ('item1', 'item2', 'item3', 'item4')
print("'item2' in tpl:", 'item2' in tpl) # Output: True
print("'apple' in fruits:", 'apple' in fruits_tpl) # Output: True (based on the last modification)

# -------------------------------------------------------------------------------
### Joining Tuples
# -------------------------------------------------------------------------------

# Use the '+' operator to join two or more tuples, creating a NEW tuple.
tpl1 = ('item1', 'item2')
tpl2 = ('item3', 'item4')
tpl3 = tpl1 + tpl2
print("Joined Tuple:", tpl3) # Output: ('item1', 'item2', 'item3', 'item4')

vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
fruits_and_vegetables = fruits_tpl + vegetables
print("Fruits and Veggies Tuple:", fruits_and_vegetables)

# -------------------------------------------------------------------------------
### Deleting Tuples
# -------------------------------------------------------------------------------

# You cannot remove a single item from a tuple.
# You can delete the entire tuple object using the 'del' keyword.
tpl_to_delete = ('a', 'b', 'c')
del tpl_to_delete
# print(tpl_to_delete) # This would result in a NameError

# ===============================================================================
## 💻 EXERCISES: DAY 6
# ===============================================================================

### Exercises: Level 1

# 1. Create an empty tuple
empty_tpl = tuple()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Alice', 'Betty')
brothers = ('Charlie', 'David', 'Edward')

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers

# 4. How many siblings do you have?
print("Total number of siblings:", len(siblings))

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('Father', 'Mother')
# Note: Tuples must be joined; simply concatenating (parents + siblings) creates the desired new tuple.
family_members = siblings + parents
print("Family Members:", family_members)

# -------------------------------------------------------------------------------
### Exercises: Level 2

# 1. Unpack siblings and parents from family_members
# We need 5 variables for siblings and 2 for parents. Total 7 variables.
sibling1, sibling2, sibling3, sibling4, sibling5, father, mother = family_members
print("Unpacked Sibling 1:", sibling1)
print("Unpacked Mother:", mother)

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits_tp = ('apple', 'orange', 'grape')
vegetables_tp = ('carrot', 'broccoli', 'spinach')
animal_products_tp = ('milk', 'eggs', 'cheese')
food_stuff_tp = fruits_tp + vegetables_tp + animal_products_tp
print("Food Stuff Tuple:", food_stuff_tp)

# 3. Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("Food Stuff List:", food_stuff_lt)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# The list has 9 items (indices 0 to 8). The middle item is at index 4.
middle_item = food_stuff_tp[4]
print("Middle item:", middle_item)

# 5. Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First three items:", first_three)
print("Last three items:", last_three)

# 6. Delete the food_stuff_tp tuple completely
del food_stuff_tp
# print(food_stuff_tp) # Would now cause a NameError

# 7. Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
print("'Estonia' is a nordic country:", 'Estonia' in nordic_countries)

# Check if 'Iceland' is a nordic country
print("'Iceland' is a nordic country:", 'Iceland' in nordic_countries)