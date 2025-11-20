"""
Assignment 2 - Question 3
Determine a person's age from their birthdate in DD/MM/YYYY format.
"""

from datetime import datetime

def find_age(birthdate_str):
    """Return the age based on a birthdate string in DD/MM/YYYY format."""

    if not isinstance(birthdate_str, str):
        raise TypeError("Birthdate must be provided as a string.")
    
    # Attempt to convert the string into a date object
    try:
        birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")
    except ValueError:
        raise ValueError("Invalid date or format. Use DD/MM/YYYY.")

    today = datetime.today()
    age = today.year - birthdate.year

    # Adjust if the birthday hasn't ocurred yet this year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1

    return age

# Get and validate user input
user_input = input("Enter your birthday (DD/MM/YYYY): ")

try:
    age = find_age(user_input)
    print(f"You are {age} years old.")
except Exception as e:
    print("Error:", e)