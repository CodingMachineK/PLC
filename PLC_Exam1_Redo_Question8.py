#Question #8

import re

def is_valid_email(email):
    """
    Check if the given string is a valid email address using regular expressions.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    match = re.match(pattern, email)
    return match is not None

# Example usage:
email = 'karriem.muhammad17@example.com'
if is_valid_email(email):
    print(f"{email} is a valid email address")
else:
    print(f"{email} is not a valid email address")
