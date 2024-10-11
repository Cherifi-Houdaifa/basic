# turn tree into code (c code)
from parse import ifstatment, comparision, assignment, expr
from lex import Token


def emitexpr(statment: expr | Token) -> str:
    if type(statment) == Token:
        return f"{statment.value}"
    return f"({emitexpr(statment.left)} {statment.op.value} {emitexpr(statment.right)})"    
# takes a statment and gives it's code
def emit(statments) -> str:
    rslt = ""
    for statment in statments:
        if type(statment) == ifstatment:
            rslt += f"""if ({emit([statment.cmp])}) {{
    {emit(statment.body)}
}}"""
        elif type(statment) == comparision:
            rslt += f"{statment.left.value} {statment.op.value} {statment.right.value}"
        elif type(statment) == assignment:
            rslt += f"{statment.op.value} = {emitexpr(statment.value)};"
        elif type(statment) == expr:
            rslt += emitexpr(statment)
        
    return rslt


def codegen(statments) -> str:
    code = \
f"""#include <stdlib.h>
#include <stdio.h>
int main () {{
    {emit(statments)}
}}
"""
    return code