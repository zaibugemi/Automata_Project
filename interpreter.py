from lexer import *
from parser import *
import ply.lex as lex
import ply.yacc as yacc
import re




mylex = lex.lex(module=lexer)
parser = yacc.yacc()

code = '''"Zuhiab"; 1 + 2; (2 * 9) / 3; z = 23; a = "shahi"; PRINT("zuhaib", 1+2, "3 times dildar"); "I am Ahmedabadi"'''

ptree = parser.parse(code)
# print(ptree)

evaluate(ptree, storage)
    
