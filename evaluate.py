from parse import expr
from lex import Token, Types


def evalute(expression: expr | Token):
    if type(expression) == Token:
        return int(expression.value)
    if expression.op.type == Types.plus:
        return evalute(expression.left) + evalute(expression.right)
    elif expression.op.type == Types.minus:
        return evalute(expression.left) - evalute(expression.right)
    elif expression.op.type == Types.star:
        return evalute(expression.left) * evalute(expression.right)
    elif expression.op.type == Types.slash:
        return evalute(expression.left) / evalute(expression.right)