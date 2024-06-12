# Write your code here
import re
def remove_trailing_whitespace(string):
    return re.sub(r'\s+$', '', string, flags=re.MULTILINE)
"""
r'\s+$': This is the pattern that the function will search for in the string. 
The r before the string indicates that this is a raw string, which treats backslashes as literal characters. 
The pattern \s+$ matches one or more (+) whitespace characters (\s) at the end of a line ($).

'': This is the replacement string. 
Matches of the pattern will be replaced with this string. 
In this case, it's an empty string, which means that matches of the pattern will be removed from the string.

string: This is the string that the function will operate on. The function will search this string for matches of the pattern.

flags=re.MULTILINE: This is an optional argument that changes the behavior of the pattern. 
The re.MULTILINE flag makes the pattern treat each line in the string as a separate string. 
This means that the $ in the pattern will match the end of each line, not just the end of the string."""