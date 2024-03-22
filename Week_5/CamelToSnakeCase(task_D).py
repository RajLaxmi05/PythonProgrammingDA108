camel_case = input("Enter the text in camel case: ")
snake_case = " "
snake_case += camel_case[0].lower()
for char in camel_case[1: ]:
    if char.isupper():
        snake_case += '_' + char.lower()
    else:
        snake_case += char

print(snake_case)


      
