def check_quadratic_formula_conditions():
    try:
        # Prompt the user to enter coefficients a, b, c as a comma-separated string
        input_str = input("Enter coefficients a, b, c : ")
        a_str, b_str, c_str = input_str.split(",")

        # Convert string inputs to float numbers
        a = float(a_str.strip())
        b = float(b_str.strip())
        c = float(c_str.strip())

        # Initialize can_use to False
        can_use = False

        # Condition 1: a must not be zero
        if a != 0:
            # Calculate the discriminant (b^2 - 4ac)
            discriminant = b**2 - 4 * a * c

            # Condition 2: discriminant must be non-negative
            if discriminant >= 0:
                can_use = True

        # Print the result
        print(f"Can use quadratic formula: {can_use}")

    except ValueError:
        print(
            "Invalid input. Please enter three comma-separated numbers (e.g., 1,4,3 or 2.3,-1.5,1.5)."
        )
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Call the function to run the check
check_quadratic_formula_conditions()
