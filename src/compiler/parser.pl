digit(0).
digit(1).
digit(2).
digit(3).
digit(4).
digit(5).
digit(6).
digit(7).
digit(8).
digit(9).

:-use_rendering(svgtree).
:-table expr/3, expr2/3.

num(N) --> [N], {number(N)}.
%num(num(T, N)) --> num(T), [N], {digit(N)}.

expr(+(T1,T2)) --> expr(T1), [+], expr2(T2).
expr(-(T1,T2)) --> expr(T1), [-], expr2(T2).
expr(T) --> expr2(T).

expr2(*(T1,T2)) --> expr2(T1), [*], expr3(T2).
expr2(/(T1,T2)) --> expr2(T1), [/], expr3(T2).
expr2('%'(T1,T2)) --> expr2(T1), ['%'], expr3(T2).
expr2(T) --> expr3(T).

expr3(T) --> num(T).
%expr3(T) --> id(T).
expr3(T) --> ['('], expr(T) , [')'].
