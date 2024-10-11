from lex import lex
from parse import Parser
from emit import codegen
import sys

if len(sys.argv) != 2:
    print("provide a file to transpile")
    exit(1)

code = open(sys.argv[1], "r").read()

tokens = lex(code)
parser = Parser()
ast = parser.parse(tokens)
output = codegen(ast)

print(output)
# with open("./out.json", "w") as f:
#     a = str(ast).replace("'", '"').replace("None", "\"None\"")
#     f.write(a)