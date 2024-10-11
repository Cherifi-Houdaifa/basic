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
    quote = 15
    assignment = 16
    plus = 17
    minus = 18
    star = 19
    slash = 20
    openpth = 21
    closepth = 22
    semicolon = 23
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
        for char in line:
            # maybe check for char instead of current for single char tokens so that "(a" won't be counted as a single token, but two tokens
            if char == " ":
                # check what the current token is
                if current == "IF":
                    rslt.append(Token(Types.IF, None))
                elif current == "THEN":
                    rslt.append(Token(Types.THEN, None))
                elif current == "ENDIF":
                    rslt.append(Token(Types.ENDIF, None))
                elif current == ">":
                    rslt.append(Token(Types.gt, ">"))
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
    return rslt


