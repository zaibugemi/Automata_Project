import ply.lex as lex
import re

t_ignore = ' \t'

tokens = (
    'INT',
    'DOUBLE',
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
    'LANGLE',
    'RANGLE',
    'LANGLEEQUAL',
    'RANGLEEQUAL',
    'NOTEQUAL',
    'ISEQUAL',
    'NOT',
    'AND',
    'OR',

)

def t_DOUBLE(t):
    r'[0-9]+[.][0-9]+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_CHAR(t):
    r'[a-zA-Z]'
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

def t_LANGLEEQUAL(t):
    r'<='
    return t

def t_RANGLEEQUAL(t):
    r'>='
    return t

def t_LANGLE(t):
    r'<'
    return t

def t_RANGLE(t):
    r'>'
    return t

def t_NOTEQUAL(t):
    r'!='
    return t

def t_NOT(t):
    r'!'
    return t

def t_AND(t):
    r'&&'
    return t

def t_OR(t):
    r'\|\|'
    return t

def t_ISEQUAL(t):
    r'=='
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


