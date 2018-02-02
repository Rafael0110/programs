neighbor(a, b).  neighbor(a, f).  neighbor(a, e).
neighbor(b, f).  neighbor(b, c).  neighbor(c, d).
neighbor(c, g).  neighbor(e, f).  neighbor(e, h).
neighbor(f, g).  neighbor(f, i).  neighbor(f, j).
neighbor(g, j).  neighbor(h, i).  neighbor(i, j).
neighbor(j, k).

next(X, Y) :- neighbor(X, Y).
next(X, Y) :- neighbor(Y, X).


%% -------- 深さ優先探索 --------
depth_search(End, End, Path) :- reverse([End | Path], Path1), write(Path1), nl, !, fail.
depth_search(Node, End, Path) :-
    not(member(Node, Path)),
    next(Node, Next),
    depth_search(Next, End, [Node | Path]).

depth_search_new(End, End, Path, Ans) :- reverse([End | Path], Ans).
depth_search_new(Node, End, Path, Ans) :-
    not(member(Node, Path)),
    next(Node, Next),
    depth_search_new(Next, End, [Node | Path], Ans).


%% -------- 幅優先探索 --------
extend_path(N, Goal) :-
    path(N, Path),
    N1 is N + 1,
    extend_one_path(N1, Goal, Path).

/* 経路をひとつ延ばす */
extend_one_path(N, Goal, [Goal | Node], Ans) :- reverse([Goal | Node], Ans).

extend_one_path(N, Goal, [Node | Rest], Ans) :-
    next(Node, Next),
    not(member(Next, Rest)),
    assert(path(N, [Next, Node | Rest])),
    fail.

/* 長さ N の経路をひとつ延ばす */
extend_path(N, Goal, Ans) :-
    path(N, Path), N1 is N + 1, extend_one_path(N1, Goal, Path, Ans).

/* 幅優先探索 */
breadth_search(N, Goal, Ans) :- extend_path(N, Goal, Ans).

breadth_search(N, Goal, Ans) :-
    N1 is N + 1, path(N1, Path), !, breadth_search(N1, Goal, Ans).

/* 経路の探索 */
keiro(Start, End, Ans) :-
    abolish(path, 2),            /* path をすべて削除する */
    assert(path(1, [Start])),
    breadth_search(1, End, Ans).

%% -------- キューを使った幅優先探索 --------
enqueue(Item, [Qh, [Item | Qt]], [Qh, Qt]).
dequeue(Item, [[Item | Qh], Qt], [Qh, Qt]).
empty([X, Y]) :- X == Y.

breadth_search(Goal, Q) :-
    not(empty(Q)),
    dequeue([Node | Path], Q, Q1),
    findall(Next, next(Node, Next), NextList),
    add_path(Goal, [Node | Path], NextList, Q1, Q2),
    breadth_search(Goal, Q2).

/* 経路を延ばしてキューに追加する */
add_path(_, _, [], Q, Q).

add_path(Goal, Path, [Goal | Rest], Q, Qe) :-
    reverse([Goal | Path], NewPath), write(NewPath), nl, !,
    add_path(Goal, Path, Rest, Q, Qe).

add_path(Goal, Path, [Next | Rest], Q, Qe) :-
    (member(Next, Path) -> Qn = Q ; enqueue([Next | Path], Q, Qn)),
    add_path(Goal, Path, Rest, Qn, Qe).

/* 幅優先探索の実行 */
keiro(Start, Goal) :-
    enqueue([Start], [Q, Q], Qn), breadth_search(Goal, Qn).

























