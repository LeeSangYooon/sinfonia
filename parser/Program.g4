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
    |set_stat
    |assignment_stat;

var_decl: ID ID ('=' expr)? ';';
if_stat: 'if' (expr | condition) block 
        elif*
        else?;
for_stat: 'for' class_object 'in' expr block;
while_stat: 'while' (expr | condition) block;
set_stat: class_object '=' expr ';';
assignment_stat: class_object ASSIGNMENT_OPERATOR expr ';';


elif: ( 'elif' (expr | condition) block );
else: ( 'else' block );

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
multExpr : atom (('*' | '/') atom)* ;
atom: literal
    | '(' expr ')' 
    | condition_value
    | func_call
    | class_object
    ;

func_args: ('(' (expr (',' expr)*)? ')');
func_call: (class_object func_args+) | return_func;
return_func: 'return' expr;
class_object: ID ('.' ID)*;
 
literal : INT | STR | BOOLEAN;
BOOLEAN : TRUE | FALSE;
TRUE    : 'true';
FALSE   : 'false';
ASSIGNMENT_OPERATOR: PLUS_EQUALS | MINUS_EQUALS | TIMES_EQUALS | DIVIDE_EQUALS;
PLUS_EQUALS : '+=';
MINUS_EQUALS : '-=';
TIMES_EQUALS : '*=';
DIVIDE_EQUALS : '/=';
ID      : [a-zA-Z_]+[0-9_]* ;
INT     : [0-9]+ ;
STR     : '"' .*? '"';
COMMENT : '//' .*? ('\n' | EOF) -> skip;
NEWLINE : '\r'? '\n' -> skip;
WS      : [ \t]+ -> skip ;