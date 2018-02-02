%% ハノイの塔
hanoi(1, From, To, _) :- write([From, to, To]), nl.
hanoi(N, From, To, Via) :-
	N1 is N - 1, hanoi(N1, From, Via, To),
	write([From, to, To]), nl,
	hanoi(N1, Via, To, From).

%% ハノイの塔　みやすい
format_hanoi(1, From, To, _) :- format('~a to ~a~n',[From, To]).
format_hanoi(N, From, To, Via) :-
	N1 is N - 1, format_hanoi(N1, From, Via, To),
	format('~a to ~a~n',[From, To]),
	format_hanoi(N1, Via, To, From).

%% ８クイーン
perm([],[]).
perm(Xs, [Z | Zs]) :- select(Z, Xs, Ys), perm(Ys, Zs).

queen(Q) :- perm([1,2,3,4,5,6,7,8], Q), safe(Q).

safe([Qt | Qr]) :- not(attack(Qt, Qr)), safe(Qr).
safe([]).

attack(X, Xs) :- attack_sub(X, 1, Xs).
attack_sub(X, N, [Y|_ ]) :- (X =:= Y + N ; X =:= Y - N).
attack_sub(X, N, [_|Ys]) :- N1 is N + 1, attack_sub(X, N1, Ys).

%% ８クイーン高速化
queen_f(Q) :- queen_sub([1,2,3,4,5,6,7,8], [], Q).

queen_sub(L, SafeQs, Q) :-
  select(X, L, RestQs),
  not(attack(X, SafeQs)),
  queen_sub(RestQs, [X | SafeQs], Q).
queen_sub([], Q, Q).

make_correct(X) :- make_correct_sub(0, [0,1,2,3,4,5,6,7,8,9], [], X).
make_correct_sub(4, _, X, X) :- !.
make_correct_sub(Num, List, Correct, X) :-
  Index is random(10 - Num),
  nth0(Index, List, Item),
  delete(List, Item, Rest),
  Num1 is Num + 1,
  make_correct_sub(Num1, Rest, [Item | Correct], X).

input_numbers(Numbers) :-
  repeat,
  format('Input 4 Numbers > '),
  format('Input 4 Numbers > '),
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


%% 農夫と山羊と狼とキャベツ
move([F, G, W, C], [NF, G, W, C])  :- (F == left -> NF = right ; NF = left).
move([F, F, W, C], [NF, NF, W, C]) :- (F == left -> NF = right ; NF = left).
move([F, G, F, C], [NF, G, NF, C]) :- (F == left -> NF = right ; NF = left).
move([F, G, W, F], [NF, G, W, NF]) :- (F == left -> NF = right ; NF = left).

safeFGWC([F, G, W, C]) :- safe_cabbage(F, G, C), safe_goat(F, G, W).
safe_cabbage(F, _, C) :- F == C.
safe_cabbage(_, G, C) :- G \== C.
safe_goat(F, G, _) :- F == G.
safe_goat(_, G, W) :- G \== W.

depth_search([State | History]) :-
  State == [right, right, right, right], !, print_answer([State | History]).

depth_search([State | History]) :-
  move(State, NewState),
  safeFGWC(NewState),
  not(member(NewState, History)),
  depth_search([NewState, State | History]).

print_answer([]) :- !.
print_answer([State | Rest]) :- print_answer(Rest), write(State), nl.

%% 地図の配色問題
selects_colors([], _).
selects_colors([X | Xs], Ys) :- select(X, Ys, Ys1), selects_colors(Xs, Ys1).

make_next(Colors) :- selects_colors([A, B], Colors), assert(next(A, B)), fail.

color_map(A, B, C, D, E, F) :-
  not(make_next([red, blue, yellow, green])),
  next(A, B), next(A, C), next(A, D),
  next(B, C), next(B, E),
  next(C, D), next(C, E), next(C, F),
  next(D, F),
  next(E, F).


%% ライツアウト
pattern(0, 0x0000023). pattern(1, 0x0000047). pattern(2, 0x000008e). pattern(3, 0x000011c).
pattern(4, 0x0000218). pattern(5, 0x0000461). pattern(6, 0x00008e2). pattern(7, 0x00011c4).
pattern(8, 0x0002388). pattern(9, 0x0004310). pattern(10, 0x0008c20). pattern(11, 0x0011c40).
pattern(12, 0x0023880). pattern(13, 0x0047100). pattern(14, 0x0086200). pattern(15, 0x0118400).
pattern(16, 0x0238800). pattern(17, 0x0471000). pattern(18, 0x08e2000). pattern(19, 0x10c4000).
pattern(20, 0x0308000). pattern(21, 0x0710000). pattern(22, 0x0e20000). pattern(23, 0x1c40000).
pattern(24, 0x1880000).

solve(Board) :-
    between(0, 31, N),
    push_button(N, 0, Board, NewBoard),
    clear_light(5, NewBoard, Result, N, PushPattern),
    Result == 0,
    print_answer(PushPattern).

push_button(_, 5, Board, Board) :- !.

push_button(N, M, Board, Result) :-
    ((1 << M) /\ N) > 0,          % ビットオンならばボタンを押す
    pattern(M, Pattern),
    NewBoard is Board xor Pattern,
    M1 is M + 1, !, push_button(N, M1, NewBoard, Result).

push_button(N, M, Board, Result) :-
    M1 is M + 1, push_button(N, M1, Board, Result).































