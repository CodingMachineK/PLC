import re

class Token:
    def __init__(self, token_type, lexeme):
        self.token_type = token_type
        self.lexeme = lexeme

class Lexer:
    def __init__(self, file_name):
        with open(file_name, 'r') as f:
            self.source_code = f.read()
        self.tokens = []
        self.current_pos = 0
        self.keywords = {'and': 'AND', 'or': 'OR'}
    
    def tokenize(self):
        while self.current_pos < len(self.source_code):
            match = None
            for pattern in self.patterns:
                regex, token_type = pattern
                match = regex.match(self.source_code, self.current_pos)
                if match:
                    lexeme = match.group(0)
                    if token_type == 'IDENTIFIER':
                        token_type = self.keywords.get(lexeme.lower(), 'IDENTIFIER')
                    token = Token(token_type, lexeme)
                    self.tokens.append(token)
                    self.current_pos = match.end(0)
                    break
            if not match:
                print(f"Invalid token: {self.source_code[self.current_pos]}")
                self.current_pos += 1
        
    def show_tokens(self):
        for token in self.tokens:
            print(f"{token.token_type}: {token.lexeme}")
    
class MathLexer(Lexer):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.patterns = [
            (re.compile(r'\('), 'L_PAR'),
            (re.compile(r'\)'), 'R_PAR'),
            (re.compile(r'\+'), 'PLUS'),
            (re.compile(r'-'), 'MINUS'),
            (re.compile(r'\*'), 'MUL'),
            (re.compile(r'/'), 'DIV'),
            (re.compile(r'%'), 'MOD'),
            (re.compile(r'='), 'ASSIGN'),
            (re.compile(r'=='), 'EQUALS'),
            (re.compile(r'<='), 'LESS_THAN_EQUAL'),
            (re.compile(r'>='), 'GREATER_THAN_EQUAL'),
            (re.compile(r'<'), 'LESS_THAN'),
            (re.compile(r'>'), 'GREATER_THAN'),
            (re.compile(r'and'), 'AND'),
            (re.compile(r'or'), 'OR'),
            (re.compile(r'[a-zA-Z][a-zA-Z0-9]*'), 'IDENTIFIER'),
            (re.compile(r'[0-9]+\.[0-9]*'), 'FLOAT_LITERAL'),
            (re.compile(r'[0-9]+'), 'INT_LITERAL')
        ]

if __name__ == '__main__':
    lexer = MathLexer('math_operations.txt')
    lexer.tokenize()
    lexer.show_tokens()