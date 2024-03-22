def remove_vowels(text):
    vowels = "aeiouAEIOU"
    stripped_text = ""
    for char in text:
        if char not in vowels:
            stripped_text += char
    return stripped_text


while True:
    task = input("user input: ")
    if task == "q":
        print("Exit")
        break

    stripped_text = remove_vowels(task)
    print("Output:", stripped_text)


   
