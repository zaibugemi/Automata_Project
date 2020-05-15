import lexer
import ply.lex as lex
import ply.yacc as yacc
import re

precedence = (
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'ISEQUAL'),
        ('left', 'LT', 'LE', 'GT', 'GE'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'MULTIPLY', 'DIVIDE'),
        ('right', 'NOT'),
)

tokens = (
    'INT',          #done
    'DOUBLE',       #done
    'CHAR',
    'STRING',
    'IDENTIFIER',
    # 'BOOL',
    'PLUS',         #done
    'MINUS',        #done
    'DIVIDE',       #done
    'MULTIPLY',     #done
    'POWER',        #done
    'MODULO',       #done
    'INCREMENT',    #done
    'DECREMENT',    #done
    'LT',           #done
    'GT',           #done
    'LE',           #done
    'GE',           #done
    'EQUAL',
    'NOTEQUAL',     #done
    'ISEQUAL',      #done
    'NOT',
    'AND',          #done
    'OR',            #done
    'LPARAN',
    'RPARAN',
    'PRINT',
)




# def p_exp_empty(p):
#     p[0] = ''

def p_stmt_assign(p):
    'stmt : IDENTIFIER EQUAL exp'
    p[0] = ("assign", p[1], p[3])

def p_stmt_print(p):
    'stmt : PRINT LPARAN exp RPARAN'
    p[0] = ("print", p[3])

def p_stmt_exp(p):
    'stmt : exp'
    p[0] = p[1]

def p_exp_binop(p):
    '''
    exp : exp PLUS exp
        | exp MINUS exp
        | exp MULTIPLY exp
        | exp DIVIDE exp
        | exp MODULO exp
        | exp POWER exp
        | exp LE exp
        | exp GE exp
        | exp ISEQUAL exp
        | exp NOTEQUAL exp
        | exp LT exp
        | exp GT exp
        | exp AND exp
        | exp OR exp'''
    p[0] = ("binop", p[1], p[2], p[3])


def p_exp_paran(p):
    'exp : LPARAN exp RPARAN'
    p[0] = p[2]

def p_exp_not(p):
    'exp : NOT exp'
    p[0] = ("NOT", p[2])

def p_exp_int(p):
    'exp : INT'
    p[0] = ("int",p[1])

def p_exp_double(p):
    'exp : DOUBLE'
    p[0] = ("double",p[1])

def p_exp_char(p):
    'exp : CHAR'
    p[0] = ("char", p[1])

def p_exp_string(p):
    'exp : STRING'
    p[0] = ("string", p[1])

def p_exp_identifier(p):
    'exp : IDENTIFIER'
    p[0] = ("identifier", p[1])

# def p_stmt_exp(p):
#     's : exp'
#     p[0] = p[1]

def p_error(p):
    if p == None:
        token = "end of file"
    else:
        token = f"{p.type}({p.value}) on line {p.lineno}"

    print(f"Syntax error: Unexpected {token}")