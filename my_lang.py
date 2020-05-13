import my_tokens
import ply.lex as lex
import ply.yacc as yacc
import re


tokens = (
    'INT',          #done
    'DOUBLE',       #done
    'CHAR',
    # 'STRING',
    # 'BOOL',
    'PLUS',         #done
    'MINUS',        #done
    'DIVIDE',       #done
    'MULTIPLY',     #done
    'POWER',        #done
    'MODULO',       #done
    'INCREMENT',    #done
    'DECREMENT',    #done
    'LANGLE',       #done
    'RANGLE',       #done
    'LANGLEEQUAL',  #done
    'RANGLEEQUAL',  #done
    'NOTEQUAL',     #done
    'ISEQUAL',      #done
    'NOT',
    'AND',          
    'OR',

)



def p_exp_binop(p):
    '''
    exp : exp PLUS exp
        | exp MINUS exp
        | exp MULTIPLY exp
        | exp DIVIDE exp
        | exp MODULO exp
        | exp POWER exp
        | exp LANGLEEQUAL exp
        | exp RANGLEEQUAL exp
        | exp ISEQUAL exp
        | exp NOTEQUAL exp
        | exp LANGLE exp
        | exp RANGLE exp
        | exp AND exp
        | exp OR exp
        '''
    p[0] = ("binop", p[1], p[2], p[3])


def p_exp_NOT(p):
    'exp : NOT exp'
    p[0] = ("NOT", p[1])


def p_exp_int(p):
    'exp : INT'
    p[0] = ("int",p[1])

def p_exp_double(p):
    'exp : DOUBLE'
    p[0] = ("double",p[1])


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

mylex = lex.lex(module=my_tokens)
parser = yacc.yacc()

while True:
    try:
        s = input('>> ')
    except EOFError:
        break
    ptree = parser.parse(s)
    evaluation = eval_exp(ptree)
    print(evaluation)
