## 1. Creating Lists and Checking Length

# Lists are defined using square brackets [].
empty_list = list()                 # Method 1: Creates an empty list using the list() constructor. But it is not the convectional way of creating lists
print(len(empty_list))              # Output: 0. The len() function checks the number of items in the list.

# Lists are usually defined using square brackets. They can hold different data types.
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
animal_products = ['milk', 'meat', 'butter', 'yoghurt']
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and their length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))              # Output: 4
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))      # Output: 5
print('Animal products:', animal_products)
print('Number of animal products:', len(animal_products)) # Output: 4
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))  # Output: 7
print('Number of countries:', len(countries))        # Output: 5

# ---

## 2. Accessing Items (Indexing)

# Accessing items using positive indices (starts from 0)
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]             # Accesses the item at index 0 ('banana').
print(first_fruit)                  # Output: banana
second_fruit = fruits[1]
print(second_fruit)                 # Output: orange
last_fruit = fruits[3]
print(last_fruit)                   # Output: lemon

# Calculating the last index manually (Length - 1)
last_index = len(fruits) - 1
last_fruit = fruits[last_index]     # Accesses the item at the calculated index (4 - 1 = 3).
print(last_fruit)                   # Output: lemon

# Accessing items using negative indices (starts from -1)
fruits = ['banana', 'orange', 'mango', 'lemon']
last_fruit = fruits[-1]             # Accesses the last item directly.
print(last_fruit)                   # Output: lemon
second_last = fruits[-2]            # Accesses the second-to-last item.
print(second_last)                  # Output: mango

# ---

## 3. Slicing Items

# Slicing extracts a section of the list using [start:stop:step]. The 'stop' index is exclusive.
fruits = ['banana', 'orange', 'mango', 'lemon']

# Slicing to get all items: [0:end]
all_fruits = fruits[0:4]            # Slices from index 0 up to (but not including) 4.
all_fruits = fruits[0:]             # Omitting the 'stop' index defaults to the end of the list.
all_fruits = fruits[:]              # Another way to copy the entire list.

# Slicing a specific range
orange_and_mango = fruits[1:3]      # Slices from index 1 up to (but not including) 3 -> ['orange', 'mango']
print(orange_and_mango)             # Output: ['orange', 'mango']

orange_mango_lemon = fruits[1:]     # Slices from index 1 to the end -> ['orange', 'mango', 'lemon']
print(orange_mango_lemon)           # Output: ['orange', 'mango', 'lemon']

# Slicing using negative indices
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:]            # Slices from the 4th item from the end to the end (the whole list).

# Slices from -3 ('orange') up to (but not including) -1 ('lemon') -> ['orange', 'mango']
orange_and_mango = fruits[-3:-1]
print(orange_and_mango)             # Output: ['orange', 'mango']

# Slices from -3 ('orange') to the end -> ['orange', 'mango', 'lemon']
orange_mango_lemon = fruits[-3:]
print(orange_mango_lemon)           # Output: ['orange', 'mango', 'lemon']

# ---

## 4. Modifying and Replacing Items

fruits = ['banana', 'orange', 'mango', 'lemon']
# Lists are mutable, meaning their contents can be changed after creation.
fruits[0] = 'Avocado'               # Replaces the item at index 0 ('banana') with 'Avocado'.
# NOTE: Corrected case in output comment to match assignment ('Avocado').
print(fruits)                       # Output: ['Avocado', 'orange', 'mango', 'lemon']

fruits[1] = 'apple'                 # Replaces the item at index 1 ('orange').
print(fruits)                       # Output: ['Avocado', 'apple', 'mango', 'lemon']

last_index = len(fruits) - 1
fruits[last_index] = 'lime'         # Replaces the last item using calculated index.
print(fruits)                       # Output: ['Avocado', 'apple', 'mango', 'lime']

# ---

## 5. Checking for Item Existence

