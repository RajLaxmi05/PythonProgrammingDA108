import re
def extract_emails(text):
     """
    Extract all valid email addresses from a given string.
    
    Args:
        text (str): The input string to search for email addresses.
        
    Returns:
        list: A list of valid email addresses found in the input string.
    """
     email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
    
    # Find all matches of email addresses in the text using the regular expression
     matches = re.finditer(email_pattern, text)
    
    # Extract email addresses from matches
     emails = [match.group() for match in matches]
    
     return emails


text = "Please send your queries to support@example.com or contact@company.org. In case you wish to contact a specific contact person, communicate with Shankar at shankar.doe@gmail.com."
emails = extract_emails(text)
print(emails)
