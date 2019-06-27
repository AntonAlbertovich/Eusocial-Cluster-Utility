#include <incmode>.

#program base.
% Define
status(-done).
status(done).
location(home).
location(mac_a).
location(mac_b).
location(mac_c).
location(mac_d).
location(mac_e).


location(X) :- block(X).
holds(F,0) :- init(F).

#program step(t).
% Generate
1{ move(X,Y,t) : task(X), location(Y)}.
{ turn(X,Y,t) : task(X), status(Y), holds(on(X,Z),t), valid_on(X, Z)}2.

% Test

:- move(X,Y,t), holds(on(B,Y),t-1), B != X, Y != home.
:- move(X,Y,t), Y == home.

:- turn(X,Y,t), holds(at(X,done),t-1).
:- turn(X,Y,t), valid_on(X, M), depends_on(X, Z), not holds(on(Z,M),t-1).
:- turn(X,Y,t), holds(at(B,Y),t-1), B != X, Y != done.



% Define

moved(X,t) :- move(X,Y,t).
turned(X,t) :- turn(X, Y, t).

:- move(X, Z, Y1), turned(X, Y2), Y1 == Y2.
:- move(X, Z1, Y), move(X, Z2, Y), Z1 != Z2.

:- turned(X1, T1), turned(X2, T2), depends_on(X2, X1), T1 >= T2.

holds(on(X,Y),t) :- move(X,Y,t).
holds(on(X,Z),t) :- holds(on(X,Z),t-1), not moved(X,t).


holds(at(X,Y),t) :- turn(X,Y,t).
holds(at(X,Z),t) :- holds(at(X,Z),t-1), not turned(X,t).

:- turned(X1, T1), turned(X2, T2), sum_valid_on(X1, Y, Z1), sum_valid_on(X2, Y, Z2), X1 != X2, T1 == T2,  Z = Z1+Z2, machine_threads(Y, Z4), Z > Z4.

sum_valid_on(X, Y, Z1) :- thread_cost(X, Z1), machine_threads(Y, Z2), Z1 <= Z2.
sum_valid_on(X1, X2, Y, Z) :- sum_valid_on(X1, Y, Z1), sum_valid_on(X2, Y, Z2), X1 != X2,  Z = Z1+Z2, machine_threads(Y, Z4), Z <= Z4.
valid_on(X, Y) :- thread_cost(X, Z1), machine_threads(Y, Z2), Z1 <= Z2.

less_valid_on(X, Y) :- thread_cost(X, Z1), machine_threads(Y, Z2), Z1*2 <= Z2.

#program check(t).
% Test
:- query(t), goal(F), not holds(F,t).

% Display
#show move/3.
#show turned/2.
%#show valid_on/2.
%#show less_valid_on/2.
%#show sum_valid_on/4.
#program base.
%

task(task_a).
task(task_b).
task(task_c).
task(task_d).

thread_cost(task_a, 1).
thread_cost(task_b, 2).
thread_cost(task_c, 3).
thread_cost(task_d, 4).

depends_on(task_d, task_a).
depends_on(task_d, task_b).
depends_on(task_d, task_c).


machine_threads(mac_a, 1).
machine_threads(mac_b, 2).
machine_threads(mac_c, 3).
machine_threads(mac_d, 4).
%
%
init(on(task_a, home)).
init(on(task_b, home)).
init(on(task_c, home)).
init(on(task_d, home)).
init(at(task_a,-done)).
init(at(task_b,-done)).
init(at(task_c,-done)).
init(at(task_d,-done)).
%
%
goal(at(task_a,done)).
goal(at(task_b,done)).
goal(at(task_c,done)).
goal(at(task_d,done)).
