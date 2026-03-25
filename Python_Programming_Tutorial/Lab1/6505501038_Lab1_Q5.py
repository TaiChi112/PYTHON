import math

# Get coefficients from user input
coeffs_str = input("Enter coefficients a, b, c (comma-separated): ")
coeffs = [float(x.strip()) for x in coeffs_str.split(",")]
a, b, c = coeffs[0], coeffs[1], coeffs[2]

# Check for valid 'a'
if a == 0:
    print("Error: Coefficient 'a' cannot be zero for a quadratic equation.")
else:
    # Calculate the discriminant
    delta = b**2 - 4 * a * c

    # Check if real solutions exist
    if delta < 0:
        print(
            "Error: Discriminant is negative, no real solutions exist (complex solutions not handled)."
        )
    else:
        # Calculate the two solutions
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)

        # Display the results
        print(f"x = {x1} , {x2}")
