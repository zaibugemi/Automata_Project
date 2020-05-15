from lexer import *
from parser import *
import ply.lex as lex
import ply.yacc as yacc
import re


storage = {}

def evaluate(tree, store):
    global storage
    nodetype = tree[0]
    if nodetype == 'int':
        return int(tree[1])
    elif nodetype == 'identifier':
        return tree[1]
    elif nodetype == 'double':
        return float(tree[1])
    elif nodetype == 'char':
        return tree[1]
    elif nodetype == 'string':
        return tree[1]
    elif nodetype == 'binop':
        binop, left_exp, right_exp = tree[2], tree[1], tree[3]
        if binop == '+':
            return evaluate(left_exp, store) + evaluate(right_exp, store)
        elif binop == '-':
            return evaluate(left_exp, store) - evaluate(right_exp, store)
        elif binop == '/':
            return evaluate(left_exp, store) / evaluate(right_exp, store)
        elif binop == '*':
            return evaluate(left_exp, store) * evaluate(right_exp, store)
        elif binop == '^':
            return evaluate(left_exp, store) ** evaluate(right_exp, store)
        elif binop == '%':
            return evaluate(left_exp, store) % evaluate(right_exp, store)
        elif binop == '<=':
            return evaluate(left_exp, store) <= evaluate(right_exp, store)
        elif binop == '>=':
            return evaluate(left_exp, store) >= evaluate(right_exp, store)
        elif binop == '==':
            return evaluate(left_exp, store) == evaluate(right_exp, store)
        elif binop == '!=':
            return evaluate(left_exp, store) != evaluate(right_exp, store)
        elif binop == '<':
            return evaluate(left_exp, store) < evaluate(right_exp, store)
        elif binop == '>':
            return evaluate(left_exp, store) > evaluate(right_exp, store)
        elif binop == '&&':
            return evaluate(left_exp, store) and evaluate(right_exp, store)
        elif binop == '||':
            return evaluate(left_exp, store) or evaluate(right_exp, store)
    elif nodetype == 'NOT':
        return not(evaluate(tree[1], store))
    elif nodetype == 'assign':
        return storage
    elif nodetype == 'print':
        expression = evaluate(tree[1], store)
        return expression

mylex = lex.lex(module=lexer)
parser = yacc.yacc()

while True:
    try:
        s = input('>> ')
    except EOFError:
        break
    ptree = parser.parse(s)
    evaluation = evaluate(ptree, storage)
    print(evaluation)
