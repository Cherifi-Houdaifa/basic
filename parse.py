# turn tokens into a tree

from lex import Types, Token, cmpoperators


class printable:
    def __repr__(self) -> str:
        return str(vars(self))


class comparision(printable):
    def __init__(self, left: Token, op: Token, right: Token) -> None:
        self.left = left
        self.op = op
        self.right = right

class ifstatment(printable):
    def __init__(self, cmp: comparision, body: list):
        self.cmp = cmp
        self.body = body

class expr(printable):
    def __init__(self, left, op: Token, right):
        self.left = left
        self.op = op
        self.right = right

class assignment(printable):
    def __init__(self, op: Token, value: expr | Token):
        self.op = op
        self.value = value



def help(tokens):
    for i in range(len(tokens)):
        print(tokens[i].type, end=' ')


class Parser:
    def __init__(self):
        pass    
    
    def parse(self, tokens: list[Token]) -> list:
        rslt = []
        i = 0
        while i < len(tokens):
            if tokens[i].type == Types.IF:
                ifobject, i = self.handleif(tokens[i:])
                rslt.append(ifobject)
            elif tokens[i].type == Types.ident:
                j = i
                while j < len(tokens):
                    if tokens[j].type == Types.semicolon:
                        break
                    j += 1
                else:
                    self.abort("No semicolon")
                rslt.append(self.handleassignment(tokens[i:j]))
                i = j + 1
                
        return rslt
            

    # i is the index from which the if statment starts
    # returns where the if statment ends and the if statment object
    def handleif(self, tokens: list[Token]) -> tuple[ifstatment, int]:
        cmptokens = []
        i = 1
        while tokens[i].type != Types.THEN:
            if i+1 == len(tokens):
                self.abort("THEN not found after IF")
            cmptokens.append(tokens[i])
            i+=1
        i+=1
        bodytokens = []
        while tokens[i].type != Types.ENDIF:
            if i+1 == len(tokens):
                self.abort("ENDIF not found after THEN")
            bodytokens.append(tokens[i])
            i+=1
        
        return (ifstatment(cmp=self.handlecmp(cmptokens), body=self.parse(bodytokens)), i+1)
    
    # takes comparision tokens and returns a comparision object
    # this thing is simple (no expressions)
    def handlecmp(self, tokens: list[Token]) -> comparision:
        if len(tokens) != 3:
            self.abort("comparision should be of the form a > 20, nothing complicated yet")
        if tokens[0].type not in [Types.number, Types.ident]:
            self.abort("left operand in comparision should be either number or identifier")
        if tokens[1].type not in cmpoperators:
            self.abort("not comparision operator after left op")
        if tokens[2].type not in [Types.number, Types.ident]:
            self.abort("right operand in comparision should be either number or identifier")
        return comparision(tokens[0], tokens[1], tokens[2])
        
    def handleassignment(self, tokens: list[Token]) -> assignment:
        if tokens[0].type != Types.ident:
            self.abort("identifier should be first")
        if tokens[1].type != Types.assignment:
            self.abort("no assignment operator")
        return assignment(tokens[0], self.handleexpr(tokens[2:]))


    # to parse it, think of it as a sum of products (after dealing with parentheses)
    # btw pth stands for parenthese (it's too long to write every time)
    def handleexpr(self, tokens: list[Token | expr] | Token | expr) -> expr:
        if len(tokens) == 1:
            return tokens[0]

        # handle parentheses
        pths = []
        pthcount = 0
        pthindex = -1
        for i in range(len(tokens)):
            if type(tokens[i]) == Token and tokens[i].type == Types.openpth:
                if pthcount == 0:
                    pthindex = i
                pthcount += 1
            if type(tokens[i]) == Token and tokens[i].type == Types.closepth:
                pthcount -= 1
                if pthcount == -1:
                    self.abort("invalid parentheses")
                elif pthcount == 0:
                    pths.append((pthindex, i))
        if pthcount != 0:
            self.abort("invalid parentheses")
        for pth in pths[::-1]:
            tokens = tokens[0:pth[0]] + [self.handleexpr(tokens[pth[0] + 1: pth[1]])] + tokens[pth[1]+1:]
        if len(tokens) == 1:
            return tokens[0]
        
        for i in range(len(tokens)):
            if type(tokens[i]) == Token and tokens[i].type in [Types.plus, Types.minus]:
                # make an expression
                return expr(self.handleexpr(tokens[0:i]), tokens[i], self.handleexpr(tokens[i+1:]))
        # we are here because there are only products or divisions
        for i in range(len(tokens)):
            if type(tokens[i]) == Token and tokens[i].type in [Types.star, Types.slash]:
                # make an expression
                return expr(self.handleexpr(tokens[0:i]), tokens[i], self.handleexpr(tokens[i+1:]))

    def abort(self, message, exitcode=1):
        print("Error:", message)
        exit(exitcode)
 
# takes a program as tokens and outputs a tree
# a program is a bunch of statments
# a statment starts with either a keyword (IF | PRINT | WHILE ...) or an identifier for assignment
