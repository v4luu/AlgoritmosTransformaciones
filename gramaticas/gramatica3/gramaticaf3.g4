grammar gramaticaf3;

s : a b c
  | s UNO
  ;

a : DOS b c
  | // ε producción vacía
  ;

b : c TRES 
  | // ε producción vacía
  ;

c : CUATRO b
  | // ε producción vacía
  ;


DOS : 'dos';
CUATRO : 'cuatro';
SEIS : 'seis';
UNO : 'uno';
TRES : 'tres';
CINCO : 'cinco';
WS : [ \t\r\n]+ -> skip;

