neighbor(L,R,[L,R|_]).
neighbor(L,R,[_|Xs]) :- neighbor(L,R,Xs).

neighborx(L,R,Xs) :- neighbor(L,R,Xs).
neighborx(L,R,Xs) :- neighbor(R,L,Xs).

drip(color, 	house(Color,_,_,_,_),		Color).
drip(country, house(_,Contry,_,_,_),	Contry).
drip(animal, 	house(_,_,Animal,_,_),	Animal).
drip(drink, 	house(_,_,_,Drink,_),		Drink).
drip(smoke, 	house(_,_,_,_,Smoke),		Smoke).

zebra(X,Y) :-
  Street = [H1,_,H3,_,_],
  member(house(red, english, _, _, _), Street),
  member(house(_, spanish, dog, _, _), Street),
  member(house(green, _, _, coffee, _), Street),
  member(house(_, ukurina, _, tea, _), Street),
  member(house(_, _,snail, _, oldgold), Street),
  member(house(yellow, _, _, _, kools), Street),
  member(house(_, _, _, orange, luckystrike), Street),
  member(house(_, japanese, _, _, parliaments), Street),

  neighbor(house(white,_,_,_,_), house(green,_,_,_,_),    Street),

  neighborx(house(_,_,_,_,chesterfields), house(_,_,fox,_,_), Street),
  neighborx(house(_,_,_,_,kools), house(_,_,horse,_,_), Street),
  neighborx(house(_,norwegian,_,_,_), house(blue,_,_,_,_), Street),

  drip(drink, H3,Milk), Milk = milk,
  drip(country, H1,Norw), Norw = norwegian,

  member(house(_,X,_,water,_),Street),
  member(house(_,Y,zebra,_,_),Street).

main :- zebra(X,Y),
  format('the person who drink water is ~a~n',[X]),
  format('the person who raize a zebra is ~a~n',[Y]).