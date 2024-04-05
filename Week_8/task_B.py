class FileManager:

    def __init__(self, file_path):
        self.file_path = file_path

    def read_contents(self):
        try:
            with open(self.file_path, 'r') as file:
                contents = file.read()
            return contents 
        except FileNotFoundError:
            return "File not found."
        
    def write_contents(self, new_contents):
        with open(self.file_path, 'w') as file:
            file.write(new_contents)

    def append_contents(self, new_contents):
        with open(self.file_path, 'a') as file:
            file.write(new_contents)


def main():
    s1 = FileManager("ex1.txt")
    print(s1.read_contents())
    s1.write_contents("This is the initial edit.\n")
    print(s1.read_contents())
    s1.append_contents("Hello Coder. This is the appended content\n")
    print(s1.read_contents())


#Calling main function.
main()
