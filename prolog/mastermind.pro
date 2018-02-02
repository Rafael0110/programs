make_correct(X) :- make_correct_sub(0, [0,1,2,3,4,5,6,7,8,9], [], X).
make_correct_sub(4, _, X, X) :- !.
%% make_correct_sub(4, _, X, X) :- write([X]), nl, !. %% 答え出力
make_correct_sub(Num, List, Correct, X) :-
        Index is random(10 - Num),
        nth0(Index, List, Item),
        delete(List, Item, Rest),
        Num1 is Num + 1,
        make_correct_sub(Num1, Rest, [Item | Correct], X).

input_numbers(Numbers) :-
    repeat,
    format('Input 4 Numbers > '),
    read(Numbers),
    length(Numbers, 4),
    check_numbers(Numbers),
    !.

check_numbers([]).
check_numbers([N | Rest]) :-
    integer(N),
    0 =< N,
    N =< 9,
    not(member(N, Rest)),
    check_numbers(Rest).

count_bulls(Correct, Data, C) :- count_bulls_sub(Correct, Data, 0, C).
count_bulls_sub([], [], C, C).
count_bulls_sub([X1 | L1], [X2 | L2], N, C) :-
    (X1 =:= X2 -> N1 is N + 1 ; N1 is N),
    count_bulls_sub(L1, L2, N1, C).

count_same_number(Correct, Data, C) :- count_same_sub(Correct, Data, 0, C).
count_same_sub([], _, C, C).
count_same_sub([X | L], Data, N, C) :-
    (member(X, Data) -> N1 is N + 1; N1 is N),
    count_same_sub(L, Data, N1, C).

play(11, Correct) :-
    format('Game Over, Correct is '), write(Correct), nl, !.
play(N, Correct) :-
    N > 0,
    input_numbers(Numbers),
    count_bulls(Numbers, Correct, Bulls),
    count_same_number(Numbers, Correct, Sames),
    Cows is Sames - Bulls,
    format('~d: Bulls is ~d, Cows is ~d~n', [N, Bulls, Cows]),
    N1 is N + 1,
    (Bulls =:= 4 -> format('Good!!~n') ; play(N1, Correct)).

mastermind :-
    make_correct(Correct),
    format('***** Master Mind *****~n'),
    play(1, Correct).


selects([], _).
selects([X | Xs], Ys) :- select(X, Ys, Ys1), selects(Xs, Ys1).

guess(Code) :-
    selects([X1,X2,X3,X4], [0,1,2,3,4,5,6,7,8,9]),
    Code = [X1,X2,X3,X4].

check(Code) :-
    query(OldCode, Bulls, Cows),
    count_bulls(OldCode, Code, Bulls1),
    count_same_number(OldCode, Code, N),
    Cows1 is N - Bulls1,
    (Bulls =\= Bulls1 ; Cows =\= Cows1).

cleanup :-
    assert(query(0,0,0)),
    retractall(query(X, Y, Z)).

ask(Correct, Code) :-
    write(Code),
    count_bulls(Correct, Code, Bulls),
    count_same_number(Correct, Code, N),
    Cows is N - Bulls,
    assert(query(Code, Bulls, Cows)),
    format(' bulls = ~d, Cows = ~d~n', [Bulls, Cows]),
    Bulls =:= 4.

mastermind_ask :-
    input_numbers(Correct),
    cleanup,
    guess(Code),
    not(check(Code)),
    ask(Correct, Code),
    format('Good!!~n'),
    !.

ask_ai(Code) :-
    write(Code), nl,
    format('Input bulls > '),
    read(Bulls),
    format('Input cows > '),
    read(Cows),
    assert(query(Code, Bulls, Cows)),
    Bulls =:= 4.

mastermind_ai :-
    cleanup,
    guess(Code),
    not(check(Code)),
    ask_ai(Code),
    format('Good!!~n'),
    !.