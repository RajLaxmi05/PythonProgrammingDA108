while True:
    string = input("user input: ")
    if string == "q":
        print("Exit")
        break
    print("case altered:", string.swapcase())
