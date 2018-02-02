move_block(From, To, Via, State, [[From | Rest1], [To, Block | Rest2], [Via | Rest3]]) :-
    member([From, Block | Rest1], State),
    member([To | Rest2], State),
    member([Via | Rest3], State).

リスト：深さ優先探索

/* 移動：move(From, To, Via) */
move(x, y, z). move(x, z, y).
move(y, x, z). move(y, z, x).
move(z, x, y). move(z, y, x).

/* 移動手順を発見 */
search_depth([State | History]) :-
    equal_state([ [x], [y], [z, red, blue, green] ], State), !,
    print_answer([State | History]).

/* 探索 */
search_depth([State | History]) :-
    move(From, To, Via),
    move_block(From, To, Via, State, NewState),
    check_state(NewState, History),
    search_depth([NewState, State | History]).


equal_state(State1, State2) :-
    member([x | X1], State1), member([x | X2], State2), X1 == X2,
    member([y | Y1], State1), member([y | Y2], State2), Y1 == Y2,
    member([z | Z1], State1), member([z | Z2], State2), Z1 == Z2.

check_state(_, []).
check_state(State1, [State2 | History]) :-
    not(equal_state(State1, State2)), check_state(State1, History).

print_answer([]) :- !.
print_answer([State | Rest]) :-
    print_answer(Rest),
    member([x | X], State), member([y | Y], State), member([z | Z], State),
    write(X), write(Y), write(Z), nl.