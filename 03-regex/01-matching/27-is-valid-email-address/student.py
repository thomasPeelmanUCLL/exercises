import re

# Write your code here
def is_valid_email_address(string):
    # Use regular expression to match the email address pattern
    return re.fullmatch(r'[a-z0-9.]+@(student\.)?ucll\.be', string)
