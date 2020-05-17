
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftISEQUALleftLTLEGTGEleftPLUSMINUSleftMULTIPLYDIVIDEleftPOWERrightNOTAND BOOL CHAR COMMA DECREMENT DIVIDE DOT DOUBLE EQUAL GE GT IDENTIFIER INCREMENT INT ISEQUAL LBRACE LE LPARAN LT MINUS MODULO MULTIPLY NOT NOTEQUAL OR PLUS POWER PRINT RBRACE RPARAN SEMICOLON STRING STRUCT VARTYPEline : stmtsstmts : stmt SEMICOLON\n             | stmt SEMICOLON stmts\n    \n    stmt : IDENTIFIER IDENTIFIER\n    \n    stmt : IDENTIFIER DOT IDENTIFIER EQUAL exp\n    \n    stmt : STRUCT IDENTIFIER LBRACE assignments RBRACE\n    \n    assignments : VARTYPE IDENTIFIER SEMICOLON\n                | VARTYPE IDENTIFIER SEMICOLON assignments\n    stmt : expstmt : VARTYPE IDENTIFIER EQUAL expstmt : IDENTIFIER EQUAL expstmt : PRINT LPARAN exps RPARANexps : exp\n            | exp COMMA exps\n    stmt : IDENTIFIER INCREMENTstmt : IDENTIFIER DECREMENTexp : MINUS IDENTIFIER\n    exp : exp PLUS exp\n        | exp MINUS exp\n        | exp MULTIPLY exp\n        | exp DIVIDE exp\n        | exp MODULO exp\n        | exp POWER exp\n        | exp LE exp\n        | exp GE exp\n        | exp ISEQUAL exp\n        | exp NOTEQUAL exp\n        | exp LT exp\n        | exp GT exp\n        | exp AND exp\n        | exp OR expexp : LPARAN exp RPARANexp : NOT expexp : INTexp : DOUBLEexp : CHARexp : STRINGexp : BOOLexp : IDENTIFIER'
    
