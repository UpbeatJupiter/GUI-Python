current_year = 2023

def calculate_age(birth_year):
    return current_year - birth_year

age = calculate_age(1999)
print(f"Function returned {age}")

def print_age(birth_year):
    age = current_year - birth_year
    print(f"Your age is {age}.")

print_age(1997)

