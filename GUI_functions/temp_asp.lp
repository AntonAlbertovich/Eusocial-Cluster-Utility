#include <incmode>. 
#program base. 
% Define
status(-done).
status(done).
location(home).
location(mac_a).
location(mac_b).
location(mac_c).
connection(home, mac_a).
connection(mac_a, mac_b).
connection(mac_a, mac_c).
connection(home, mac_b).
connection(mac_b, mac_a).
connection(mac_b, mac_c).
connection(home, mac_c).
connection(mac_c, mac_a).
connection(mac_c, mac_b).
holds(F,0) :- init(F).
#program step(t).
{ move(X,Y,t) : task(X), location(Y)} :- holds(on(X,M),t-1), connection(M, Y).
0{ turn(X,Y,t)}3 :- status(Y), task(X), holds(on(X,Z),t), valid_on(X, Z).
:- move(X,Y,t), holds(on(X,Y1),t-1), Y == home.
:- turn(X,Y,t), holds(at(X,done),t-1).
:- turn(X,Y,t), holds(on(X,M),t), depends_on(X, X1), not holds(on(X1,M),t-1).
moved(X,t) :- move(X,Y,t).
turned(X,t) :- turn(X, Y, t).
turned_at(X, M, t) :- turned(X, t), holds(on(X,M),t).
:- turned_at(X, M, t), cuda_not_on(M),  cuda_needed(X).
:- turned_at(X, M, t), spacy_not_on(M),  spacy_needed(X).
:- turned_at(X, M, t), psutil_not_on(M),  psutil_needed(X).
:- turned_at(X, M, t), clingo_not_on(M),  clingo_needed(X).
:- -turned_at(X1, X2,  M, t).
:- move(X, Z, Y1), turned(X, Y2), Y1 == Y2.
:- move(X, Z1, Y), move(X, Z2, Y), Z1 != Z2.
:- move(X, Z, Y1), move(X, Z, Y2), Y1 != Y2.
:- turned(X1, T1), turned(X2, T2), depends_on(X2, X1), T1 >= T2, moved(X2,T).
:- turned(X1, T1), turned(X2, T1), X1 != X2, moved(X2,T).
holds(on(X,Y),t) :- move(X,Y,t).
holds(on(X,Z),t) :- holds(on(X,Z),t-1), not moved(X,t).
holds(at(X,Y),t) :- turn(X,Y,t).
holds(at(X,Z),t) :- holds(at(X,Z),t-1), not turned(X,t).
:- turned(X1, T1), turned(X2, T2), sum_valid_on(X1, Y, Z1), sum_valid_on(X2, Y, Z2), X1 != X2, T1 == T2,  Z = Z1+Z2, machine_threads(Y, Z4), Z > Z4.
cost_valid_on(X, Y, Z1) :- thread_cost(X, Z1), machine_threads(Y, Z2), Z1 <= Z2.
sum_valid_on(X1, X2, Y, Z) :- cost_valid_on(X1, Y, Z1), cost_valid_on(X2, Y, Z2), X1 != X2,  Z = Z1+Z2, machine_threads(Y, Z4), Z <= Z4.
-sum_valid_on(X1, X2, Y):- task(X1), task(X2), machine_threads(Y, Z), not sum_valid_on(X1, X2, Y, Z).
-turned_at(X1, X2,  M, t) :- turned(X1, t), holds(on(X1,M),t), holds(on(X2,M),t), turned(X2, t), X1 != X2, -sum_valid_on(X1, X2, M, Z).
valid_on(X, Y) :- thread_cost(X, Z1), machine_threads(Y, Z2), Z1 <= Z2.
valid_os(X, M, S, t) :- os_needed(X, S), turned_at(X, M, t), os_on(M, S), not -os_needed(X).
:- os_needed(X, S), turned_at(X, M, t), not os_on(M, S), not -os_needed(X).
#program check(t).
:- query(t), goal(F), not holds(F,t).
%#show move/3.
%#show turned_at/3.
#program base.
task(asp_py).
task(days_in_month_c).
task(project_asm).
task(timer_f90).
os(ubuntu_DE).
os(centOS_7_DE).
os(centOS_7_NE).
os(debian).
os(red_hat).
os(no_os).


cuda_on(mac_a).
spacy_on(mac_a).
psutil_on(mac_a).
clingo_on(mac_a).
cuda_on(mac_b).
spacy_on(mac_b).
psutil_on(mac_b).
clingo_on(mac_b).
cuda_on(mac_c).
spacy_on(mac_c).
psutil_on(mac_c).
clingo_on(mac_c).
cuda_not_on(X) :- location(X), not cuda_on(X).
spacy_not_on(X) :- location(X), not spacy_on(X).
psutil_not_on(X) :- location(X), not psutil_on(X).
clingo_not_on(X) :- location(X), not clingo_on(X).

os_needed(asp_py, ubuntu_DE).
os_needed(days_in_month_c, ubuntu_DE).
-os_needed(project_asm).
-os_needed(timer_f90).



os_on(mac_a, ubuntu_DE).
os_on(mac_b, ubuntu_DE).
os_on(mac_c, ubuntu_DE).

thread_cost(asp_py, 1).
thread_cost(days_in_month_c, 1).
thread_cost(project_asm, 3).
thread_cost(timer_f90, 2).
machine_threads(mac_a, 4).
machine_threads(mac_b, 4).
machine_threads(mac_c, 4).
init(on(asp_py, home)).
init(at(asp_py, -done)).
init(on(days_in_month_c, home)).
init(at(days_in_month_c, -done)).
init(on(project_asm, home)).
init(at(project_asm, -done)).
init(on(timer_f90, home)).
init(at(timer_f90, -done)).
goal(at(asp_py, done)).
goal(at(days_in_month_c, done)).
goal(at(project_asm, done)).
goal(at(timer_f90, done)).
