import time
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
    




def is_birthdate_in_pi():
    """
        Check if the user's birthdate in DD-MM-YYYY format is contained in pi_string.
    """
    user_input = input("Enter your birthdate in DD-MM-YYYY format: ")
    try:
        day, month, year = map(int, user_input.split('-'))
        date_str = f"{day:02d}{month:02d}{year}"
    except ValueError:
        print("Invalid input. Please enter the date in DD-MM-YYYY format.")
        return
    start_time = time.time()
    if date_str in pi_string:
        num_occurrences = pi_string.count(date_str)
        end_time = time.time()
        processing_time = ( end_time - start_time) * 1000
        print(f"Date found in pi.")
        print(f"No. of occurrrences: {num_occurrences}")
        print(f"Processing time: {processing_time:.2f} ms")
    else:
        end_time = time.time()
        processing_time = ( end_time - start_time) * 1000
        print(f"Date not found in pi.")
is_birthdate_in_pi()   
