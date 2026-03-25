total_score = 0

while True:
    try:
        num_students = int(input("Number of students : "))
        if num_students >= 0:
            break
        else:
            print("Incorrect Input. Number of students must be non-negative.")
    except ValueError:
        print("Incorrect Input. Please enter an integer for the number of students.")

for i in range(1, num_students + 1):
    while True:
        try:
            score = float(input(f"Student {i} : "))
            total_score += score
            break
        except ValueError:
            print("Incorrect Input. Please enter a valid number for the score.")

print(f"Total score : {total_score}")
