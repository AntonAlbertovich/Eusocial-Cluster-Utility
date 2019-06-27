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

location(X) :- block(X).
holds(F,0) :- init(F).

#program step(t).
% Generate
{ move(X,Y,t) : task(X), location(Y)}.
{ turn(X,Y,t) : task(X), status(Y), holds(on(X,Z),t), run_on(X, Z)}.

% Test

:- move(X,Y,t), holds(on(B,Y),t-1), B != X, Y != home.
:- move(X,Y,t), Y == home.

:- turn(X,Y,t), holds(at(X,done),t-1).
:- turn(X,Y,t), run_on(X, M), depends_on(X, Z), not holds(on(Z,M),t-1).
:- turn(X,Y,t), holds(at(B,Y),t-1), B != X, Y != done.



% Define

moved(X,t) :- move(X,Y,t).
turned(X,t) :- turn(X, Y, t).
ready(X,t) :- prep(X, t).

:- move(X, Z, Y1), turned(X, Y2), Y1 == Y2.
:- move(X, Z1, Y), move(X, Z2, Y), Z1 != Z2.
:- turned(X1, T1), turned(X2, T2), depends_on(X2, X1), T1 >= T2.
holds(on(X,Y),t) :- move(X,Y,t).
holds(on(X,Z),t) :- holds(on(X,Z),t-1), not moved(X,t).


holds(at(X,Y),t) :- turn(X,Y,t).
holds(at(X,Z),t) :- holds(at(X,Z),t-1), not turned(X,t).



#program check(t).
% Test
:- query(t), goal(F), not holds(F,t).

% Display
#show move/3.
#show turned/2.
#program base.
%

task(task_a).
task(task_b).
task(task_c).
task(task_d).

run_on(task_a, mac_a).
run_on(task_b, mac_b).
run_on(task_c, mac_c).
run_on(task_d, mac_d).

depends_on(task_d, task_a).
depends_on(task_d, task_b).
depends_on(task_d, task_c).

thread_cost(task_0, 1).
thread_cost(task_1, 4).
thread_cost(task_2, 4).
thread_cost(task_3, 6).
thread_cost(task_4, 7).
thread_cost(task_5, 8).
machine_threads(mac_a, 4).
machine_threads(mac_b, 6).
machine_threads(mac_c, 8).
machine_threads(mac_d, 8).
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
