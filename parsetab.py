
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftISEQUALleftLTLEGTGEleftPLUSMINUSleftMULTIPLYDIVIDErightNOTAND BOOL CHAR COMMA DECREMENT DIVIDE DOUBLE EQUAL GE GT IDENTIFIER INCREMENT INT ISEQUAL LE LPARAN LT MINUS MODULO MULTIPLY NOT NOTEQUAL OR PLUS POWER PRINT RPARAN SEMICOLON STRING VARTYPEline : stmtsstmts : stmt\n             | stmt SEMICOLON stmts\n    stmt : expstmt : VARTYPE IDENTIFIER EQUAL expstmt : PRINT LPARAN exps RPARANexps : exp\n            | exp COMMA exps\n    \n    exp : exp PLUS exp\n        | exp MINUS exp\n        | exp MULTIPLY exp\n        | exp DIVIDE exp\n        | exp MODULO exp\n        | exp POWER exp\n        | exp LE exp\n        | exp GE exp\n        | exp ISEQUAL exp\n        | exp NOTEQUAL exp\n        | exp LT exp\n        | exp GT exp\n        | exp AND exp\n        | exp OR expexp : LPARAN exp RPARANexp : NOT expexp : INTexp : DOUBLEexp : CHARexp : STRINGexp : BOOLexp : IDENTIFIER'
    
