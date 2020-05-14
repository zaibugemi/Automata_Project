from lexer import *
from parser import *
import ply.lex as lex
import ply.yacc as yacc
import re

def eval_exp(tree):
    nodetype = tree[0]
    if nodetype == 'int':
        return int(tree[1])
    elif nodetype == 'double':
        return float(tree[1])
    elif nodetype == 'binop':
        binop, left_exp, right_exp = tree[2], tree[1], tree[3]
        if binop == '+':
            return eval_exp(left_exp) + eval_exp(right_exp)
        elif binop == '-':
            return eval_exp(left_exp) - eval_exp(right_exp)
        elif binop == '/':
            return eval_exp(left_exp) / eval_exp(right_exp)
        elif binop == '*':
            return eval_exp(left_exp) * eval_exp(right_exp)
        elif binop == '^':
            return eval_exp(left_exp) ** eval_exp(right_exp)
        elif binop == '%':
            return eval_exp(left_exp) % eval_exp(right_exp)
        elif binop == '<=':
            return eval_exp(left_exp) <= eval_exp(right_exp)
        elif binop == '>=':
            return eval_exp(left_exp) >= eval_exp(right_exp)
        elif binop == '==':
            return eval_exp(left_exp) == eval_exp(right_exp)
        elif binop == '!=':
            return eval_exp(left_exp) != eval_exp(right_exp)
        elif binop == '<':
            return eval_exp(left_exp) < eval_exp(right_exp)
        elif binop == '>':
            return eval_exp(left_exp) > eval_exp(right_exp)
        elif binop == '&&':
            return eval_exp(left_exp) and eval_exp(right_exp)
        elif binop == '||':
            return eval_exp(left_exp) or eval_exp(right_exp)
    elif nodetype == 'NOT':
        return not(eval_exp(tree[1]))

mylex = lex.lex(module=lexer)
parser = yacc.yacc()

while True:
    try:
        s = input('>> ')
    except EOFError:
        break
    ptree = parser.parse(s)
    print(ptree)
    evaluation = eval_exp(ptree)
    print(evaluation)
