square(X, Y) :- Y is X * X.

fact(0, 1).
fact(X, Sum) :- X > 0, X1 is X - 1, fact(X1, Sum1), Sum is X * Sum1.

first([X | _], X).
rest([_ | Ys], Ys).
add_to_list(X, Ls, [X | Ls]).

retrieve(1, [X | _], X).
retrieve(N, [_ | Ls], X) :- N > 1, N1 is N - 1, retrieve(N1, Ls, X).

insert_at(1, X, Ls, [X | Ls]).
insert_at(N, X, [Y, Ls], [Y | Zs]) :- N > 1, N1 is N - 1, insert_at(N1, X, Ls, Zs).

remove_at(1, [_ | Ls], Ls).
remove_at(N, [X | Ls], [X | Zs]) :- N > 1, N1 is N - 1, remove_at(N1, Ls, Zs).

my_length([], 0).
my_length([_ | Xs], N) :- my_length(Xs, N1), N is N1 + 1.

my_append([], Xs, Xs).
my_append([X | Ls], Ys, [X | Zs]) :- my_append(Ls, Ys, Zs).

my_reverse([],[]).
my_reverse([X | Xs], Ys) :- my_reverse(Xs, Zs), append(Zs, [X], Ys).

my_member(X, [X | _]).
my_member(X, [_ | Ls]) :- my_menber(X, Ls).

my_select(X, [X | Xs], Xs).
my_select(X, [Y | Ys], [Y | Zs]) :- my_select(X, Ys, Zs).

selects([], _).
selects([X | Xs], Ys) :- select(X, Ys, Ys1), selects(Xs, Ys1).

my_flatten([X | Xs], Ys) :- my_flatten(X, Ys1), my_flatten(Xs, Ys2), append(Ys1, Ys2, Ys).
my_flatten(X, [X]) :- atomic(X), X \== [].
my_flatten([], []).

take_integer([X | Xs], Ys) :- take_integer(X, Ys1), take_integer(Xs, Ys2), append(Ys1, Ys2, Ys).
take_integer(X, [X]) :- integer(X), !.
take_integer(_, []).

remove(_, [], []).
remove(X, [X | Xs], Zs) :- remove(X, Xs, Zs).
remove(X, [Y | Ys], [Y | Zs]) :- X \= Y, remove(X, Ys, Zs).

ticket(Age, Money) :- Age < 13, Money is 500.
ticket(_, Money) :- Money is 1000.

%% main :- take_integer([1, a, [2, b]], X), writef('%t\n', [X]).
%% main :- take_integer([1, a, [2, b]], X), write(X), nl, fail.
main :- ticket(12, Money), write(Money).