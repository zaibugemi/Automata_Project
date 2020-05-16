from lexer import *
from parser import *
import ply.lex as lex
import ply.yacc as yacc
import re




mylex = lex.lex(module=lexer)
parser = yacc.yacc()

code = ''''''

ptree = parser.parse(code)
# print(ptree)

evaluate(ptree, storage)
    
