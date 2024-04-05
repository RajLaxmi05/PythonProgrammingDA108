class FileReader:

    def read_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            return "File not found"
        except Exception as e:
            return f"An error occurred: {e}"
        
        


class TextAnalyzer:
    def __init__(self, text):
        self.text = text
    
    def get_word_count(self):
        words = self.text.split()
        return len(words)
    
    def get_sentence_count(self):
        sentence = self.text.split('.')
        return len(sentence)
    
    def get_average_word_length(self):
        words = self.text.split()
        total_characters = sum(len(word) for word in words)
        return total_characters/len(words)
    
    def get_top_words(self, n):
        word_counts = {}
        words = self.text.split()
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        return sorted_word_counts[:n]
    

        
class ReportGenerator:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def generate_report(self):
        report = ""
        report += "Word count: {}\n".format(self.analyzer.get_word_count())
        report += "Sentence count: {}\n".format(self.analyzer.get_sentence_count())
        report += "Average word length: {:.2f}\n".format(self.analyzer.get_average_word_length())
        top_words = self.analyzer.get_top_words(10)
        report += "Top Words:\n"
        for word, frequency in top_words:
            report += "{}: {}\n".format(word, frequency)
        return report
    
    def save_report(self, file_path):
        report = self.generate_report()
        with open(file_path, 'w') as file:
            file.write(report)

def main():
    #Prompt the user to enter the path of the text file to be analyzed.
    file_path = input("Enter the path of the text file to be analyzed: ")

    #Create an instance of the FileReader class and read the contents of the file.
    file_reader = FileReader()
    file_content = file_reader.read_file(file_path)

    #Create an instance of the TextAnalyzer class with the file contents.
    analyzer = TextAnalyzer(file_content)

    #Create an instance of the ReportGenerator class with the TextAnalyzer instance.
    report_generator = ReportGenerator(analyzer)

    #Generate the summary report using the generate_report method.
    report = report_generator.generate_report()

    #Prompt the user to enter the path where the report should be saved.
    report_path = input("Enter the path where the report should be saved: ")

    #Save the report using the save_report method.
    report_generator.save_report(report_path)



main()
