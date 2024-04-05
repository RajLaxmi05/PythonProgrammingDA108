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

class CSVDataManager(FileManager):
    def __init__(self, file_path, delimiter=','):
        super().__init__(file_path)
        self.delimiter = delimiter
    
    def read_data(self):
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    header = lines[0].split('self.delimiter')
                    data = []
                    for line in lines[1 :]:
                        values = line.split('self.delimiter')
                        data.append(dict(zip(header, values)))
            return data            
        except FileNotFoundError:
            print ("File not found.")

    def write_data(self, data):
        with open(self.file_path, 'w') as file:
            if data:
                headers = data[0].keys()
                file.write(self.delimiter.join(headers) + '\n')
                for row in data:
                    values = [str(row[key]) for key in headers]
                    file.write(self.delimiter.join(values) + '\n')

    def append_data(self, data):
        with open(self.file_path, 'a') as file:
            if data:
                headers = data[0].keys()
                for row in data:
                    values = [str(row[key]) for key in headers]
                    file.write(self.delimiter.join(values) +'\n')
          

def main():
    csv_manager = CSVDataManager("data.csv")    

    data = [ 
        {"Name": "John", "Age": 30, "City": "New York"},
        {"Name": "Alice", "Age": 25, "City": "Los Angeles"},
        {"Name": "Bob", "Age": 35, "City": "Chicago"}
    ]
    csv_manager.write_data(data)

    print(csv_manager.read_data())

    new_data = [
        {"Name": "Emily", "Age": 28, "City": "San Francisco"},
        {"Name": "Michael", "Age": 40, "City": "Seattle"}
    ]

    csv_manager.append_data(new_data)

    print(csv_manager.read_data())

main()


