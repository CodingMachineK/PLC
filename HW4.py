class Token:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
    
    def match(self, expected_type):
        """Match the current token against the expected token type."""
        if self.current_token().type == expected_type:
            self.advance()
            return True
        return False
    
    def expect(self, expected_type):
        """Expect that the current token is of the expected type."""
        if not self.match(expected_type):
            raise Exception(f"Expected '{expected_type}', found '{self.current_token().value}'")
    
    def current_token(self):
        """Get the current token."""
        return self.tokens[self.current_token_index]
    
    def advance(self):
        """Advance to the next token."""
        self.current_token_index += 1
    
    def parse(self):
        """Parse the input tokens."""
        self.stmt()
    
    def stmt(self):
        """Parse a statement."""
        if self.match('IF'):
            self.expect('LPAREN')
            self.bool_expr()
            self.expect('RPAREN')
            self.parse_braced_block()
            if self.match('ELSE'):
                self.parse_else_block()
        elif self.match('LBRACE'):
            self.parse_braced_block()
        elif self.match('WHILE'):
            self.expect('LPAREN')
            self.bool_expr()
            self.expect('RPAREN')
            self.parse_braced_block()
        else:
            self.expr()
    
    def parse_braced_block(self):
        """Parse a block of statements enclosed in braces."""
        self.expect('LBRACE')
        self.stmt_list()
        self.expect('RBRACE')
    
    def parse_else_block(self):
        """Parse the else block of an if statement."""
        if self.match('LBRACE'):
            self.stmt_list()
            self.expect('RBRACE')
        else:
            self.stmt()
    
    def stmt_list(self):
        """Parse a list of statements."""
        while not self.match('RBRACE'):
            self.stmt()
            self.expect('SEMICOLON')
    
    def bool_expr(self):
        """Parse a boolean expression."""
        self.bterm()
        while self.match('LT') or self.match('GT') or self.match('LE') or self.match('GE'):
            self.bterm()
    
    def bterm(self):
        """Parse a boolean term."""
        self.band()
        while self.match('EQ') or self.match('NE'):
            self.band()
    
    def band(self):
        """Parse a boolean and."""
        self.bor()
        while self.match('AND'):
            self.bor()
    
    def bor(self):
        """Parse a boolean or."""
        self.expr()
        while self.match('OR'):
            self.expr()
    
    def expr(self):
        """Parse an expression."""
        self.term()
        while self.match('PLUS') or self.match('MINUS'):
            self.term()
    
    def term(self):
        """Parse a term."""
        self.fact()
        while self.match('MULT') or self.match('DIV') or self.match('MOD'):
            self.fact()
    
    def fact(self):
        """Parse a factor."""
        if self.match('ID') or self.match('INT_LIT') or self.match('FLOAT_LIT'):
            pass
        elif self.match('LPAREN'):
            self.expr()
            self.expect('RPAREN')
        else:
            raise Exception(f"Expected identifier, integer literal, or floating point literal, found '{self.tokens[self.pos].value}'")