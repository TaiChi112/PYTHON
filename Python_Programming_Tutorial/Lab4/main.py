from __future__ import annotations


def cut_deck(cards: list[str]) -> list[str]:
    half = len(cards) // 2
    return cards[half:] + cards[:half]


def riffle_deck(cards: list[str]) -> list[str]:
    half = len(cards) // 2
    front = cards[:half]
    back = cards[half:]

    mixed: list[str] = []
    for a, b in zip(front, back):
        mixed.append(a)
        mixed.append(b)
    return mixed


def run_cards_task() -> None:
    print("\n=== Task 1: Cut / Riffle ===")
    raw = input("Enter cards separated by spaces: ").strip()
    cards = raw.split()

    if len(cards) == 0 or len(cards) % 2 != 0:
        print("Please provide an even number of cards.")
        return

    print("Original:", " ".join(cards))
    print("Cut     :", " ".join(cut_deck(cards)))
    print("Riffle  :", " ".join(riffle_deck(cards)))


def run_list_comprehension_task() -> None:
    print("\n=== Task 2: List Comprehension ===")
    points = [(5, 2), (3, 8), (4, 4), (3, 9), (25, 5), (10, 1), (2, 4), (9, 3)]

    swapped = [(y, x) for x, y in points]
    x_gt_y = [(x, y) for x, y in points if x > y]
    x_lt_y = [(x, y) for x, y in points if x < y]
    x_eq_y = [(x, y) for x, y in points if x == y]
    x2_eq_y = [(x, y) for x, y in points if x**2 == y]
    y2_eq_x = [(x, y) for x, y in points if y**2 == x]

    print("points     =", points)
    print("a) swap    =", swapped)
    print("b) x > y   =", x_gt_y)
    print("c) x < y   =", x_lt_y)
    print("d) x == y  =", x_eq_y)
    print("e) x^2 == y=", x2_eq_y)
    print("f) y^2 == x=", y2_eq_x)


def run_student_dict_task() -> None:
    print("\n=== Task 3: Student Dictionary ===")
    students: dict[str, str] = {}

    while True:
        print("\n1) Add Student")
        print("2) View Student")
        print("3) Update Student")
        print("4) Delete Student")
        print("5) View All Students")
        print("6) Exit")
        option = input("Select option: ").strip()

        if option == "1":
            sid = input("Student ID: ").strip()
            name = input("Full Name: ").strip()
            if sid in students:
                print("Student ID already exists.")
            else:
                students[sid] = name
                print("Student added successfully.")

        elif option == "2":
            sid = input("Student ID: ").strip()
            if sid in students:
                print(students[sid])
            else:
                print("Student ID not found.")

        elif option == "3":
            sid = input("Student ID: ").strip()
            if sid in students:
                new_name = input("New Full Name: ").strip()
                students[sid] = new_name
                print("Student data updated successfully.")
            else:
                print("Student ID not found.")

        elif option == "4":
            sid = input("Student ID: ").strip()
            if sid in students:
                del students[sid]
                print("Student deleted successfully.")
            else:
                print("Student ID not found.")

        elif option == "5":
            if not students:
                print("No student data.")
            else:
                for sid, name in students.items():
                    print(f"{sid}: {name}")

        elif option == "6":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


def show_group(title: str, group: set[str]) -> None:
    ordered = sorted(group)
    print(f"{title}: {len(ordered)} คน")
    print(ordered)


def run_set_analysis_task() -> None:
    print("\n=== Task 4: Set Analysis ===")
    python_set = {"SUPANAT", "TEERAPON", "KAWINWAT", "KIDSAKORN", "PHON", "SURACHAD"}
    java_set = {"PAWARIS", "SUPANAT", "PONGSAKORN", "RATTANACHAT", "PHON", "SURACHAD"}
    cpp_set = {
        "SUPANAT",
        "TEERAPON",
        "KAWINWAT",
        "RATTANACHAT",
        "SURACHAD",
        "MATCHAKAN",
    }

    all_three = python_set & java_set & cpp_set
    only_python = python_set - java_set - cpp_set
    only_java = java_set - python_set - cpp_set
    only_cpp = cpp_set - python_set - java_set
    py_java_only = (python_set & java_set) - cpp_set
    py_cpp_only = (python_set & cpp_set) - java_set
    java_cpp_only = (java_set & cpp_set) - python_set
    at_least_two = (
        (python_set & java_set) | (python_set & cpp_set) | (java_set & cpp_set)
    )

    show_group("1) ครบทั้ง 3 วิชา", all_three)
    show_group("2) เฉพาะ Python", only_python)
    show_group("3) เฉพาะ Java", only_java)
    show_group("4) เฉพาะ C++", only_cpp)
    show_group("5) Python และ Java เท่านั้น", py_java_only)
    show_group("6) Python และ C++ เท่านั้น", py_cpp_only)
    show_group("7) Java และ C++ เท่านั้น", java_cpp_only)
    show_group("8) อย่างน้อย 2 วิชาขึ้นไป", at_least_two)


def main() -> None:
    while True:
        print("\n=== COS2210 Assignment 3 ===")
        print("1) Task 1: Card Cut/Riffle")
        print("2) Task 2: List Comprehension")
        print("3) Task 3: Student Dictionary")
        print("4) Task 4: Set Analysis")
        print("5) Exit")

        choice = input("Choose task: ").strip()

        if choice == "1":
            run_cards_task()
        elif choice == "2":
            run_list_comprehension_task()
        elif choice == "3":
            run_student_dict_task()
        elif choice == "4":
            run_set_analysis_task()
        elif choice == "5":
            print("Bye")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
