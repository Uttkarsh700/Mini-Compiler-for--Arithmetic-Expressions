grammar Arithmetic;

prog: stmt EOF;

stmt: expr                    # ExprStmt
    | ID '=' expr            # AssignStmt
    ;

expr: expr ('*' | '/') expr  # MulDiv
    | expr ('+' | '-') expr  # AddSub
    | '(' expr ')'           # Parens
    | ID                     # Variable
    | NUMBER                 # Number
    ;

ID: [a-zA-Z][a-zA-Z0-9]*;
NUMBER: [0-9]+ ('.' [0-9]+)?;
WS: [ \t\r\n]+ -> skip; 