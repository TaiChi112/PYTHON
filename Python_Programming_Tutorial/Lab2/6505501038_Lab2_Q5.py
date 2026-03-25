sentence = []
while True:
    word = input("Next word : ")
    if word == ".":
        break
    sentence.append(word)

print("Sentence: " + " ".join(sentence))
