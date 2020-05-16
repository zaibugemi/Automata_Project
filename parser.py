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
    'VARTYPE',
    'INT',          #done
    'DOUBLE',       #done
    'CHAR',
    'STRING',
    'BOOL',
    'IDENTIFIER',
    'COMMA',
    'SEMICOLON',
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


def p_stmt_multiline(p):
    'line : stmts'
    p[0] = ("statements", p[1])

def p_stmt_end(p):
    '''stmts : stmt
             | stmt SEMICOLON stmts
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_stmt_exp(p):
    'stmt : exp'
    p[0] = p[1]

def p_stmt_assign(p):
    'stmt : VARTYPE IDENTIFIER EQUAL exp'
    p[0] = ("assign", p[1],p[2],p[4])

def p_stmt_print(p):
    'stmt : PRINT LPARAN exps RPARAN'
    p[0] = ("printexps",p[3])

def p_stmt_many_exps(p):
    '''exps : exp
            | exp COMMA exps
    '''
    if len(p) == 2: 
        p[0] = [p[1]]
    else: 
        p[0] = [p[1]] + p[3]

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

def p_exp_bool(p):
    'exp : BOOL'
    p[0] = ("bool", p[1])

def p_exp_identifier(p):
    'exp : IDENTIFIER'
    p[0] = ("identifier", p[1])

def p_error(p):
    if p == None:
        token = "end of file"
    else:
        token = f"{p.type}({p.value}) on line {p.lineno}"

    print(f"Syntax error: Unexpected {token}")

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
    elif nodetype == 'bool':
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
        var_type = tree[1]
        var_name = tree[2]
        var_value = tree[3]
        if var_type == 'STRING':
            if type(var_value[1]) is str:
                storage[var_name] = var_value
            else:
                print('INVALID ASSIGNMENT STATEMENT')
        elif var_type == 'INT':
            if type(var_value[1]) is int:
                storage[var_name] = var_value
            else:
                print('INVALID ASSIGNMENT STATEMENT')
        elif var_type == 'CHAR':
            if type(var_value[1]) is str and len(var_name) == 1:
                storage[var_name] = var_value
            else:
                print('INVALID ASSIGNMENT STATEMENT')
        elif var_type == 'DOUBLE':
            if type(var_value[1]) is float:
                storage[var_name] = var_value
            else:
                print('INVALID ASSIGNMENT STATEMENT')
        elif var_type == 'BOOL':
            if var_value[1] == 'TRUE':
                storage[var_name] = True
            elif var_value[1] == 'FALSE':
                storage[var_name] = False
            else:
                print('INVALID ASSIGNMENT STATEMENT')
    elif nodetype == 'printexps':
        exp_list = tree[1]
        for exp in exp_list:
            print(evaluate(exp,storage),end=" ")
        print()
    elif nodetype == 'statements':
        stmts_list = tree[1]
        for stmt in stmts_list:
            result = evaluate(stmt, storage)
            if result is not None:
                print(result)
        