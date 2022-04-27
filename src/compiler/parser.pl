:-use_rendering(svgtree).
:-table expr/3, expr2/3, expr3/3.

num(N1) --> [N], {atom_number(N, N1)}.
%num(num(T, N)) --> num(T), [N], {digit(N)}.

id(id(T)) --> [T], {atom_chars(T, TList), isIdentifier(TList, [])}.
isIdentifier --> [A], id_suffix, {is_alpha(A)}.
id_suffix --> [].
id_suffix --> [A], id_suffix, {is_alpha(A)}.
id_suffix --> [N], id_suffix, {atom_number(N, _)}.


expr(+(T1,T2)) --> expr(T1), ['%'], expr2(T2).
expr(T) --> expr2(T).

expr2(+(T1,T2)) --> expr2(T1), [+], expr3(T2).
expr2(-(T1,T2)) --> expr2(T1), [-], expr3(T2).
expr2(T) --> expr3(T).

expr3(*(T1,T2)) --> expr3(T1), [*], expr4(T2).
expr3(/(T1,T2)) --> expr3(T1), [/], expr4(T2).
expr3(T) --> expr4(T).

expr4(T) --> num(T).
expr4(T) --> id(T).
expr4(T) --> ['('], expr(T) , [')'].


