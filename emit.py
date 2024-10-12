# turn tree into code (c code)
from parse import ifstatment, assignment, expr, letdefinition, printstatement, inputstatement, whilestatement, unary
from lex import Types
from lex import Token


def emitexpr(statment: expr | Token | unary) -> str:
    if type(statment) == Token:
        return f"{statment.value}"
    if type(statment) == unary:
        return f"({statment.op.value} {emitexpr(statment.arg)})"
    return f"({emitexpr(statment.left)} {statment.op.value} {emitexpr(statment.right)})"    
# takes a statment and gives it's code
def emit(statments) -> str:
    rslt = ""
    for statment in statments:
        if type(statment) == ifstatment:
            rslt += f"""if ({emit([statment.cmp])}) {{
    {emit(statment.body)}
}}\n"""
        elif type(statment) == whilestatement:
            rslt += f"""while ({emit([statment.cmp])}) {{
    {emit(statment.body)}
}}\n"""
        elif type(statment) == assignment:
            rslt += f"{statment.op.value} = {emitexpr(statment.value)};\n"
        elif type(statment) in [expr, unary]:
            rslt += emitexpr(statment)
        elif type(statment) == letdefinition:
            rslt += f"int {statment.op.value};\n"
        elif type(statment) == printstatement:
            if statment.arg.type == Types.string:
                rslt += f"printf(\"{statment.arg.value}\");\n"
            elif statment.arg.type in [Types.ident, Types.number]:
                rslt += f"printf(\"%d\\n\", {statment.arg.value});\n"
        elif type(statment) == inputstatement:
            rslt += f"scanf(\"%d\", &{statment.arg.value});\n"
        
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