from lex import lex
from parse import Parser, help
from emit import codegen, emitexpr
import sys

if len(sys.argv) != 2:
    print("provide a file to transpile")
    exit(1)

code = open(sys.argv[1], "r").read()

tokens = lex(code)
#help(tokens)

parser = Parser()
ast = parser.parse(tokens)
print(codegen(ast))

exit(0)
print(output)
# with open("./out.json", "w") as f:
#     a = str(ast).replace("'", '"').replace("None", "\"None\"")
#     f.write(a)