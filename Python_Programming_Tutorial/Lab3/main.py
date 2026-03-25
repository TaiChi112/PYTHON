from __future__ import annotations

import math


def circle_relation(
    c1: tuple[float, float, float], c2: tuple[float, float, float]
) -> str:
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    sum_r = r1 + r2

    if math.isclose(d, sum_r, rel_tol=1e-9, abs_tol=1e-9):
        return "touch"
    if d < sum_r:
        return "overlap"
    return "free"


def run_circle_detector() -> None:
    print("--- Circle Overlap Detector ---")
    x1, y1, r1 = map(float, input("Enter x, y, and radius for Circle 1: ").split())
    x2, y2, r2 = map(float, input("Enter x, y, and radius for Circle 2: ").split())
    print(circle_relation((x1, y1, r1), (x2, y2, r2)))


def fuel_required(distance: float, car_type: int, driving_pattern: int) -> float:
    rates = {
        (1, 1): 12,
        (1, 2): 10,
        (2, 1): 10,
        (2, 2): 8,
        (3, 1): 9,
        (3, 2): 7,
    }
    if (car_type, driving_pattern) not in rates:
        raise ValueError("Invalid car type or driving pattern")
    return distance / rates[(car_type, driving_pattern)]


def run_fuel_calculator() -> None:
    print("--- Fuel Calculator ---")
    distance = float(input("Enter travel distance (km.): "))
    car_type = int(input("Enter the type of car: "))
    driving_pattern = int(input("Enter driving pattern: "))

    try:
        fuel = fuel_required(distance, car_type, driving_pattern)
        print(f"Fuel required: {fuel:.2f} litres.")
    except ValueError:
        print("Invalid input")


def count_correct_answers(correct: str, student: str) -> int:
    return sum(c.lower() == s.lower() for c, s in zip(correct, student))


def run_answer_checker() -> None:
    print("--- Multiple Choice Answer Checker ---")
    while True:
        correct = input("Enter the correct answers (type 'exit' to quit): ").strip()
        if correct.lower() == "exit":
            print("Exiting program. Goodbye!")
            break

        student = input("Enter the student's answers: ").strip()
        if len(correct) != len(student):
            print("Incomplete answer")
            continue

        correct_count = count_correct_answers(correct, student)
        print(f"Number of correct answers: {correct_count}")


def calculate_checksum_digit(thai_id: str) -> int:
    first_12 = [int(d) for d in thai_id[:12]]
    weighted_sum = sum(d * w for d, w in zip(first_12, range(13, 1, -1)))
    return (11 - (weighted_sum % 11)) % 10


def run_checksum_calculator() -> None:
    print("--- ID Checksum Calculator ---")
    thai_id = input("Enter 13-digit ID number: ").strip()

    if len(thai_id) != 13 or not thai_id.isdigit():
        print("Invalid ID number")
        return

    checksum = calculate_checksum_digit(thai_id)
    print(f"Calculated checksum digit: {checksum}")


def main() -> None:
    while True:
        print("\n=== Extra Assignment Menu ===")
        print("1) Circle Overlap Detector")
        print("2) Fuel Required Calculator")
        print("3) Multiple Choice Answer Checker")
        print("4) Thai ID Checksum Calculator")
        print("5) Exit")
        choice = input("Select option: ").strip()

        if choice == "1":
            run_circle_detector()
        elif choice == "2":
            run_fuel_calculator()
        elif choice == "3":
            run_answer_checker()
        elif choice == "4":
            run_checksum_calculator()
        elif choice == "5":
            print("Bye")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
