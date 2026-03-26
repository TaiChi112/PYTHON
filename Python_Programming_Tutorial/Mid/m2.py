def calExam():
    sf = input("Choose your solution file: ")
    ef = input("Choose your exam file: ")

    sol = []
    score = []
    studen = []

    with open(sf, "r") as f:
        for line in f:
            sol = line.split(" ")

    with open(ef, "r") as f:
        t = 0
        for line in f:
            studen.append(line.split())

        for i in range(8):
            for j in range(10):
                if sol[j] == studen[i][j]:
                    t += 1
            score.append(t)
            t = 0

    print("Studen score: ", score)


calExam()
