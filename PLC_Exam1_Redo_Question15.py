#Question #15
import re

def is_valid_name(name):
    pattern = r'^[a-zA-Z_]\w*$'
    return bool(re.match(pattern, name))

# Example usage:
print(is_valid_name('my_variable'))  
print(is_valid_name('MyClass'))      
print(is_valid_name('myMethod'))     
print(is_valid_name('123abc'))       
print(is_valid_name('my-variable'))  