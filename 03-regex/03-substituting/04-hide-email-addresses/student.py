# Write your code here
import re
def hide_email_addresses(string):
    return re.sub(r'\b\w+@\w+\.\w+\b', '***@***.***', string)


def hide_email_addresses2(string):
    def replace(match):
        return '*' * len(match.group(0))

    return re.sub(r'[a-zA-Z0-9.]+@[a-zA-Z0-9.]+', replace, string)
