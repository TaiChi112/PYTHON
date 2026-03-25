n_str = input("Enter an integer: ")

try:
    n = int(n_str)
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        print(f"{n} is divisible by:")
        for i in range(1, n + 1):
            if n % i == 0:
                print(i)
except ValueError:
    print("Invalid input. Please enter an integer.")
