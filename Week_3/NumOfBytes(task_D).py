while True:
    string = input("Enter the number: ")
    if string == "q":
        print("Exit")
        break
    num = int(string)
    num_bytes = (num.bit_length() + 7 // 8)
    print(num_bytes)
