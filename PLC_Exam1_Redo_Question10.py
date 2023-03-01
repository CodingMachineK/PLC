
#Question #10
import re

def is_valid_integer(s):
    """
    Check if the given string is a valid integer literal using regular expressions.
    """
    pattern = r'[+-]?(0[xX][0-9a-fA-F]+|0[0-7]*|[1-9][0-9]*)'
    match = re.match(pattern, s)
    return match is not None

# Example usage:
s = '0x8a44000000000040Ui64'
if is_valid_integer(s):
    print(f"{s} is a valid integer literal")
else:
    print(f"{s} is not a valid integer literal")