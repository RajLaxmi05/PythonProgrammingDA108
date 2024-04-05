def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
        return contents
    except FileExistsError:
        return(f"File does't exist.")
    
file_path = "ex1.txt"
file_contents = read_file(file_path)
print(file_contents)
