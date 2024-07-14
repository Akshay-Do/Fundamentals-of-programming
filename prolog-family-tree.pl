male(lakhamshi).
male(amritlal).
male(jitesh).

female(valiben).
female(jayaben).
female(archana).

parent(lakhamshi,amritlal).
parent(lakhamshi,kantilal).
parent(lakhamshi,dhanjilal).
parent(valiben,amritlal).
parent(valiben,kantilal).
parent(valiben,dhanjilal).

parent(amritlal,jitesh).
parent(amritlal,dipak).
parent(jayaben,jitesh).
parent(jayaben,dipak).

parent(jitesh,akshay).
parent(jitesh,akshat).
parent(jitesh,riya).
parent(archana,akshay).
parent(archana,akshat).
parent(archana,riya).

siblings(X,Y):- parent(Z,X),parent(Z,Y), X \= Y.
father(X,Y) :- male(X), parent(X,Y).
mother(X,Y) :- female(X), parent(X,Y).
