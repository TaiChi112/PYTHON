from datetime import date

username = input("Enter your username: ")
age = int(input("Enter your age: "))
calculate_birth_year = date.today().year - age
email = (
    username
    + str(calculate_birth_year)[-2]
    + str(calculate_birth_year)[-1]
    + "@rumail.ru.ac.th"
)
print(f"Name: {username}")
print(f"Age: {age}")
print(f"{email}")
