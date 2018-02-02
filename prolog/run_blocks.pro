on(space,d).
on(d,a).
on(a,b).
on(b,c).
on(c,table).
on(space,table).
result(t).

if(Test, Then, _) :- Test, !, Then.
if(_ , _ , Else) :- Else.

look :- on(X,Y), write([X,Y]), nl, fail.

move(X,Y,Z) :-
	on(space,X), on(X,Y), on(space,Z),
	X \== Y, Y \== Z, Z \== X,
	assert(on(X,Z)),
	if(Y \== table,assert(on(space,Y)),true),
	retract(on(X,Y)),
	if(Z \== table,retract(on(space,Z)),true),
	if(result(t),true,assert(result(t))).

count(X) :-
	tables(Ls),
	length(Ls,X),
	retract(result(t)).
tables(Ls) :- find_table([], Ls).
find_table(L, Ls) :-
  on(X, table), not(member(X, L)), !,
  find_table([X | L], Ls).
find_table(Ls, Ls).

repea(X,Y,Z) :- move(X,Z,Y), fail.

judge :-
	on(space,d),
	on(d,b),
	on(b,c),
	on(c,a),
	on(a,table),
	on(space,table).

main(2) :- judge.
main(_) :-
	move(X,Y,Z),
	if(result(t),count(N),repea(X,Y,Z)),
	main(N), format('move ~a from ~a to ~a ~n',[X,Y,Z]).