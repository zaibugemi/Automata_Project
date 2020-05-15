import ply.lex as lex
import re

t_ignore = ' \t'

tokens = (
    'INT',
    'DOUBLE',
    'CHAR',
    'STRING',
    'IDENTIFIER',
    'COMMA',
    # 'BOOL',
    # 'TRUE',
    # 'FALSE',
    'PLUS',         #done
    'MINUS',        #done
    'DIVIDE',       #done
    'MULTIPLY',     #done
    'POWER',        #done
    'MODULO',       #done
    'INCREMENT',    #done
    'DECREMENT',    #done
    'LT',
    'GT',
    'LE',
    'GE',
    'EQUAL',
    'NOTEQUAL',
    'ISEQUAL',
    'NOT',
    'AND',
    'OR',
    'LPARAN',
    'RPARAN',
    'PRINT',
)

def t_error(t):
    print('Unrecognized token "%s"' % t.value)
    t.lexer.skip(1) 

# def t_BOOL(t):
#     r'TRUE|FALSE'
#     return t

def t_COMMA(t):
    r'\,'
    return t
    
def t_PRINT(t):
    r'PRINT'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z]+(:?_[a-zA-Z])*'
    return t

def t_ISEQUAL(t):
    r'\=\='
    return t

def t_EQUAL(t):
    r'\='
    return t

def t_LPARAN(t):
    r'\('
    return t

def t_RPARAN(t):
    r'\)'
    return t

def t_DOUBLE(t):
    r'[0-9]+[.][0-9]+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_CHAR(t):
    r"'[a-zA-Z]'"
    t.value = t.value[1:-1]
    return t

    
def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t


def t_INCREMENT(t):
    r'\+\+'
    return t

def t_DECREMENT(t):
    r'\-\-'
    return t

def t_PLUS(t):
    r'\+'
    return t

def t_MINUS(t):
    r'\-'
    return t

def t_MULTIPLY(t):
    r'\*'
    return t

def t_DIVIDE(t):
    r'\/'
    return t

def t_POWER(t):
    r'\^'
    return t

def t_MODULO(t):
    r'\%'
    return t

def t_LE(t):
    r'\<\='
    return t

def t_GE(t):
    r'\>\='
    return t

def t_LT(t):
    r'\<'
    return t

def t_GT(t):
    r'\>'
    return t

def t_NOTEQUAL(t):
    r'\!\='
    return t

def t_NOT(t):
    r'\!'
    return t

def t_AND(t):
    r'\&\&'
    return t

def t_OR(t):
    r'\|\|'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


