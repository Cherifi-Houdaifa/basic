from lex import lex
from parse import Parser 
from emit import codegen, emitexpr
from evaluate import evalute
import sys

if len(sys.argv) != 2:
    print("provide a file to transpile")
    exit(1)
code = open(sys.argv[1], "r").read()
tokens = lex(code)



parser = Parser()
ast = parser.parse(tokens)

print(codegen(ast))
# exit(0)
# print(emitexpr(ast))

# print(ast)
# exit(0)
#print(ast)
# print(codegen(ast))



# exit(0)
with open("./out.json", "w") as f:
    a = str(ast).replace("'", '"').replace("None", "\"None\"")
    f.write(a)