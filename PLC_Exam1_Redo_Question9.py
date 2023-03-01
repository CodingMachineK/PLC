#Question #9

import re

def is_valid_float(s):
    """
    Check if the given string is a valid floating point literal using regular expressions.
    """
    pattern = r'^[+-]?(\d*\.\d+|\d+\.\d*)([eE][+-]?\d+)?$'
    match = re.match(pattern, s)
    return match is not None

# Example usage:
s = '1.575E1'
if is_valid_float(s):
    print(f"{s} is a valid floating point literal")
else:
    print(f"{s} is not a valid floating point literal")