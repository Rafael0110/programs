male(taro).
male(ichiro).
male(jiro).
male(saburo).
female(hanako).
female(sachiko).
female(tomoko).
female(yoko).
father_of(taro, ichiro).
father_of(taro, jiro).
father_of(taro, tomoko).
father_of(ichiro, saburo).
father_of(ichiro, yoko).
mother_of(hanako, ichiro).
mother_of(hanako, jiro).
mother_of(hanako, tomoko).
mother_of(sachiko, saburo).
mother_of(sachiko, yoko).

parents_of(X, Y) :- father_of(X, Y).
parents_of(X, Y) :- mother_of(X, Y).

sans_of(X, Y) :- parents_of(Y, X), male(X).
daughter_of(X, Y) :- parents_of(Y, X), female(X).

grandfather_of(X, Y) :- parents_of(Z, Y), father_of(X, Z).

all_children(X, Ls) :- children_sub(X, [], Ls).
children_sub(X, C, Ls) :- father_of(X, C1), not(member(C1, C)), !, children_sub(X, [C1 | C], Ls).
children_sub(_, Ls, Ls).

main :- all_children(X, Ls), writef('%t → %t\n', [X,Ls]).
main :- all_children(ichiro, Ls), writef('ichiro → %t\n', [Ls]).