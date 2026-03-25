from datetime import date

username = input("Enter your username: ")
age = int(input("Enter your age: "))
print(f"Name, age: {username} {age}")
print(f"{username} year of birth is {date.today().year - age}")
