
# Variables in Python

first_name = 'Asabeneh'  #assings the name Asabeneh to the variable first_name

last_name = 'Yetayeh' #assings the name Yetayeh to the variable last_name
country = 'Finland'       #assings the country Finland to the variable country
city = 'Helsinki'         #assings the city Helsinki to the variable city
age = 250           #assings the age 250 to the variable age    
is_married = True      #assings the boolean value True to the variable is_married
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']   #assings a list of skills to the variable skills
person_info = {
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki'
    }  #assings a dictionary with personal information to the variable person_info
#first_name, last_name, country, city, age, is_married, skills    unaer the variable person_info

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)