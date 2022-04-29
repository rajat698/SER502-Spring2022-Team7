spec_char('!').
spec_char('\\').
spec_char('#').
spec_char('$').
spec_char('&').
spec_char('(').
spec_char(')').
spec_char('*').
spec_char('+').
spec_char(',').
spec_char('-').
spec_char('.').
spec_char('/').
spec_char(':').
spec_char(';').
spec_char('<').
spec_char('=').
spec_char('>').
spec_char('?').
spec_char('@').
spec_char('~').

datatype('int').
datatype('str').
datatype('bool').


boolean('True').
boolean('False').

%:-use_rendering(svgtree).
:-table expr/3, expr2/3, expr3/3, bool_expr/3, bool_expr2/3.

% numbers
num(num(pos,N1)) --> [N], {atom_number(N, N1)}.
num(num(neg,N1)) --> ['-'], [N], {atom_number(N, N1)}.
num(num(pos,N1)) --> ['+'], [N], {atom_number(N, N1)}.



% strings
string(str(T)) --> ['\"'], [T], ['\"'], {atom_chars(T, TList), char(TList, [])}.
char --> [].
char --> [A], char, {is_alpha(A)}.
char --> [A], char, {atom_number(A, _)}.
char --> [A], char, {spec_char(A)}.

% identifiers
id(id(T)) --> [T], {atom_chars(T, TList), isIdentifier(TList, [])}.
isIdentifier --> [A], id_suffix, {is_alpha(A)}.
id_suffix --> [].
id_suffix --> [A], id_suffix, {is_alpha(A)}.
id_suffix --> [N], id_suffix, {atom_number(N, _)}.

% arithmetic expressions
expr(t_add(T1,T2)) --> expr(T1), ['+'], expr2(T2).
expr(t_sub(T1,T2)) --> expr(T1), ['-'], expr2(T2).
expr(T) --> expr2(T).

expr2(t_mul(T1,T2)) --> expr2(T1), ['*'], expr3(T2).
expr2(t_div(T1,T2)) --> expr2(T1), ['/'], expr3(T2).
expr2(t_mod(T1,T2)) --> expr2(T1), ['%'], expr3(T2).
expr2(T) --> expr3(T).

expr3(T) --> num(T).
expr3(T) --> id(T).
expr3(T) --> ['('], expr(T) , [')'].

% boolean expressions

bool_expr(or(T1,T2)) --> bool_expr(T1), ['or'], bool_expr2(T2).
bool_expr(T) --> bool_expr2(T).

bool_expr2(and(T1,T2)) --> bool_expr2(T1), ['and'], bool_expr3(T2).
bool_expr2(T) --> bool_expr3(T).

% equality (boolean)
bool_expr3(equals(T1,T2)) -->  bool_expr(T1), ['=='], bool_expr(T2).
bool_expr3(equals(T1,T2)) --> expr(T1), ['=='], expr(T2).
bool_expr3(equals(T1,T2)) --> id(T1), ['=='], value(T2).

% arithmetic comparison (boolean)
bool_expr3(lt(T1,T2)) --> expr(T1), ['<'], expr(T2).
bool_expr3(gt(T1,T2)) --> expr(T1), ['>'], expr(T2). 
bool_expr3(lteq(T1,T2)) --> expr(T1), ['<='], expr(T2). 
bool_expr3(gteq(T1,T2)) --> expr(T1), ['>='], expr(T2).

bool_expr3(T) -->['('], bool_expr(T), [')'].
bool_expr3(not(T)) --> ['not'], bool_expr(T).
bool_expr3(T) --> bool(T).
bool(T) --> [T], {boolean(T)}.

% statements
stmt_list(T) --> stmt(T), [';'].
stmt_list(T) --> stmt_block(T).
stmt_list(stmt_list(T1,T2)) --> stmt(T1), [';'], stmt_list(T2).
stmt_list(stmt_list(T1,T2)) --> stmt_block(T1), stmt_list(T2).



% declarations
value(T) --> bool_expr(T).
value(T) --> expr(T).
value(T) --> string(T).
stmt(dec(T1,T2)) --> [T1], id(T2), {datatype(T1)}.
stmt(decAssign(T1,T2,T3)) --> [T1], id(T2), ['='], value(T3), {datatype(T1)}.

% display
stmt(display(T)) --> ['display'], value(T).

% assignment
stmt(assign(T1,T2)) --> id(T1), ['='], value(T2).
stmt(addAssign(T1,T2)) --> id(T1), ['+='], expr(T2).
stmt(subAssign(T1,T2)) --> id(T1), ['-='], expr(T2).
stmt(mulAssign(T1,T2)) --> id(T1), ['*='], expr(T2).
stmt(divAssign(T1,T2)) --> id(T1), ['/='], expr(T2).




% ternary if-else
stmt(ifelse(T1,T2,T3)) --> bool_expr(T1), ['?'], stmt(T2), [':'], stmt(T3), [';'].

% if-else block
stmt_block(ifelse(T1,T2,T3)) --> ['if'], 
    ['('], bool_expr(T1), [')'], 
    ['{'], stmt_list(T2), ['}'],
    ['else'],
    ['{'], stmt_list(T3), ['}'].

% for-loop traditional
stmt_block(forT(T1,T2,T3,T4)) --> ['for-loop', '('], 
    stmt(T1), [';'], bool_expr(T2), [';'], stmt(T3), [')', '{'],
    stmt_list(T4), ['}'].

% for-loop range
stmt_block(forR(T1,T2,T3,T4)) --> ['for-loop', '('],
    id(T1), ['in', 'range', '('], expr(T2), [','], expr(T3), [')', '{'],
    stmt_list(T4), ['}'].

% program
program(T) --> ['shuru'], stmt_list(T), ['khatam'].

    




