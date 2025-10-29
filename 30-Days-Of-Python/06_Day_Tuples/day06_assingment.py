# =====================================================================
# ASSIGNMENT: DAY 6 - TUPLES
# =====================================================================

# 1. Create an empty tuple named 'empty_tuple'
# Tuples are written using round brackets ().
# Example: my_tuple = ()
# Use either () or tuple() constructor to make an empty tuple.
# Print it to confirm the result.
empty_tuple=()
print("empty tupple :",empty_tuple)

# 2. Create two tuples: one for sisters and one for brothers.
# Each tuple should contain at least two string names.
# Example: sisters = ('Mary', 'Jane'), brothers = ('Tom', 'Alex')
# Print both tuples to confirm they were created correctly.

brothers=("John","James","Mato")
sisters=("Mary","Helen","Njoki")
print("tupple containing brothers details is :",brothers)
print("tupple containing  sisters names is :",sisters)

# 3. Join the two tuples into a single tuple called 'siblings'.

# Use the + operator to combine them.
# Example: siblings = sisters + brothers
# Print the new tuple and verify it includes all names.
siblings=brothers+sisters

print("this is the combined tupple including all the siblings names :",siblings)

# 4. Find and print the total number of siblings.
# Use the len() function to count how many elements are inside 'siblings'.
# Example: print(len(siblings))
print(len(siblings))

# 5. Create a 'parents' tuple with two names: your father and mother.
# Join the 'parents' tuple with the 'siblings' tuple to form a new tuple called 'family_members'.
# Example: family_members = siblings + parents
# Print the 'family_members' tuple to confirm it contains all names.
parents=("Samwna","samwananangina")
family_members=siblings+parents
print("the family members are :",family_members)

# 6. Unpack all items from 'family_members' into individual variables.
# Assign each element of the tuple to a variable, e.g., 
# sibling1, sibling2, sibling3, sibling4, father, mother = family_members
# Then print at least two variables (for example, print your first sibling and your mother) to confirm.
sibling1,sibling2,sibling3,sibling4,sibling5,sibling6,father,mother=family_members

print("Mother and one siblings are ",mother+" "+sibling1)

# 7. Create three tuples named:
#    fruits (e.g., 'apple', 'banana', 'mango')
#    vegetables (e.g., 'carrot', 'broccoli', 'spinach')
#    animal_products (e.g., 'milk', 'cheese', 'eggs')
# These tuples should each contain at least three items.
# Print each tuple to confirm.
fruits=('apple','banana','mango')
vegetables=('carrot','brocoli','spinach')
animal_products= ('milk',"cheese",'eggs')

print("the tuple created for fruits contains:",fruits)
print("the tuple created for vegetables contains:",vegetables)
print("the tuple created for animal products contains:",animal_products)

# 8. Join the three tuples created above into one tuple named 'food_stuff_tp'.
# Use the + operator to combine them.
# Example: food_stuff_tp = fruits + vegetables + animal_products
# Print the result to verify the combined tuple.
food_stuff_tp=fruits+vegetables+animal_products
print("the combined tuple containing the food stufs is :",food_stuff_tp)

# 9. Convert 'food_stuff_tp' into a list named 'food_stuff_lt'.
# Use the list() constructor to change it into a list.
# Example: food_stuff_lt = list(food_stuff_tp)
# Print both the tuple and the list to see the difference.
food_stuff_lt=list(food_stuff_tp)
print("the tupple before conversion is :",food_stuff_tp)
print("the list after the tuple conversion is :",food_stuff_lt)

# 10. Slice out the middle item (or items) from 'food_stuff_tp'.
# First, find the total length using len().
# If the length is odd, there will be one middle item. If even, two middle items.
# Use slicing to extract the middle item(s) and print the result.
print("leght of list created is ",len(food_stuff_tp))
length = len(food_stuff_tp) # 9
middle_index = length // 2 # 4
middle_item = food_stuff_tp[middle_index:middle_index + 1]
print("Middle Item:", middle_item) # ('spinach',)

# 11. Slice and print the first three and last three items from 'food_stuff_lt'.
# Use slicing with positive and negative indices.
# Example: first_three = food_stuff_lt[:3], last_three = food_stuff_lt[-3:]
# Print both slices.
first_3=food_stuff_lt[:3]
print("the first 3 in the tupple are :",first_3)

last_3=food_stuff_lt[-3:]
print('the last three elements in the tupple are :',last_3)
# 12. Delete the 'food_stuff_tp' tuple completely.
# Use the del keyword to delete it from memory.
# Example: del food_stuff_tp
# Try to print it afterward (commented out) to see that it causes a NameError.
del food_stuff_tp

# 13. Create a tuple named 'nordic_countries'.
# It should contain these five countries:
# 'Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden'
# Print the tuple to confirm.
nordic_countries=('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('the tuple of normadic countries is :',nordic_countries)

# 14. Check if 'Estonia' exists in the nordic_countries tuple.
# Use the 'in' keyword for membership checking.
# Example: print('Estonia' in nordic_countries)
# The result should be False.   
print("Estonia" in nordic_countries)


# 15. Check if 'Iceland' exists in the nordic_countries tuple.
# Again use the 'in' keyword.
# Example: print('Iceland' in nordic_countries)
# The result should be True.
print("Iceland" in nordic_countries)
