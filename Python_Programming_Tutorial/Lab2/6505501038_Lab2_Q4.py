def calculate_student_scores():
    while True:
        try:
            num_students_str = input("Number of students : ")
            num_students = int(num_students_str)
            if num_students <= 0:
                print("Incorrect Input. Number of students : ", end="")
            else:
                break
        except ValueError:
            print("Incorrect Input. Number of students : ", end="")

    scores = []
    for i in range(num_students):
        while True:
            try:
                score_str = input(f"Student {i + 1} : ")
                score = float(score_str)
                scores.append(score)
                break
            except ValueError:
                print("Invalid score. Please enter a number.")

    if not scores:
        print("No scores entered.")
        return

    # Overall average score
    average_score = sum(scores) / len(scores)

    # Passing and Failing scores
    passing_scores = [s for s in scores if s >= 5]
    failing_scores = [s for s in scores if s < 5]

    average_passing_score = (
        sum(passing_scores) / len(passing_scores) if passing_scores else None
    )
    average_failing_score = (
        sum(failing_scores) / len(failing_scores) if failing_scores else None
    )

    # Highest score
    highest_score = max(scores)

    print(f"Average score : {average_score}")
    if average_passing_score is not None:
        print(f"Average passing score : {average_passing_score}")
    else:
        print("Average passing score : No student passed")

    if average_failing_score is not None:
        print(f"Average failing score : {average_failing_score}")
    else:
        print("Average failing score : No student failed")

    print(f"Highest score : {highest_score}")


calculate_student_scores()
