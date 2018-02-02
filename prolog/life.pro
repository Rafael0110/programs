/*========================================================================*/
/*                 ■ AZ Prologによるライフゲーム                         */
/*========================================================================*/
/*　　(1) 実行開始は lifeGame. と入力してください。                       */
/*    (2) 終わるときは[ctrl] Z を押してください。　　                     */
/*    (3) [ctrl] Z 以外の入力で最初からやり直します。                     */
/*    (4) [ctrl] Z で終わったあと再開するとき restart. と入力して下さい。 */
/*------------------------------------------------------------------------*/
/*                                                                        */
/*【補足説明１】                                                          */
/*                                                                        */
/*　　周りの判定を単純化するため、配列は(NX + 2)×(NY + 2)の大きさをとり、*/
/*  セル(I,J)は、配列の(I + 1, J + 1)に格納します。すなわち配列の 0 行目、*/
/*  0 列目、NX + 1 列目, NY + 1 行目には必ず 0 の値が入ります             */
/*                                                                        */
/*........................................................................*/
/*                                                                        */
/*【補足説明２】                                                          */
/*                                                                        */
/*　　繰り返し速度を変えるときは、exeLifeGame の最後の s_sleepで指定して  */
/*  いる値（ミリ秒単位）を変更して下さい。                                */
/*                                                                        */
/*     exeLifeGame:-curState(A,_),…(中略)…, s_sleep(200).               */
/*                                                                        */
/*  で s_sleep(100) や s_sleep(300) 等と指定します。                      */
/*                                                                        */
/*------------------------------------------------------------------------*/
/* ■メイン述語 */
lifeGame    :- initLifeGame, lifeGameLoop.
lifeGameLoop:- repeat, exeLifeGame, endCheck.
restart     :- setData,lifeGameLoop.
endCheck:-d_keylength(0),!,fail.
endCheck:-d_keyin(X), endCheck(X).
endCheck( 26):-d_cursor(on).
endCheck( _ ):-restart.
/* ■実行制御関連述語 */
initLifeGame:-createCells(a,40,24),createCells(b,40,24),setData.
setData:-(retract(curState(X,Y));true),assert(curState(a,b)),
		clearCells(a,0), genCells(a,100),d_clear,d_cursor(off).
exeLifeGame:-curState(A,_),dspCells(A),	checkArCells,
					       changeCurrent,s_sleep(200).
changeCurrent:- retract(curState(X,Y)), assert(curState(Y,X)).

/* ■セル設定用述語 */
createCells(Name, NX,NY):-N is (NX + 2) * (NY + 2),
		create_array(N, AR),asserta(cells(Name,N, NX,NY,AR)).

setCells(Name,X,Y, V):-cells(Name,_, NX,_,AR),
			I is (NX+2) * Y + X, set_array(AR, I, V).
getCells(Name,X,Y, V):-cells(Name,_, NX,_,AR),
			I is (NX+2) * Y + X, get_array(AR, I, V).

clearCells(Name,V):-cells(Name,N, _,_,AR),setAR(AR,0,N,V).
setAR(AR,N,N,V).
setAR(AR,I,N,V):-set_array(AR, I, V), II is I+1, setAR(AR,II,N,V).

/* ■セル生成用述語（乱数を発生させてセルを生成します） */
genCells(Name,MX):-cells(Name,_, NX,NY,AR),genRandCells(Name, NX,NY,0,MX).

genRandCells(Name,NX,NY,MX,MX):-!.
genRandCells(Name,NX,NY,I,MX):-s_random(NX,X),s_random(NY,Y),!,
					chkRandCells(Name, NX,NY,X,Y,I,MX).

chkRandCells(Name,NX,NY,X,Y,I,MX):-XX is X+1, YY is Y+1,
	getCells(Name,XX,YY,0), !,
	setCells(Name,XX,YY,1), II is I+1, genRandCells(Name,NX,NY,II,MX).
chkRandCells(Name,NX,NY,X,Y,I,MX):-genRandCells(Name,NX,NY,I,MX).
/* ■セル表示述語 */
dspCells(Name):-cells(Name,_,NX,NY,_),dspCells(Name,0,0,NX,NY).
dspCells(Name, X,NY,NX,NY):-!.
dspCells(Name,NX, Y,NX,NY):-!, YY is Y + 1, dspCells(Name,0,YY,NX,NY).
dspCells(Name, X, Y,NX,NY):-XX is X+1, YY is Y+1,
	getCells(Name, XX,YY, 0),!,
	DX is X * 2+1, DY is Y +1, d_cursor(DX,DY),
	write('　'), XZ is X + 1, dspCells(Name,XZ,Y,NX,NY).
dspCells(Name, X, Y,NX,NY):-DX is X * 2+1, DY is Y +1, d_cursor(DX,DY),
	write('■'), XZ is X + 1, dspCells(Name,XZ,Y,NX,NY).
/* ■周りを取り出しカウント*/
getAround(Name, X, Y, [V1,V2,V3,V4,V5,V6,V7,V8]):-
	X0 is X + 1, XA is X+2, Y0 is Y+1,YA is Y+2,
	getCells(Name,X,Y ,V1),getCells(Name,X0,Y ,V2),getCells(Name,XA,Y ,V3),
	getCells(Name,X,Y0,V4),getCells(Name,XA,Y0,V5),
	getCells(Name,X,YA,V6),getCells(Name,X0,YA,V7),getCells(Name,XA,YA,V8).
numberAround(Name,X,Y,N):-getAround(Name, X, Y, L), countAround(L,0, N).
countAround([],N,N):-!.
countAround([1|X],NB,N):- NN is NB+1,countAround(X, NN,N).
countAround([0|X],NB,N):- countAround(X, NB,N).
/* ■生死判定 */
deadAlive(Curr, Next, X,Y):-numberAround(Curr,X,Y,N),
                        XX is X+1, YY=Y+1,
			getCells(Curr,XX,YY,V),judgeDA(V,Next,X,Y,N).
setAlive(Next,X,Y):-XX is X+1, YY is Y+1,  setCells(Next,XX,YY,1).
judgeDA(0, Next,X,Y,3):-!,setAlive(Next,X,Y).
judgeDA(1, Next,X,Y,2):-!,setAlive(Next,X,Y).
judgeDA(1, Next,X,Y,3):-!,setAlive(Next,X,Y).
judgeDA(_, _,_,_,_).
/* ■全体の生死判定 */
checkArCells:-curState(A,B), clearCells(B,0),
	cells(A,_,NX,NY,_), checkAr(A,B,0,0,NX,NY).
checkAr(A,B, X, NY,NX,NY):-!.
checkAr(A,B, NX, Y,NX,NY):-!, YY is Y + 1, checkAr(A,B,0,YY,NX,NY).
checkAr(A,B, X, Y,NX,NY):-
	deadAlive(A,B,X,Y), XX is X+1, checkAr(A,B,XX,Y,NX,NY).