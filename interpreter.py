from lexer import *
from parser import *
import ply.lex as lex
import ply.yacc as yacc
import re




mylex = lex.lex(module=lexer)
parser = yacc.yacc()

code = '''INT z = 2; DOUBLE fl = 2.8; CHAR a = "b"; z = 4; z = 6; z = 8; a = "k"; a = "w";fl = 2.999999;z; a;fl'''

ptree = parser.parse(code)
# print(ptree)

evaluate(ptree, storage)
    
