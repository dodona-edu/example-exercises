:- module(dodonaevaluate, [tests/6]).

sol_echo(H, H).

testEcho(0).
testEcho(1).
testEcho(2).
testEcho(3).
testEcho(4).
testEcho(5).
testEcho(6).
testEcho(7).
testEcho(8).
testEcho(9).

tests("Test Last", dodonaevaluate:sol_echo, echo, false, 10000, L) :-
    setof([Out,In], (testEcho(In), member(Out, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])), L).
