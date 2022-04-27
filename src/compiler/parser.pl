boolean('True').
boolean('False').

:-use_rendering(svgtree).
:-table expr/3, expr2/3, expr3/3, bool_expr/3, bool_expr2/3.

% numbers
num(N1) --> [N], {atom_number(N, N1)}.

% identifiers
id(id(T)) --> [T], {atom_chars(T, TList), isIdentifier(TList, [])}.
isIdentifier --> [A], id_suffix, {is_alpha(A)}.
id_suffix --> [].
id_suffix --> [A], id_suffix, {is_alpha(A)}.
id_suffix --> [N], id_suffix, {atom_number(N, _)}.

% arithmetic expressions
expr(+(T1,T2)) --> expr(T1), [+], expr2(T2).
expr(-(T1,T2)) --> expr(T1), [-], expr2(T2).
expr(T) --> expr2(T).

expr2(*(T1,T2)) --> expr2(T1), [*], expr3(T2).
expr2(/(T1,T2)) --> expr2(T1), [/], expr3(T2).
expr2(mod(T1,T2)) --> expr2(T1), ['%'], expr3(T2).
expr2(T) --> expr3(T).

expr3(T) --> num(T).
expr3(T) --> id(T).
expr3(T) --> ['('], expr(T) , [')'].

% boolean expressions

bool_expr(or(T1,T2)) --> bool_expr(T1), [or], bool_expr2(T2).
bool_expr(T) --> bool_expr2(T).

bool_expr2(and(T1,T2)) --> bool_expr2(T1), [and], bool_expr3(T2).
bool_expr2(T) --> bool_expr3(T).

% ==
bool_expr3(equals(T1,T2)) -->  bool_expr(T1), [==], bool_expr(T2).


bool_expr3(T) -->['('], bool_expr(T), [')'].
bool_expr3(not(T)) --> [not], bool_expr(T).


% < > 
bool(T) --> [T], {boolean(T)}.


