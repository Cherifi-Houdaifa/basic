# turn code into tokens

import re
import enum
class Types(enum.Enum):
    PRINT = 0
    LET = 1
    IF = 2
    THEN = 3
    ENDIF = 4
    WHILE = 5
    DO = 6
    ENDWHILE = 7
    gt = 8
    lt = 9
    eq = 10
    gteq = 11
    lteq = 12
    ident = 13
    number = 14
    string = 15
    assignment = 16
    plus = 17
    minus = 18
    star = 19
    slash = 20
    openpth = 21
    closepth = 22
    semicolon = 23
    INPUT = 24
    noteq = 25
    lognot = 26
    bitnot = 27
    mod = 28
    leftshift = 29
    rightshift = 30
    bitand = 31
    bitxor = 32
    bitor = 33
    logand = 34
    logor = 35
    def __repr__(self) -> str:
        return f"\"{str(self.name)}\""

cmpoperators = [Types.gt, Types.lt, Types.eq, Types.gteq, Types.lteq]




class Token:
    def __init__(self, type: Types, value: str | None):
        self.type = type
        self.value = value
    def __repr__(self) -> str:
        return str(vars(self))


def lex(code: str) -> list[Token]:
    code = code.split("\n")
    rslt = []
    for line in code:
        line = line.replace("\t", " ").strip()
        line = re.sub(" +", " ", line) + " "
        if line == " ":
            continue
        current = ""
        instring = False
        for char in line:
            # maybe check for char instead of current for single char tokens so that "(a" won't be counted as a single token, but two tokens
            if not instring:
                if char == '"':
                    # now we are inside a string
                    instring = True
                    current = ""

                elif char == " ":
                    if current != "":
                        # check what the current token is
                        if current == "IF":
                            rslt.append(Token(Types.IF, None))
                        elif current == "THEN":
                            rslt.append(Token(Types.THEN, None))
                        elif current == "ENDIF":
                            rslt.append(Token(Types.ENDIF, None))
                        elif current == "LET":
                            rslt.append(Token(Types.LET, None))
                        elif current == "PRINT":
                            rslt.append(Token(Types.PRINT, None))
                        elif current == "INPUT":
                            rslt.append(Token(Types.INPUT, None))
                        elif current == "WHILE":
                            rslt.append(Token(Types.WHILE, None))
                        elif current == "DO":
                            rslt.append(Token(Types.DO, None))
                        elif current == "ENDWHILE":
                            rslt.append(Token(Types.ENDWHILE, None))
                        elif current == ">":
                            rslt.append(Token(Types.gt, ">"))
                        elif current == "<":
                            rslt.append(Token(Types.lt, "<"))
                        elif current == "==":
                            rslt.append(Token(Types.eq, "=="))
                        elif current == "!=":
                            rslt.append(Token(Types.noteq, "!="))
                        elif current == ">=":
                            rslt.append(Token(Types.gteq, ">="))
                        elif current == "<=":
                            rslt.append(Token(Types.lteq, "<="))
                        elif current == "=":
                            rslt.append(Token(Types.assignment, None))
                        elif current == "+":
                            rslt.append(Token(Types.plus, "+"))
                        elif current == "-":
                            rslt.append(Token(Types.minus, "-"))
                        elif current == "*":
                            rslt.append(Token(Types.star, "*"))
                        elif current == "/":
                            rslt.append(Token(Types.slash, "/"))
                        elif current == "!":
                            rslt.append(Token(Types.lognot, "!"))
                        elif current == "~":
                            rslt.append(Token(Types.bitnot, "~"))
                        elif current == "%":
                            rslt.append(Token(Types.mod, "%"))
                        elif current == "<<":
                            rslt.append(Token(Types.leftshift, "<<"))
                        elif current == ">>":
                            rslt.append(Token(Types.rightshift, ">>"))
                        elif current == "&":
                            rslt.append(Token(Types.bitand, "&"))
                        elif current == "^":
                            rslt.append(Token(Types.bitxor, "^"))
                        elif current == "|":
                            rslt.append(Token(Types.bitor, "|"))
                        elif current == "&&":
                            rslt.append(Token(Types.logand, "&&"))
                        elif current == "||":
                            rslt.append(Token(Types.logor, "||"))
                        
                        elif current == "(":
                            rslt.append(Token(Types.openpth, None))
                        elif current == ")":
                            rslt.append(Token(Types.closepth, None))
                        elif current == ";":
                            rslt.append(Token(Types.semicolon, None))
                        elif current.isdigit():
                            rslt.append(Token(Types.number, current))
                        else:
                            rslt.append(Token(Types.ident, current))
                    current = ""
                else:
                    current += char
            else:
                if char == '"':
                    # string has ended
                    instring = False
                    rslt.append(Token(Types.string, current))
                    current = ""
                else:
                    current += char

    return rslt


