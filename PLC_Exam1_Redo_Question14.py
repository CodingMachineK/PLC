#Question #14

import re

pattern = r"((a{2})|(bb))*((c|d)+|(cbad){2})*"
string = "aabbccddcbadcbad"

match = re.fullmatch(pattern, string)

if match:
    print("The string matches the regular expression.")
else:
    print("The string does not match the regular expression.")