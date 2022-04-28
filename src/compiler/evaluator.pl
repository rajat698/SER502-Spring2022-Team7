
:- table expr/3, expr2/3, expr3/3.



% arithmetic expressions
eval_expression(+(T1, T2), Env, Result) :- eval_expression(T1, Env, R1), eval_expression(T2, Env, R2), Result is R1+R2.
eval_expression(-(T1, T2), Env, Result) :- eval_expression(X, Env, R1), eval_expression(T2, Env, R2), Result is R1-R2.
eval_expression(*(T1, T2), Env, Result) :- eval_expression(X, Env, R1), eval_expression(T2, Env, R2), Result is R1*R2.
eval_expression(mod(T1, T2), Env, Result) :- eval_expression(X, Env, R1), eval_expression(T2, Env, R2), Result is R1%R2.



% boolean expressions

eval_expression(t_boolean_expression(T1, t_boolean_operator(Operator), T2), Env, Result) :-
    eval_expression(T1, Env, R1),
    eval_expression(T2, Env, R2),
    eval_boolean(R1,  Operator, R2, Result).

eval_boolean(true , and, true  , true).
eval_boolean(true , and, false , false).
eval_boolean(false , and, true  , false).
eval_boolean(false , and, false , false).
eval_boolean(true , or , true  , true).
eval_boolean(true , or , false , true).
eval_boolean(false , or , true  , true).
eval_boolean(false , or , false , false).


% for-loop range
eval_command(forR(T1, T2, T3, T4), Env, NewEnv) :-
    eval_command(t_assignment_expression(T1, T2), Env, E1),
    eval_condition(t_condition(T2, t_comparison_operator(>), T3), E1, false),
    eval_for_command(t_condition(T1, t_comparison_operator(=<), T3), t_pre_increment(Variable), T4, E1, NewEnv).

eval_command(forR(T1, T2, T3, T4), Env, NewEnv) :-
    eval_command(t_assignment_expression(T1, T2), Env, E1),
    eval_condition(t_condition(T2, t_comparison_operator(<), T3), E1, false),
    eval_for_command(t_condition(T1, t_comparison_operator(>=), T3), t_pre_decrement(Variable), T4, E1, NewEnv).


eval_comparison(V1, t_comparison_operator(>), V2, true)  :- V1 > V2.
eval_comparison(V1, t_comparison_operator(>), V2, false)  :- V1 =< V2.
eval_comparison(V1, t_comparison_operator(<), V2, true)  :- V1 < V2.
eval_comparison(V1, t_comparison_operator(<), V2, false)  :- V1 >= V2.
eval_comparison(V1, t_comparison_operator(>=), V2, true)  :- V1 >= V2.
eval_comparison(V1, t_comparison_operator(>=), V2, false) :- V1 < V2.
eval_comparison(V1, t_comparison_operator(=<), V2, true)  :- V1 =< V2.
eval_comparison(V1, t_comparison_operator(=<), V2, false) :- V1 > V2.

eval_comparison(V1, t_comparison_operator(==), V2, true)  :- V1 =:= V2.
eval_comparison(V1, t_comparison_operator(==), V2, false) :- V1 =\= V2. 