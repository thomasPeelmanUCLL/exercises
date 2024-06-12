# Write your code here
import re
def is_valid_password(string):
    # List of positive regex patterns that the password must match
    positive_regexes = [
        r'.{12,}',  # Matches any string with 12 or more characters
        r'[0-9]',   # Matches any digit
        r'[a-z]',   # Matches any lowercase letter
        r'[A-Z]',   # Matches any uppercase letter
        r'[-+/.*@]',  # Matches any of the specified special characters
    ]

    # List of negative regex patterns that the password must not match
    negative_regexes = [
        r'(.)\1{2}',       # Matches any character repeated 3 times in a row
        r'(.)(.*\1){3}'    # Matches any character repeated 4 times in the string
    ]

    # Check if the password matches all positive regex patterns
    for regex in positive_regexes:
        if not re.search(regex, string):
            return False

    # Check if the password matches any negative regex patterns
    for regex in negative_regexes:
        if re.search(regex, string):
            return False

    # If the password passes all checks, it is considered valid
    return True