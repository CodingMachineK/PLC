import re
from parser import Parser

class Token:
    def __init__(self, lexeme: str, code: int):
        self.lexeme = lexeme
        self.code = code
class Compiler:
    def __init__(self):
        self.lexer = Lexer()
        self.parser = Parser()
    
    def compile(self, input_file: str) -> str:
        with open(input_file, 'r') as file:
            input_str = file.read()
        return input_str
compiler = Compiler()
input_file = 'example_input.txt'
input_str = compiler.compile(input_file)

class Lexer:
    def __init__(self, input_str: str):
        self.input_str = input_str
        self.tokens = []
        self.current_pos = 0
        self.keywords = {'for', 'if', 'else', 'while', 'do', 'int', 'float', 'char', 'bool', 'true', 'false'}
        self.operators = {'+', '-', '*', '/', '**', '%', '++', '--', '==', '!=', '<=', '>=', '<', '>', '&&', '||', '!', '='}
        self.grouping_symbols = {'(', ')', '{', '}', '[', ']'}
        self.parameter_separator = ','
        self.function_symbols = {'(' , ')' }
        self.regex_patterns = [
            (r'\d+\.\d+', 'real_literal'),  # matches fractional numbers
            (r'\d+', 'natural_literal'),   # matches whole numbers
            (r'true|false', 'bool_literal'),  # matches boolean literals
            (r"'\\?.'", 'char_literal'),  # matches single ascii characters, including escape characters
            (r'"(\\"|.)*?"', 'string_literal'),  # matches any number of ascii characters, including escape characters
            (r'\bfor\b|\bif\b|\belse\b|\bwhile\b|\bdo\b|\bint\b|\bfloat\b|\bchar\b|\bbool\b|\btrue\b|\bfalse\b', 'keyword'),  # matches keywords
            (r'\+|-|\*|/|\*\*|%|\+\+|--|==|!=|<=|>=|<|>|&&|\|\||!|=', 'operator'),  # matches operators
            (r'\(|\)|\{|\}|\[|\]', 'grouping_symbol'),  # matches grouping symbols
            (r',', 'parameter_separator'),  # matches parameter separator
            (r'\(|\)', 'function_symbol')  # matches function symbols
        ]
    
    def lex(self) -> list:
        while self.current_pos < len(self.input_str):
            token = self.get_next_token()
            if token is None:
                return None
            self.tokens.append(token)
        return self.tokens
    
    def get_next_token(self) -> object:
        for pattern, token_type in self.regex_patterns:
            match = re.match(pattern, self.input_str[self.current_pos:])
            if match:
                lexeme = match.group(0)
                token = Token(lexeme, token_type)
                self.current_pos += len(lexeme)
                return token
        return None
