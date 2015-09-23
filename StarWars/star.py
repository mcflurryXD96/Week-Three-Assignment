# Daniel McMurray
# starwars.py
# Week 3 Star Wars Name Translation

# Prompt User for first name, last name, mother's maiden name, and name of birth City

firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
maiden = input("Enter your mother's maiden name: ")
city = input("Enter the name of the city in which you were born: ")

# Calculate and print the user's Star Wars name

print(lastname[0:3]+firstname[0:2], maiden[0:2]+city[0:3])
