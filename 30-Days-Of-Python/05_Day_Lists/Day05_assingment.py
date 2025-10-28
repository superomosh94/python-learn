## PYTHON LISTS ASSIGNMENT
# Topic: Lists, Indexing, Slicing, and Methods
# Instruction: Write code for each question where indicated. Use the notes as reference.

# ---------------------------------------
# 1. Creating and Checking Length
# ---------------------------------------
# Create three lists: countries, fruits, and web_techs with at least 5 items each.
# Then print each list and its length.

# Write your code below:
countries=["Kenya","Uganda","Nigeria","sudan","algeria"]
fruits=["Mango","Orange","Pawpaw","Tomato","Pear"]
web_techs=["HTML","CSS","Javascript","python","React"]

print("lenght of countries is:",len(countries))
print("lengt of fruits list is ", len(fruits))
print("lenght of web techs is ", len(web_techs))


# ---------------------------------------
# 2. Accessing List Items
# ---------------------------------------
# From your fruits list:
#   - Print the first item
#   - Print the third item
#   - Print the last item using both positive and negative indexing

# Write your code below:
print(fruits[0])
print(fruits[2])
lenght=len(fruits)

print(fruits[-1])




# ---------------------------------------
# 3. Slicing Lists
# ---------------------------------------
# Use slicing to:
#   - Get the first three items of your countries list
#   - Get all items except the first one
#   - Get the last two items using negative indices

# Write your code below:
slice=countries
print("first 3 list elements are :",slice[0:4])
print("This is the list excluding the first elenet in the list :",slice[2:])
print(slice[-2:])


# ---------------------------------------
# 4. Modifying Items
# ---------------------------------------
# Change the second fruit in your list to 'apple'.
# Change the last web technology to 'TypeScript'.

# Write your code below:
fruits[1]="apple"
web_techs_last=len(fruits) -1
fruits[web_techs_last]="TypeScript"


# ---------------------------------------
# 5. Checking Item Existence
# ---------------------------------------
# Check if 'Kenya' exists in your countries list.
# Check if 'React' exists in your web_techs list.

# Write your code below:
print("Kenya" in countries)
print("React" in web_techs)

# ---------------------------------------
# 6. Adding Items
# ---------------------------------------
# Use append() to add a new country to the list.
# Use insert() to add a fruit at index 2.

# Write your code below:
countries.append("tanzania")
print(countries)

fruits.insert(2,"pinapple")
print(fruits)

# ---------------------------------------
# 7. Removing Items
# ---------------------------------------
# Remove one item from your fruits list using remove().
# Remove one item using pop() (try popping index 0).
# Clear your web_techs list completely.

# Write your code below:
print(fruits)
fruits.remove("Mango")
print(fruits)

fruits.pop()
print(fruits)

del web_techs

# ---------------------------------------
# 8. Copying and Joining Lists
# ---------------------------------------
# Copy your fruits list into a new variable.
# Join your countries and fruits lists using '+'.
# Join the two lists again using extend().

# Write your code below:
fruits_copy=fruits.copy()
combo_list=countries+fruits
print("this is a + combo list",combo_list)


apend_list=fruits.extend(countries)
print("this ia an append list :",apend_list)



# ---------------------------------------
# 9. Useful List Methods
# ---------------------------------------
# Create a list of ages = [18, 21, 19, 18, 25, 19, 22, 18].
# Use count() to count how many times 18 appears.
# Use index() to find the first position of 25.
# Reverse the list.
# Sort it in ascending and descending order.

# Write your code below:

ages = [18, 21, 19, 18, 25, 19, 22, 18]
print("count of 18:",ages.count(18))

print("the age using index is :",ages.index(25))
print("this is age list in reversen :",ages.reverse())
print("ascending list :",ages.sort())
print("descending list :",ages.sort(reverse=True))


