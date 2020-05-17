import lexer
import ply.lex as lex
import ply.yacc as yacc
import re
import sys

precedence = (
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'ISEQUAL'),
        ('left', 'LT', 'LE', 'GT', 'GE'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'MULTIPLY', 'DIVIDE'),
        ('left', 'POWER'),
        ('right', 'NOT'),
)

tokens = (
    'DOT',
    'STRUCT',
    'LBRACE',
    'RBRACE',
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
    '''stmts : stmt SEMICOLON
             | stmt SEMICOLON stmts
    '''
    if len(p) == 3:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_struct_variable(p):
    '''
    stmt : IDENTIFIER IDENTIFIER
    '''
    p[0] = ('declarestruct', p[1], p[2])

def p_struct_members_init(p):
    '''
    stmt : IDENTIFIER DOT IDENTIFIER EQUAL exp
    '''
    p[0] = ('initmember', p[1], p[3], p[5])

def p_struct(p):
    '''
    stmt : STRUCT IDENTIFIER LBRACE assignments RBRACE
    '''
    p[0] = ('initstruct', p[2], p[4])


def p_struct_initialisation(p):
    '''
    assignments : VARTYPE IDENTIFIER SEMICOLON
                | VARTYPE IDENTIFIER SEMICOLON assignments
    '''
    if len(p) == 4:
        p[0] = [[p[1],p[2]]]
    else:
        p[0] = [[p[1],p[2]]] + p[4]

def p_stmt_exp(p):
    'stmt : exp'
    p[0] = p[1]

def p_stmt_assign(p):
    'stmt : VARTYPE IDENTIFIER EQUAL exp'
    p[0] = ("assign", p[1],p[2],p[4])

def p_stmt_change(p):
    'stmt : IDENTIFIER EQUAL exp'
    p[0] = ("change", p[1],p[3])

def p_stmt_print(p):
    'stmt : PRINT LPARAN exps RPARAN'
    p[0] = ("printexps",p[3])

def p_struct_print(p):
    'stmt : PRINT LPARAN IDENTIFIER DOT IDENTIFIER RPARAN'
    p[0] = ("printstruct", p[3], p[5])

def p_stmt_many_exps(p):
    '''exps : exp
            | exp COMMA exps
    '''
    if len(p) == 2: 
        p[0] = [p[1]]
    else: 
        p[0] = [p[1]] + p[3]

def p_stmt_increment(p):
    '''stmt : IDENTIFIER INCREMENT'''
    p[0] = ('increment', p[1])

def p_stmt_decrement(p):
    '''stmt : IDENTIFIER DECREMENT'''
    p[0] = ('decrement', p[1])

def p_exp_neg_number(p):
    '''exp : MINUS IDENTIFIER'''
    p[0] = ('negate', p[2])

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
structure = {}

def evaluate(tree, store):
    global storage
    nodetype = tree[0]
    if nodetype == 'int':
        return int(tree[1])
    elif nodetype == 'identifier':
        var = tree[1]
        if var in storage:
            return storage[var][1]
        else:
            return var
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
        var_name = tree[2]
        if var_name in storage:
            print("RedeclarationError")
            sys.exit()
        else:
            var_type = tree[1]
            var_value = evaluate(tree[3], store)
            if var_type == 'STRING':
                if type(var_value) is str:
                    storage[var_name] = [str,var_value]
                else:
                    print('Invalid assignment')
                    sys.exit()
            elif var_type == 'INT':
                if type(var_value) is int:
                    storage[var_name] = [int,var_value]
                else:
                    print('Invalid assignment')
                    sys.exit()
            elif var_type == 'CHAR':
                if type(var_value) is str and len(var_name) == 1:
                    storage[var_name] = [str,var_value]
                else:
                    print('Invalid assignment')
                    sys.exit()
            elif var_type == 'DOUBLE':
                if type(var_value) is float:
                    storage[var_name] = [float,var_value]
                else:
                    print('Invalid assignment')
                    sys.exit()
            elif var_type == 'BOOL':
                if var_value == 'TRUE':
                    storage[var_name] = [bool,True]
                elif var_value == 'FALSE':
                    storage[var_name] = [bool,False]
                else:
                    print('Invalid assignment')
                    sys.exit()
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
    elif nodetype == 'change':
        var_name = tree[1]
        var_val = tree[2]
        if var_name not in storage:
            print('variable "{}" does not exist'.format(var_name))
            sys.exit()
        else:
            var_type = type(tree[2][1])
            if storage[var_name][0] == var_type:
                storage[var_name][1] = var_val[1]
            else:
                print("types do not match")
                sys.exit()
    elif nodetype == 'increment':
        var_name = tree[1]
        if var_name in storage and type(storage[var_name][1]) is int:
            storage[var_name][1] = storage[var_name][1] + 1
        else:
            print('variable "{}" does not exist'.format(var_name))
            sys.exit()
    elif nodetype == 'decrement':
        var_name = tree[1]
        if var_name in storage and type(storage[var_name][1]) is int:
            storage[var_name][1] = storage[var_name][1] - 1
        else:
            print('variable "{}" does not exist'.format(var_name))
            sys.exit()
    elif nodetype == 'negate':
        var_name = tree[1]
        if var_name not in storage:
            print('variable "{}" does not exist'.format(var_name))
            sys.exit()
        else:
            if type(storage[var_name][1]) is float or type(storage[var_name][1]) is int:
                return -storage[var_name][1]
    elif nodetype == 'initstruct':
        struct_name = tree[1]
        if struct_name in storage:
            print('A struct by name {} already exists'.format(struct_name))
            sys.exit()
        else:
            global structure
            temp_struct = []
            type_map = {'STRING':str, 'INT':int, 'BOOL':bool, 'DOUBLE':float, 'CHAR':str }
            for i in range(len(tree[2])):
                temp_struct.append([tree[2][i][1],type_map[tree[2][i][0]]])
            structure[struct_name] = temp_struct
    elif nodetype == 'declarestruct':
        struct_type = tree[1]
        struct_name = tree[2]
        if struct_type not in structure:
            print('A struct by name {} does not exist'.format(struct_type))
            sys.exit()
        else:
            if struct_name in storage:
                print("RedeclarationError")
                sys.exit()
            else:
                temp_strct = {}
                for i in range(len(structure[struct_type])):
                    temp_strct[structure[struct_type][i][0]]=None
                storage[struct_name] = temp_strct
    elif nodetype == 'initmember':
        struct_name = tree[1]
        struct_member = tree[2]
        member_val = evaluate(tree[3],store)
        if struct_name not in storage:
            print('variable "{}" does not exist'.format(var_name))
            sys.exit()
        else:
            if struct_member not in store[struct_name]:
                print("AttributeError")
                sys.exit()
            store[struct_name][struct_member] = member_val
    elif nodetype == 'printstruct' 
