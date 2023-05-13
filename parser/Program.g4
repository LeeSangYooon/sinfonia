grammar Program;
 
prog: first+;
 
first: 
    class_decl
    | func_decl
    | statement;

class_decl: 
    'class ' ID '{' (func_decl | class_var_decl)* '}';


func_decl: func_type func_head block;

func_type: '#' ID (',' ID)* '->' ID;
func_head: ID ID*;
block: '{' statement* '}';

class_var_decl: ID ID ';';

statement: var_decl
    |if_stat
    |for_stat
    |while_stat
    |(func_call ';')
    |set_stat;

var_decl: 'let' ID ID ('=' expr)? ';';
if_stat: 'if' expr block;
for_stat: 'for' expr 'in' expr block;
while_stat: 'while' expr block;
set_stat: expr '=' expr ';';


// Define a new rule for logical operations
condition: term (OR term)*;
term: factor (AND factor)*;
factor: comparison | '(' condition ')' /* | expr */;
comparison: expr COMPARISON_OPERATOR expr;
AND: 'and';
OR: 'or';
COMPARISON_OPERATOR: '<=' | '>=' | '<' | '>' | '==';


condition_value: ('('  condition ')');


expr     : (multExpr (('+' | '-') multExpr)*); //added
multExpr : atom ('*' atom)* ;
atom: literal
    | '(' expr ')' 
    | condition_value
    | func_call
    | class_object
    ;

func_call: ID (expr)*;
class_object: ID ('.' ID)+;
 
literal : INT;
ID      : [a-zA-Z]+ ;
INT     : [0-9]+ ;
NEWLINE : '\r'? '\n' -> skip;
WS      : [ \t]+ -> skip ;