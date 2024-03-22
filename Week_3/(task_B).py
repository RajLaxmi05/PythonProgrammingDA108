while True:
    string = input("user input: ")
    if string == "q":
        print(exit)
        break
    word = "...".join(string.split())
    print(word)
