# Write your code here
import re
def is_valid_time(string):
    return re.fullmatch(r'([01][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])(.[0-9]{3})?', string)