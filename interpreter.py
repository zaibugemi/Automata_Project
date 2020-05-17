from lexer import *
from parser import *
import ply.lex as lex
import ply.yacc as yacc
import re
import sys




mylex = lex.lex(module=lexer)
parser = yacc.yacc()

f = open(sys.argv[1],'r')
code = f.read()
ptree = parser.parse(code)
#print(ptree)

evaluate(ptree, storage)
    
