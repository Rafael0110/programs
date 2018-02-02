if(Test, Then, _) :- Test, ! , Then.
if(_, _, Else) :- Else.

not(X) :- X, !, fail.
not(_).

remove(_, [], []).
remove(X, [X | Xs], Zs) :- remove(X, Xs, Zs).
remove(X, [Y | Ys], [Y | Zs]) :- X \= Y, remove(X, Ys, Zs).

echo :- repeat, read(X), echo_sub(X), !.
echo_sub(X) :- X == end_of_file, !.
echo_sub(X) :- write(X), nl, fail.

yes_or_no(X) :- write('yes_or_no > '), read(X), (X == yes ; X == no), !.

my_between(L, H, L) :- L =< H.
my_between(L, H, V) :- L < H, L1 is L + 1, between(L1, H, V).

my_reverese([],[]).
my_reverese([X | Xs], Ys) :- my_reverese(Xs, Zs), append(Zs, [X], Ys).

new_reverese(Xs, Ys) :- new_reverese(Xs, [], Ys).
new_reverese([], Xs, Xs).
new_reverese([X | Xs], As, Ys) :- new_reverese(Xs, [X | As], Ys).

quick([X | Xs], Ys) :-
	partition(Xs, X, Littles, Bigs),
	quick(Littles, Ls),
	quick(Bigs, Bs),
	append(Ls, [X | Bs], Ys).
quick([],[]).

quick1(Xs, Ys) :- quick_sub(Xs, [Ys, []]).
quick_sub([X | Xs], [Ys, Zs]) :-
  partition(Xs, X, Littles, Bigs),
  quick_sub(Littles, [Ys, [X | Ys1]]),
  quick_sub(Bigs, [Ys1, Zs]).
quick_sub([], [Xs, Xs]).

partition([X | Xs], Y, [X | Ls], Bs) :- X =< Y, partition(Xs, Y, Ls, Bs).
partition([X | Xs], Y, Ls, [X | Bs]) :- X > Y,  partition(Xs, Y, Ls, Bs).
partition([], _, [], []).

set_gvar(Name, X) :- nonvar(Name), retract(gvar(Name, Val)), !, asserta(gvar(Name, X)).
set_gvar(Name, X) :- nonvar(Name), asserta(gvar(Name, X)).

enqueue(Item, [Qh, [Item | Qt]], [Qh, Qt]).
dequeue(Item, [[Item | Qh], Qt], [Qh, Qt]).
empty([X, Y]) :- X == Y.