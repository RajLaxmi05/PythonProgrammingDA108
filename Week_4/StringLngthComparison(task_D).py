string_1 = input("Enter the string_1: ")
string_2 = input("Enter the string_2: ")
if len(string_1) > len(string_2):
    print("String 1 is longer than 2.")
elif len(string_1) < len(string_2):
    print("String 2 is longer than 1.")
else:
    print("Both string are of equal length.")
