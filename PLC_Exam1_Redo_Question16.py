#Question 16

import re

def is_multiline_comment(comment):
    pattern = r'^\s*/\*.*\*/\s*$'
    return bool(re.match(pattern, comment, re.DOTALL))

# Example usage:
print(is_multiline_comment('/* This is a multiline comment */'))  
print(is_multiline_comment('/* This is\na multiline\ncomment */')) 
print(is_multiline_comment('/* Not a multiline comment */'))       
print(is_multiline_comment('This is not a comment'))      