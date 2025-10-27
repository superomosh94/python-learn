# Create personal information variables
first_name = "magna"       # User's first name
last_name = "coder"        # User's last name
age = 30                   # User's age
country = "Kenya"          # User's country
city = "Nairobi"           # User's city
is_student = True          # True if user is a student

# List of top 3 skills
skills = ["html", "css", "javascript"]

# Dictionary with name, city, and country
profile = {
    "name": "magna coder",
    "city": "Nairobi",
    "country": "Kenya"
}

# Combine first and last name
name1 = first_name + " " + last_name

# Print full name
print("Full name:", name1)

# Print name from dictionary
print("Name from dictionary:", profile["name"])

# Print name length
print("Name length:", len(name1))

# Print age and city
print("Age:", age, "City:", city)

# Print first skill
print("First skill:", skills[0])

# Print entire profile dictionary
print("Profile details:", profile)

# Reassign multiple variables in one line with new values
first_name, city, country, age = "senior", "Eldoret", "Uganda", 21

# Print reassigned values
print("Reassigned values are:", first_name, city, country, age)
