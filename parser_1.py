from typing import List
from lexer import Lexer
from token import Token


class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.lexer = Lexer(tokens)
        self.index = 0

    def parse(self) -> bool:
        try:
            return self.function1()
        except:
            return False

    def function1(self) -> bool:
        tr = False
        if self.stmt():
            tr = self.function2()
        return tr

    def function2(self) -> bool:
        tr = False
        back = self.index
        self.index += 1
        if self.tokens[self.index - 1].lexeme == "SEMICOL":
            self.index += 1
            if self.stmt():
                if self.function2():
                    tr = True
                else:
                    self.index = back  # backtrack
            else:
                self.index = back
        else:
            tr = True  # epsilon
        return tr

    def stmt(self) -> bool:
        tr = False
        back = self.index
        self.index += 1
        if self.tokens[self.index - 1].token_class == "IF":
            self.index += 1
            if self.expr():
                self.index += 1
                if self.tokens[self.index - 1].token_class == "THEN":
                    self.index += 1
                    if self.stmt():
                        tr = True
                    else:
                        self.index = back
                else:
                    self.index = back
            else:
                self.index = back
        elif self.tokens[self.index - 1].token_class == "WHILE":
            self.index += 1
            if self.expr():
                self.index += 1
                if self.tokens[self.index - 1].token_class == "DO":
                    self.index += 1
                    if self.stmt():
                        tr = True
                    else:
                        self.index = back
                else:
                    self.index = back
            else:
                self.index = back
        else:
            if "ID:" in self.tokens[self.index - 1].token_class:
                self.index += 1
                self.index += 1
                if self.tokens[self.index - 1].lexeme == "ASSIGN":
                    self.index += 1
                    if self.expr():
                        tr = True
                    else:
                        self.index = back
                else:
                    self.index = back
            else:
                self.index = back
        return tr

    def expr(self) -> bool:
        tr = False
        back = self.index
        if self.term():
            if self.expr1():
                tr = True
            else:
                self.index = back
        else:
            self.index = back
        return tr

    def expr1(self) -> bool:
        tr = False
        back = self.index
        self.index += 1
        if self.tokens[self.index - 1].token_class == "RELOP":
            self.index += 1
            if self.term():
                tr = True
            else:
                self.index = back
        else:
            tr = True  # epsilon
        return tr

    def term(self) -> bool:
        tr = False
        self.index += 1
        token_class = self.tokens[self.index - 1].token_class
        if "ID:" in token_class or "CONST" in token_class or \
                self.tokens[self.index - 1].lexeme in ["TRUE", "FALSE"]:
            tr = True
        return tr


    
    