fruits = ['banana', 'orange', 'mango', 'lemon']
# The 'in' operator checks if an item is present in the list (returns a boolean).
does_exist = 'banana' in fruits
print(does_exist)                   # Output: True
does_exist = 'lime' in fruits
print(does_exist)                   # Output: False

# ---

## 6. Adding Items (Append and Insert)

# append(): Adds a single item to the END of the list.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)                       # Output: ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')
print(fruits)                       # Output: ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']

# insert(): Inserts an item at a specific index. Syntax: list.insert(index, item)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple')           # Inserts 'apple' at index 2 (between 'orange' and 'mango').
print(fruits)                       # Output: ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')            # Inserts 'lime' at index 3 (between 'apple' and 'mango').
print(fruits)                       # Output: ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']

# ---

## 7. Removing Items (Remove, Pop, Del, Clear)

# remove(): Removes the FIRST occurrence of a specified item by its VALUE.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)                       # Output: ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits)                       # Output: ['orange', 'mango']

# pop(): Removes and RETURNS an item based on its INDEX. If no index is given, removes and returns the LAST item.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()                        # Removes 'lemon' (the last item).
print(fruits)                       # Output: ['banana', 'orange', 'mango']
fruits.pop(0)                       # Removes the item at index 0 ('banana').
print(fruits)                       # Output: ['orange', 'mango']

# del: Removes items by index or deletes the entire list variable.
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]                       # Deletes the item at index 0.
print(fruits)                       # Output: ['orange', 'mango', 'lemon']

del fruits[1]                       # Deletes the item at index 1 ('mango').
print(fruits)                       # Output: ['orange', 'lemon']

del fruits                          # Deletes the entire 'fruits' variable from memory.
# print(fruits)                     # This line would cause a NameError: name 'fruits' is not defined

# clear(): Empties the list, leaving an empty list ([]) object.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)                       # Output: []

# ---

## 8. Copying and Joining Lists

# copy(): Creates a true copy (a new list object) to prevent unintended modification of the original.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)                  # Output: ['banana', 'orange', 'mango', 'lemon']

# Joining lists using the '+' operator (Creates a new list)
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)                     # Output: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)        # Output: combined list

# Joining lists with extend() (Modifies the first list in place)
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)                   # Appends all items from num2 to the end of num1.
print('Numbers:', num1)             # Output: [0, 1, 2, 3, 4, 5, 6]

negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers.extend(zero)       # Modifies negative_numbers: [-5, ..., -1, 0]
negative_numbers.extend(positive_numbers) # Modifies negative_numbers: [-5, ..., 5]
print('Integers:', negative_numbers)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.extend(vegetables)           # Modifies fruits list by adding vegetables.
print('Fruits and vegetables:', fruits)

# ---

## 9. Other Useful List Methods (Count, Index, Reverse, Sort)

# count(): Returns the number of times a specified item appears in the list.
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))       # Output: 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))               # Output: 3

# index(): Returns the index of the FIRST occurrence of a specified item. Raises a ValueError if not found.
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))       # Output: 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))               # Output: 2 (The first occurrence of 24 is at index 2)

# reverse(): Reverses the order of the items in the list IN PLACE (modifies the original list).
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)                       # Output: ['lemon', 'mango', 'orange', 'banana']

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)                         # Output: [24, 25, 24, 26, 25, 24, 19, 22]

# sort(): Sorts the list items IN PLACE (modifies the original list). Default is ascending (alphabetical/numerical).
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()                       # Sorts alphabetically (ascending).
print(fruits)                       # Output: ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)           # Sorts in descending order.
print(fruits)                       # Output: ['orange', 'mango', 'lemon', 'banana']

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()                         # Sorts numerically (ascending).
print(ages)                         # Output: [19, 22, 24, 24, 24, 25, 25, 26]
ages.sort(reverse=True)             # Sorts in descending order.
print(ages)                         # Output: [26, 25, 25, 24, 24, 24, 22, 19]