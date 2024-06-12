# Write your code here
import re
def correct_dates(string):
    return re.sub(r'(\d+)/(\d+)/(\d+)', r'\2/\1/\3', string)
    # Commented explanation of the code
    # The code uses the re.sub() function from the re module to perform a substitution operation on the input string.
    # The regular expression pattern r'(\d+)/(\d+)/(\d+)' matches a date format in the form of dd/mm/yyyy, where each component is represented by (\d+).
    # The parentheses capture the day, month, and year components separately.
    # The replacement string r'\2/\1/\3' rearranges the captured components to the desired format mm/dd/yyyy.
    # The re.sub() function replaces all occurrences of the matched pattern with the replacement string.
    # The corrected string is then returned as the result.