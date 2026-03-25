temperatures = []

for i in range(1, 8):
    while True:
        try:
            temp_str = input(f"Day {i} : ")
            temp = float(temp_str)
            temperatures.append(temp)
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value for temperature.")

for i in range(1, len(temperatures)):
    if temperatures[i] < temperatures[i - 1]:
        print(f"Temperature dropped on day {i + 1}")
