grammar gramatica1;

s : a b c
  | d e
  ;

a : DOS b TRES
  | // ε producción vacía
  ;

b : b CUATRO c CINCO
  | // ε producción vacía
  ;

c : SEIS a b
  | e
  ;

d : UNO a e
  | b
  ;

e : TRES;

DOS : 'dos';
CUATRO : 'cuatro';
SEIS : 'seis';
UNO : 'uno';
TRES : 'tres';
CINCO : 'cinco';
WS : [ \t\r\n]+ -> skip;
