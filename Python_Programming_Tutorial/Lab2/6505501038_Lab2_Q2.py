attempts = 0
name = input("Enter username : ")
while name != "Lisa":
    attempts += 1
    if attempts == 3:
        print("Not allowed. Incorrect name.")
        break
    name = input("Incorrect. Enter again : ")
else:
    print("Hello,", name)
