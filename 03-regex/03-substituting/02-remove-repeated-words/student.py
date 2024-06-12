# Write your code here
import re
def remove_repeated_words(string):
    return re.sub(r'(\b[a-zA-Z]+\b)( \1)+', r'\1', string)

""""
(\b[a-zA-Z]+\b): This part of the pattern matches a whole word that consists of one or more alphabetical characters.
 \b is a word boundary, which means it matches the position where a word character is not followed or preceded by another word-character.

( \1)+: This part of the pattern matches one or more occurrences of a space followed by the same word that was matched by the first part of the pattern.
 \1 is a backreference, which refers to the first group in the pattern.

 r'\1': This is the replacement string. 
 Matches of the pattern will be replaced with this string. 
 In this case, it's a backreference to the first group in the pattern, which is the word that was matched.

"""