_lr_action_items = {'IDENTIFIER':([0,4,6,7,9,10,11,17,19,20,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,62,66,68,71,],[4,18,37,38,41,42,41,4,45,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,74,41,]),'STRUCT':([0,17,],[6,6,]),'VARTYPE':([0,17,61,76,],[7,7,68,68,]),'PRINT':([0,17,],[8,8,]),'MINUS':([0,4,5,9,11,12,13,14,15,16,17,20,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,40,41,42,43,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,64,65,66,69,71,72,],[10,-39,24,10,10,-34,-35,-36,-37,-38,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,24,-39,-17,-33,24,-18,-19,-20,-21,24,-23,24,24,24,24,24,24,24,24,10,24,-32,10,24,10,24,]),'LPARAN':([0,8,9,11,17,20,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,62,66,71,],[9,39,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'NOT':([0,9,11,17,20,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,62,66,71,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'INT':([0,9,11,17,20,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,62,66,71,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'DOUBLE':([0,9,11,17,20,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,62,66,71,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'CHAR':([0,9,11,17,20,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,62,66,71,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'STRING':([0,9,11,17,20,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,62,66,71,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'BOOL':([0,9,11,17,20,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,62,66,71,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'$end':([1,2,17,44,],[0,-1,-2,-3,]),'SEMICOLON':([3,4,5,12,13,14,15,16,18,21,22,41,42,43,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,65,69,70,72,73,74,],[17,-39,-9,-34,-35,-36,-37,-38,-4,-15,-16,-39,-17,-33,-11,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-10,-12,-5,-6,76,]),'DOT':([4,],[19,]),'EQUAL':([4,38,45,],[20,62,66,]),'INCREMENT':([4,],[21,]),'DECREMENT':([4,],[22,]),'PLUS':([4,5,12,13,14,15,16,40,41,42,43,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,64,65,69,72,],[-39,23,-34,-35,-36,-37,-38,23,-39,-17,-33,23,-18,-19,-20,-21,23,-23,23,23,23,23,23,23,23,23,23,-32,23,23,]),'MULTIPLY':([4,5,12,13,14,15,16,40,41,42,43,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,64,65,69,72,],[-39,25,-34,-35,-36,-37,-38,25,-39,-17,-33,25,25,25,-20,-21,25,-23,25,25,25,25,25,25,25,25,25,-32,25,25,]),'DIVIDE':([4,5,12,13,14,15,16,40,41,42,43,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,64,65,69,72,],[-39,26,-34,-35,-36,-37,-38,26,-39,-17,-33,26,26,26,-20,-21,26,-23,26,26,26,26,26,26,26,26,26,-32,26,26,]),'MODULO':([4,5,12,13,14,15,16,40,41,42,43,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,64,65,69,72,],[-39,27,-34,-35,-36,-37,-38,27,-39,-17,-33,27,-18,-19,-20,-21,27,-23,-24,-25,-26,27,-28,-29,-30,-31,27,-32,27,27,]),'POWER':([4,5,12,13,14,15,16,40,41,42,43,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,64,65,69,72,],[-39,28,-34,-35,-36,-37,-38,28,-39,-17,-33,28,28,28,28,28,28,-23,28,28,28,28,28,28,28,28,28,-32,28,28,]),'LE':([4,5,12,13,14,15,16,40,41,42,43,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,64,65,69,72,],[-39,29,-34,-35,-36,-37,-38,29,-39,-17,-33,29,-18,-19,-20,-21,29,-23,-24,-25,29,29,-28,-29,29,29,29,-32,29,29,]),'GE':([4,5,12,13,14,15,16,40,41,42,43,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,64,65,69,72,],[-39,30,-34,-35,-36,-37,-38,30,-39,-17,-33,30,-18,-19,-20,-21,30,-23,-24,-25,30,30,-28,-29,30,30,30,-32,30,30,]),'ISEQUAL':([4,5,12,13,14,15,16,40,41,42,43,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,64,65,69,72,],[-39,31,-34,-35,-36,-37,-38,31,-39,-17,-33,31,-18,-19,-20,-21,31,-23,-24,-25,-26,31,-28,-29,31,31,31,-32,31,31,]),'NOTEQUAL':([4,5,12,13,14,15,16,40,41,42,43,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,64,65,69,72,],[-39,32,-34,-35,-36,-37,-38,32,-39,-17,-33,32,-18,-19,-20,-21,32,-23,-24,-25,-26,32,-28,-29,-30,-31,32,-32,32,32,]),'LT':([4,5,12,13,14,15,16,40,41,42,43,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,64,65,69,72,],[-39,33,-34,-35,-36,-37,-38,33,-39,-17,-33,33,-18,-19,-20,-21,33,-23,-24,-25,33,33,-28,-29,33,33,33,-32,33,33,]),'GT':([4,5,12,13,14,15,16,40,41,42,43,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,64,65,69,72,],[-39,34,-34,-35,-36,-37,-38,34,-39,-17,-33,34,-18,-19,-20,-21,34,-23,-24,-25,34,34,-28,-29,34,34,34,-32,34,34,]),'AND':([4,5,12,13,14,15,16,40,41,42,43,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,64,65,69,72,],[-39,35,-34,-35,-36,-37,-38,35,-39,-17,-33,35,-18,-19,-20,-21,35,-23,-24,-25,-26,35,-28,-29,-30,35,35,-32,35,35,]),'OR':([4,5,12,13,14,15,16,40,41,42,43,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,64,65,69,72,],[-39,36,-34,-35,-36,-37,-38,36,-39,-17,-33,36,-18,-19,-20,-21,36,-23,-24,-25,-26,36,-28,-29,-30,-31,36,-32,36,36,]),'RPARAN':([12,13,14,15,16,40,41,42,43,47,48,49,50,51,52,53,54,55,56,57,58,59,60,63,64,65,75,],[-34,-35,-36,-37,-38,65,-39,-17,-33,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,70,-13,-32,-14,]),'COMMA':([12,13,14,15,16,41,42,43,47,48,49,50,51,52,53,54,55,56,57,58,59,60,64,65,],[-34,-35,-36,-37,-38,-39,-17,-33,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,71,-32,]),'LBRACE':([37,],[61,]),'RBRACE':([67,76,77,],[73,-7,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'line':([0,],[1,]),'stmts':([0,17,],[2,44,]),'stmt':([0,17,],[3,3,]),'exp':([0,9,11,17,20,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,62,66,71,],[5,40,43,5,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,64,69,72,64,]),'exps':([39,71,],[63,75,]),'assignments':([61,76,],[67,77,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> line","S'",1,None,None,None),
  ('line -> stmts','line',1,'p_stmt_multiline','parser.py',57),
  ('stmts -> stmt SEMICOLON','stmts',2,'p_stmt_end','parser.py',62),
  ('stmts -> stmt SEMICOLON stmts','stmts',3,'p_stmt_end','parser.py',63),
  ('stmt -> IDENTIFIER IDENTIFIER','stmt',2,'p_struct_variable','parser.py',72),
  ('stmt -> IDENTIFIER DOT IDENTIFIER EQUAL exp','stmt',5,'p_struct_members_init','parser.py',78),
  ('stmt -> STRUCT IDENTIFIER LBRACE assignments RBRACE','stmt',5,'p_struct','parser.py',84),
  ('assignments -> VARTYPE IDENTIFIER SEMICOLON','assignments',3,'p_struct_initialisation','parser.py',91),
  ('assignments -> VARTYPE IDENTIFIER SEMICOLON assignments','assignments',4,'p_struct_initialisation','parser.py',92),
  ('stmt -> exp','stmt',1,'p_stmt_exp','parser.py',100),
  ('stmt -> VARTYPE IDENTIFIER EQUAL exp','stmt',4,'p_stmt_assign','parser.py',104),
  ('stmt -> IDENTIFIER EQUAL exp','stmt',3,'p_stmt_change','parser.py',108),
  ('stmt -> PRINT LPARAN exps RPARAN','stmt',4,'p_stmt_print','parser.py',112),
  ('exps -> exp','exps',1,'p_stmt_many_exps','parser.py',116),
  ('exps -> exp COMMA exps','exps',3,'p_stmt_many_exps','parser.py',117),
  ('stmt -> IDENTIFIER INCREMENT','stmt',2,'p_stmt_increment','parser.py',125),
  ('stmt -> IDENTIFIER DECREMENT','stmt',2,'p_stmt_decrement','parser.py',129),
  ('exp -> MINUS IDENTIFIER','exp',2,'p_exp_neg_number','parser.py',133),
  ('exp -> exp PLUS exp','exp',3,'p_exp_binop','parser.py',138),
  ('exp -> exp MINUS exp','exp',3,'p_exp_binop','parser.py',139),
  ('exp -> exp MULTIPLY exp','exp',3,'p_exp_binop','parser.py',140),
  ('exp -> exp DIVIDE exp','exp',3,'p_exp_binop','parser.py',141),
  ('exp -> exp MODULO exp','exp',3,'p_exp_binop','parser.py',142),
  ('exp -> exp POWER exp','exp',3,'p_exp_binop','parser.py',143),
  ('exp -> exp LE exp','exp',3,'p_exp_binop','parser.py',144),
  ('exp -> exp GE exp','exp',3,'p_exp_binop','parser.py',145),
  ('exp -> exp ISEQUAL exp','exp',3,'p_exp_binop','parser.py',146),
  ('exp -> exp NOTEQUAL exp','exp',3,'p_exp_binop','parser.py',147),
  ('exp -> exp LT exp','exp',3,'p_exp_binop','parser.py',148),
  ('exp -> exp GT exp','exp',3,'p_exp_binop','parser.py',149),
  ('exp -> exp AND exp','exp',3,'p_exp_binop','parser.py',150),
  ('exp -> exp OR exp','exp',3,'p_exp_binop','parser.py',151),
  ('exp -> LPARAN exp RPARAN','exp',3,'p_exp_paran','parser.py',155),
  ('exp -> NOT exp','exp',2,'p_exp_not','parser.py',159),
  ('exp -> INT','exp',1,'p_exp_int','parser.py',163),
  ('exp -> DOUBLE','exp',1,'p_exp_double','parser.py',167),
  ('exp -> CHAR','exp',1,'p_exp_char','parser.py',171),
  ('exp -> STRING','exp',1,'p_exp_string','parser.py',175),
  ('exp -> BOOL','exp',1,'p_exp_bool','parser.py',179),
  ('exp -> IDENTIFIER','exp',1,'p_exp_identifier','parser.py',183),
]
