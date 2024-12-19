with open("models.txt", "w") as f:
    f.write("hello\n")
    f.write("Карапетян Виген\nя играю в игру\n")
    f.writelines(["1, 2, 3, 4"])

with open("models.txt", "r") as f:
    for i in f:
        print(i)
