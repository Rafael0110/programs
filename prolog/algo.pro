%% coding: utf-8

%% card(Player, Hand, Color, Number).
%%	| Player : プレイヤ番号
%%	| Hand	 : 手札の昇順番号
%%	| Color	 : カードの色
%%	| Number : カードの数字

%% -------------- Defined Functions --------------
if(Test, Then, _) :- Test, !, Then.
if(_ , _ , Else) :- Else.

ifif(Test1, Then1, _, _, _) :- Test1, !, Then1.
ifif(_, _, Test2, Then2, _) :- Test2, !, Then2.
ifif(_, _, _, _, Else) :- Else.


card(P,H,C,N) :- if(H == 0, H1 is H, H1 is H - 1),
								 card(P1,H1,C1,N1), .
%% card自体にルールを設ける
%% 	1 : 自分より左のカードよりかは大きく，自分より右のカードよりかは小さい
%%  2 : 隣のカードの数がわからないときは，もう１つ隣を参照する
%%	3 : 発言で得られたカード情報は除外する
%% 発言は「誰が」「どこに」「何を」発言したかを持つ　失敗した場合だけクロージャを持つ
%% 発言した「誰が」は高確率で「何を」を持っていない
%% 「どこに」に「何を」は絶対に含まれていない

assert_data(end_of_file).
assert_data(X) :- drip(X,P,H,C,N), integer(N), retractall(card(_,_,C,N)), assert(X), !.
assert_data(X) :- write(X), nl, assert(X).

read_data(X) :-
	see(X),
	repeat,
	read(Y),
	assert_data(Y),
	Y = end_of_file,
	!,
	seen.
readd :- read_data('tsume_q03.dat').

%% -------------- Original Functions --------------
drip(card(P,H,C,N),P,H,C,N).

make :- between(0,11,N), member(C,[b,w]),
				assert(card(_,_,C,N)),
				N == 11, C == w.

add_info(X) :- drip(X,P,H,C,N).

players :- between(0,3,P), card(P,H,C,N), cards(P,H,C,N), fail.
cards(P,H,C,N) :-
		integer(P),
		integer(H),
		if(integer(N),
			format('[~d,~d] ~a,~d~n',[P,H,C,N]),
			format('[~d,~d] ~a,  ~n',[P,H,C])).

allcard :-  member(C,[b,w]), between(0,11,N),
			card(P,H,C1,N1), C == C1, N == N1, allcard(P,H,C,N).
allcard(P,H,C,N) :- integer(H), write([P,H,C,N]), nl, !, fail.
allcard(_,_,C,N) :- write([-,-,C,N]), nl, fail.

main :- make, readd, allcard.