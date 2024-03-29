pi_string = ""

def load_pi_digits(filename):
    global pi_string 
    with open(filename, 'r') as file:
        pi_string = file.read().strip()
        load_pi_digits("pi_1M.txt")     
print(pi_string)




def get_pi_one_gram_stats():
    """
    Compute the percentage of each digit (0 to 9) in pi_string.
    
    Returns:
        dict: A dictionary containing the percentage of each digit.
    """
    digit_counts = {str(digit): 0 for digit in range(10)}
    for digit_char in pi_string:
        if digit_char.isdigit():
            digit_counts[digit_char] += 1
    total_length = len(pi_string)
    digit_percentages = {digit: (count / total_length) * 100 for digit, count in digit_counts.items()}
    return digit_percentages
stats = get_pi_one_gram_stats()
for digit, percentage in stats.items():
    print(f"Digit: {digit}, Percentage: {percentage:.2f}%")
    



def save_pi_stats_to_file(filename):
    """
    Compute the percentage of each digit (0 to 9) in pi_string and save the data to a text file.
    
    Args:
        filename (str): The name of the file to save the data.
    """
    stats = get_pi_one_gram_stats()
    with open(filename, 'w') as file:
        for digit, percentage in stats.items():
            file.write(f"Digit: {digit}, Percentage: {percentage:.2f}%\n")
save_pi_stats_to_file("pi_stats.txt")            


