import math


def is_right_triangle(a, b, c):
    # Sort the sides to ensure c is the hypotenuse
    sides = sorted([a, b, c])
    # Check Pythagorean theorem: a^2 + b^2 = c^2
    # Using math.isclose for float comparison due to potential precision issues
    return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)


# Get input from the user
lengths_str = input("Length of 3 sides (comma-separated): ")
try:
    # Split the input string by comma and convert to floats
    s1, s2, s3 = map(float, lengths_str.split(","))
    result = is_right_triangle(s1, s2, s3)
    print(f"Right triangle: {result}")
except ValueError:
    print("Invalid input. Please enter three numbers separated by commas.")
