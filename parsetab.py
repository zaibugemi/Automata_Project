
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftISEQUALleftLTLEGTGEleftPLUSMINUSleftMULTIPLYDIVIDErightNOTAND CHAR DECREMENT DIVIDE DOUBLE EQUAL GE GT IDENTIFIER INCREMENT INT ISEQUAL LE LPARAN LT MINUS MODULO MULTIPLY NOT NOTEQUAL OR PLUS POWER PRINT RPARAN STRINGstmt : IDENTIFIER EQUAL expstmt : PRINT LPARAN exp RPARANstmt : exp\n    exp : exp PLUS exp\n        | exp MINUS exp\n        | exp MULTIPLY exp\n        | exp DIVIDE exp\n        | exp MODULO exp\n        | exp POWER exp\n        | exp LE exp\n        | exp GE exp\n        | exp ISEQUAL exp\n        | exp NOTEQUAL exp\n        | exp LT exp\n        | exp GT exp\n        | exp AND exp\n        | exp OR expexp : LPARAN exp RPARANexp : NOT expexp : INTexp : DOUBLEexp : CHARexp : STRINGexp : IDENTIFIER'
    
_lr_action_items = {'IDENTIFIER':([0,5,6,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[2,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'PRINT':([0,],[4,]),'LPARAN':([0,4,5,6,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[5,26,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'NOT':([0,5,6,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'INT':([0,5,6,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'DOUBLE':([0,5,6,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'CHAR':([0,5,6,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'STRING':([0,5,6,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'$end':([1,2,3,7,8,9,10,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,],[0,-24,-3,-20,-21,-22,-23,-24,-19,-1,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-2,]),'EQUAL':([2,],[11,]),'PLUS':([2,3,7,8,9,10,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[-24,12,-20,-21,-22,-23,12,-24,-19,12,-4,-5,-6,-7,12,12,12,12,12,12,12,12,12,12,12,-18,]),'MINUS':([2,3,7,8,9,10,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[-24,13,-20,-21,-22,-23,13,-24,-19,13,-4,-5,-6,-7,13,13,13,13,13,13,13,13,13,13,13,-18,]),'MULTIPLY':([2,3,7,8,9,10,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[-24,14,-20,-21,-22,-23,14,-24,-19,14,14,14,-6,-7,14,14,14,14,14,14,14,14,14,14,14,-18,]),'DIVIDE':([2,3,7,8,9,10,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[-24,15,-20,-21,-22,-23,15,-24,-19,15,15,15,-6,-7,15,15,15,15,15,15,15,15,15,15,15,-18,]),'MODULO':([2,3,7,8,9,10,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[-24,16,-20,-21,-22,-23,16,-24,-19,16,-4,-5,-6,-7,16,16,-10,-11,-12,16,-14,-15,-16,-17,16,-18,]),'POWER':([2,3,7,8,9,10,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[-24,17,-20,-21,-22,-23,17,-24,-19,17,-4,-5,-6,-7,17,17,-10,-11,-12,17,-14,-15,-16,-17,17,-18,]),'LE':([2,3,7,8,9,10,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[-24,18,-20,-21,-22,-23,18,-24,-19,18,-4,-5,-6,-7,18,18,-10,-11,18,18,-14,-15,18,18,18,-18,]),'GE':([2,3,7,8,9,10,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[-24,19,-20,-21,-22,-23,19,-24,-19,19,-4,-5,-6,-7,19,19,-10,-11,19,19,-14,-15,19,19,19,-18,]),'ISEQUAL':([2,3,7,8,9,10,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[-24,20,-20,-21,-22,-23,20,-24,-19,20,-4,-5,-6,-7,20,20,-10,-11,-12,20,-14,-15,20,20,20,-18,]),'NOTEQUAL':([2,3,7,8,9,10,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[-24,21,-20,-21,-22,-23,21,-24,-19,21,-4,-5,-6,-7,21,21,-10,-11,-12,21,-14,-15,-16,-17,21,-18,]),'LT':([2,3,7,8,9,10,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[-24,22,-20,-21,-22,-23,22,-24,-19,22,-4,-5,-6,-7,22,22,-10,-11,22,22,-14,-15,22,22,22,-18,]),'GT':([2,3,7,8,9,10,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[-24,23,-20,-21,-22,-23,23,-24,-19,23,-4,-5,-6,-7,23,23,-10,-11,23,23,-14,-15,23,23,23,-18,]),'AND':([2,3,7,8,9,10,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[-24,24,-20,-21,-22,-23,24,-24,-19,24,-4,-5,-6,-7,24,24,-10,-11,-12,24,-14,-15,-16,24,24,-18,]),'OR':([2,3,7,8,9,10,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[-24,25,-20,-21,-22,-23,25,-24,-19,25,-4,-5,-6,-7,25,25,-10,-11,-12,25,-14,-15,-16,-17,25,-18,]),'RPARAN':([7,8,9,10,27,28,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[-20,-21,-22,-23,46,-24,-19,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,47,-18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'stmt':([0,],[1,]),'exp':([0,5,6,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[3,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> stmt","S'",1,None,None,None),
  ('stmt -> IDENTIFIER EQUAL exp','stmt',3,'p_stmt_assign','parser.py',53),
  ('stmt -> PRINT LPARAN exp RPARAN','stmt',4,'p_stmt_print','parser.py',57),
  ('stmt -> exp','stmt',1,'p_stmt_exp','parser.py',61),
  ('exp -> exp PLUS exp','exp',3,'p_exp_binop','parser.py',66),
  ('exp -> exp MINUS exp','exp',3,'p_exp_binop','parser.py',67),
  ('exp -> exp MULTIPLY exp','exp',3,'p_exp_binop','parser.py',68),
  ('exp -> exp DIVIDE exp','exp',3,'p_exp_binop','parser.py',69),
  ('exp -> exp MODULO exp','exp',3,'p_exp_binop','parser.py',70),
  ('exp -> exp POWER exp','exp',3,'p_exp_binop','parser.py',71),
  ('exp -> exp LE exp','exp',3,'p_exp_binop','parser.py',72),
  ('exp -> exp GE exp','exp',3,'p_exp_binop','parser.py',73),
  ('exp -> exp ISEQUAL exp','exp',3,'p_exp_binop','parser.py',74),
  ('exp -> exp NOTEQUAL exp','exp',3,'p_exp_binop','parser.py',75),
  ('exp -> exp LT exp','exp',3,'p_exp_binop','parser.py',76),
  ('exp -> exp GT exp','exp',3,'p_exp_binop','parser.py',77),
  ('exp -> exp AND exp','exp',3,'p_exp_binop','parser.py',78),
  ('exp -> exp OR exp','exp',3,'p_exp_binop','parser.py',79),
  ('exp -> LPARAN exp RPARAN','exp',3,'p_exp_paran','parser.py',84),
  ('exp -> NOT exp','exp',2,'p_exp_not','parser.py',88),
  ('exp -> INT','exp',1,'p_exp_int','parser.py',92),
  ('exp -> DOUBLE','exp',1,'p_exp_double','parser.py',96),
  ('exp -> CHAR','exp',1,'p_exp_char','parser.py',100),
  ('exp -> STRING','exp',1,'p_exp_string','parser.py',104),
  ('exp -> IDENTIFIER','exp',1,'p_exp_identifier','parser.py',108),
]
