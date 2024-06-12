# Write your code here
import re
def scrape_email_addresses(string):
    return re.findall(r'[\w\.-]+@[\w\.-]+', string)

#[\w\.-]+@[\w\.-]+: 
#This regular expression matches one or more word characters (alphanumeric and underscore), dots (.), or hyphens (-), followed by an @, followed by one or more word characters, dots, or hyphens. 
#The \w shorthand character class matches any word character (equal to [a-zA-Z0-9_]).