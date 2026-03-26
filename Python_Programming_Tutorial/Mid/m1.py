fn = input("Enter filename: ")
print(fn)
total = 0
with open(fn, "r") as f:
    for line in f:
        x, y = line.split(",")
        x, y = int(x), int(y)
        total += abs(x - y)
total = total / 3

print("Averge temoerature difference: ", total)