_lr_action_items = {'VARTYPE':([0,15,],[5,5,]),'PRINT':([0,15,],[7,7,]),'LPARAN':([0,7,8,9,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31,49,55,],[8,31,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'NOT':([0,8,9,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31,49,55,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'INT':([0,8,9,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31,49,55,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'DOUBLE':([0,8,9,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31,49,55,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'CHAR':([0,8,9,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31,49,55,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'STRING':([0,8,9,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31,49,55,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'BOOL':([0,8,9,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31,49,55,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'IDENTIFIER':([0,5,8,9,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31,49,55,],[6,30,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'$end':([1,2,3,4,6,10,11,12,13,14,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54,],[0,-1,-2,-4,-30,-25,-26,-27,-28,-29,-24,-3,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-5,-6,]),'SEMICOLON':([3,4,6,10,11,12,13,14,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54,],[15,-4,-30,-25,-26,-27,-28,-29,-24,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-5,-6,]),'PLUS':([4,6,10,11,12,13,14,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,],[16,-30,-25,-26,-27,-28,-29,16,-24,-9,-10,-11,-12,16,16,16,16,16,16,16,16,16,16,16,-23,16,]),'MINUS':([4,6,10,11,12,13,14,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,],[17,-30,-25,-26,-27,-28,-29,17,-24,-9,-10,-11,-12,17,17,17,17,17,17,17,17,17,17,17,-23,17,]),'MULTIPLY':([4,6,10,11,12,13,14,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,],[18,-30,-25,-26,-27,-28,-29,18,-24,18,18,-11,-12,18,18,18,18,18,18,18,18,18,18,18,-23,18,]),'DIVIDE':([4,6,10,11,12,13,14,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,],[19,-30,-25,-26,-27,-28,-29,19,-24,19,19,-11,-12,19,19,19,19,19,19,19,19,19,19,19,-23,19,]),'MODULO':([4,6,10,11,12,13,14,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,],[20,-30,-25,-26,-27,-28,-29,20,-24,-9,-10,-11,-12,20,20,-15,-16,-17,20,-19,-20,-21,-22,20,-23,20,]),'POWER':([4,6,10,11,12,13,14,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,],[21,-30,-25,-26,-27,-28,-29,21,-24,-9,-10,-11,-12,21,21,-15,-16,-17,21,-19,-20,-21,-22,21,-23,21,]),'LE':([4,6,10,11,12,13,14,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,],[22,-30,-25,-26,-27,-28,-29,22,-24,-9,-10,-11,-12,22,22,-15,-16,22,22,-19,-20,22,22,22,-23,22,]),'GE':([4,6,10,11,12,13,14,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,],[23,-30,-25,-26,-27,-28,-29,23,-24,-9,-10,-11,-12,23,23,-15,-16,23,23,-19,-20,23,23,23,-23,23,]),'ISEQUAL':([4,6,10,11,12,13,14,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,],[24,-30,-25,-26,-27,-28,-29,24,-24,-9,-10,-11,-12,24,24,-15,-16,-17,24,-19,-20,24,24,24,-23,24,]),'NOTEQUAL':([4,6,10,11,12,13,14,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,],[25,-30,-25,-26,-27,-28,-29,25,-24,-9,-10,-11,-12,25,25,-15,-16,-17,25,-19,-20,-21,-22,25,-23,25,]),'LT':([4,6,10,11,12,13,14,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,],[26,-30,-25,-26,-27,-28,-29,26,-24,-9,-10,-11,-12,26,26,-15,-16,26,26,-19,-20,26,26,26,-23,26,]),'GT':([4,6,10,11,12,13,14,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,],[27,-30,-25,-26,-27,-28,-29,27,-24,-9,-10,-11,-12,27,27,-15,-16,27,27,-19,-20,27,27,27,-23,27,]),'AND':([4,6,10,11,12,13,14,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,],[28,-30,-25,-26,-27,-28,-29,28,-24,-9,-10,-11,-12,28,28,-15,-16,-17,28,-19,-20,-21,28,28,-23,28,]),'OR':([4,6,10,11,12,13,14,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,],[29,-30,-25,-26,-27,-28,-29,29,-24,-9,-10,-11,-12,29,29,-15,-16,-17,29,-19,-20,-21,-22,29,-23,29,]),'RPARAN':([6,10,11,12,13,14,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,50,51,52,56,],[-30,-25,-26,-27,-28,-29,52,-24,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,54,-7,-23,-8,]),'COMMA':([6,10,11,12,13,14,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,],[-30,-25,-26,-27,-28,-29,-24,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,55,-23,]),'EQUAL':([30,],[49,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'line':([0,],[1,]),'stmts':([0,15,],[2,34,]),'stmt':([0,15,],[3,3,]),'exp':([0,8,9,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31,49,55,],[4,32,33,4,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,53,51,]),'exps':([31,55,],[50,56,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> line","S'",1,None,None,None),
  ('line -> stmts','line',1,'p_stmt_multiline','parser.py',55),
  ('stmts -> stmt','stmts',1,'p_stmt_end','parser.py',59),
  ('stmts -> stmt SEMICOLON stmts','stmts',3,'p_stmt_end','parser.py',60),
  ('stmt -> exp','stmt',1,'p_stmt_exp','parser.py',68),
  ('stmt -> VARTYPE IDENTIFIER EQUAL exp','stmt',4,'p_stmt_assign','parser.py',72),
  ('stmt -> PRINT LPARAN exps RPARAN','stmt',4,'p_stmt_print','parser.py',76),
  ('exps -> exp','exps',1,'p_stmt_many_exps','parser.py',80),
  ('exps -> exp COMMA exps','exps',3,'p_stmt_many_exps','parser.py',81),
  ('exp -> exp PLUS exp','exp',3,'p_exp_binop','parser.py',90),
  ('exp -> exp MINUS exp','exp',3,'p_exp_binop','parser.py',91),
  ('exp -> exp MULTIPLY exp','exp',3,'p_exp_binop','parser.py',92),
  ('exp -> exp DIVIDE exp','exp',3,'p_exp_binop','parser.py',93),
  ('exp -> exp MODULO exp','exp',3,'p_exp_binop','parser.py',94),
  ('exp -> exp POWER exp','exp',3,'p_exp_binop','parser.py',95),
  ('exp -> exp LE exp','exp',3,'p_exp_binop','parser.py',96),
  ('exp -> exp GE exp','exp',3,'p_exp_binop','parser.py',97),
  ('exp -> exp ISEQUAL exp','exp',3,'p_exp_binop','parser.py',98),
  ('exp -> exp NOTEQUAL exp','exp',3,'p_exp_binop','parser.py',99),
  ('exp -> exp LT exp','exp',3,'p_exp_binop','parser.py',100),
  ('exp -> exp GT exp','exp',3,'p_exp_binop','parser.py',101),
  ('exp -> exp AND exp','exp',3,'p_exp_binop','parser.py',102),
  ('exp -> exp OR exp','exp',3,'p_exp_binop','parser.py',103),
  ('exp -> LPARAN exp RPARAN','exp',3,'p_exp_paran','parser.py',108),
  ('exp -> NOT exp','exp',2,'p_exp_not','parser.py',112),
  ('exp -> INT','exp',1,'p_exp_int','parser.py',116),
  ('exp -> DOUBLE','exp',1,'p_exp_double','parser.py',120),
  ('exp -> CHAR','exp',1,'p_exp_char','parser.py',124),
  ('exp -> STRING','exp',1,'p_exp_string','parser.py',128),
  ('exp -> BOOL','exp',1,'p_exp_bool','parser.py',132),
  ('exp -> IDENTIFIER','exp',1,'p_exp_identifier','parser.py',136),
]
