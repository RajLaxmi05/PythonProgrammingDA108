text = input("Enter the str: ")
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
text_without_vowels = " "
for char in text:
    if char not in vowels:
        text_without_vowels += char
print(text_without_vowels)
