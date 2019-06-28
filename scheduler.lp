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

holds(F,0) :- init(F).

#program step(t).
% Generate
1{ move(X,Y,t) : task(X), location(Y)}.
{ turn(X,Y,t) : task(X), status(Y), holds(on(X,Z),t), valid_on(X, Z), valid_os(X, Z)}.

% Test

:- move(X,Y,t), holds(on(B,Y),t-1), B != X, Y != home.
:- move(X,Y,t), Y == home.

:- turn(X,Y,t), holds(at(X,done),t-1).
:- turn(X,Y,t), holds(at(B,Y),t-1), B != X, Y != done.
:- turn(X,Y,t), holds(on(X,M),t), os_needed(X,Z1), os_on(M,Z2), Z1 != Z2.


% Define

moved(X,t) :- move(X,Y,t).
turned(X,t) :- turn(X, Y, t).
turned_at(X, M, t) :- turned(X, t), holds(on(X,M),t).

:- turned_at(X, M, t), cuda_not_on(M),  cuda_needed(X).

:- move(X, Z, Y1), turned(X, Y2), Y1 == Y2.
:- move(X, Z1, Y), move(X, Z2, Y), Z1 != Z2.
:- move(X, Z, Y1), move(X, Z, Y2), Y1 != Y2.

:- turned(X1, T1), turned(X2, T2), depends_on(X2, X1), T1 >= T2.

holds(on(X,Y),t) :- move(X,Y,t).
holds(on(X,Z),t) :- holds(on(X,Z),t-1), not moved(X,t).


holds(at(X,Y),t) :- turn(X,Y,t).
holds(at(X,Z),t) :- holds(at(X,Z),t-1), not turned(X,t).

:- turned(X1, T1), turned(X2, T2), sum_valid_on(X1, Y, Z1), sum_valid_on(X2, Y, Z2), X1 != X2, T1 == T2,  Z = Z1+Z2, machine_threads(Y, Z4), Z > Z4.

sum_valid_on(X, Y, Z1) :- thread_cost(X, Z1), machine_threads(Y, Z2), Z1 <= Z2.
sum_valid_on(X1, X2, Y, Z) :- sum_valid_on(X1, Y, Z1), sum_valid_on(X2, Y, Z2), X1 != X2,  Z = Z1+Z2, machine_threads(Y, Z4), Z <= Z4.
valid_on(X, Y) :- thread_cost(X, Z1), machine_threads(Y, Z2), Z1 <= Z2.
valid_os(X, Y) :- os_needed(X, Z1), os_on(Y, Z2), Z1 == Z2.





#program check(t).
% Test
:- query(t), goal(F), not holds(F,t).

% Display
%#show move/3.
%#show turned_at/3.
#show cuda_not_on/1.
%#show valid_os/2.
%#show valid_on/2.
%#show less_valid_on/2.
%#show sum_valid_on/4.

#program base.
%

task(task_a).
task(task_b).
task(task_c).
task(task_d).
task(task_e).
%task(task_f).

os(ubuntu_DE).
os(centOS_7_DE).
os(centOS_7_NE).
os(debian).
os(red_hat).

toolkit(cuda).

  
cuda_needed(task_a).
cuda_needed(task_b).
cuda_needed(task_a).
spacy_needed(task_b).
psutil_needed(task_b).
clingo_needed(task_b).

cuda_on(mac_a).
cuda_on(mac_b).
spacy_on(mac_b).
psutil_on(mac_b).
clingo_on(mca_b).

cuda_not_on(X) :- location(X), not cuda_on(X).
spacy_not_on(X) :- location(X), not spacy_on(X).
psutil_not_on(X) :- location(X), not psutil_on(X).
clingo_not_on(X) :- location(X), not clingo_on(X).



os_needed(task_a, ubuntu_DE).
os_needed(task_b, centOS_7_DE).
os_needed(task_c, centOS_7_NE).
os_needed(task_d, debian).
os_needed(task_e, red_hat).
%os_needed(task_f, NA).

os_on(mac_a, ubuntu_DE).
os_on(mac_b, centOS_7_DE).
os_on(mac_c, centOS_7_NE).
os_on(mac_d, debian).
os_on(mac_e, red_hat).
%os_on(task_f, NA).

thread_cost(task_a, 1).
thread_cost(task_b, 2).
thread_cost(task_c, 3).
thread_cost(task_d, 4).
thread_cost(task_e, 4).

%needs_toolkit(task_a , CUDA).
%needs_toolkit(task_b , CUDA).
%needs_toolkit(task_c , spaCy).
%needs_toolkit(task_d , psutil).
%needs_toolkit(task_e , clingo).

depends_on(task_a, task_e).
depends_on(task_d, task_a).
depends_on(task_d, task_b).
depends_on(task_d, task_c).


machine_threads(mac_a, 1).
machine_threads(mac_b, 2).
machine_threads(mac_c, 3).
machine_threads(mac_d, 4).
machine_threads(mac_e, 4).
%
%
init(on(task_a, home)).
init(on(task_b, home)).
init(on(task_c, home)).
init(on(task_d, home)).
init(on(task_e, home)).
init(at(task_a,-done)).
init(at(task_b,-done)).
init(at(task_c,-done)).
init(at(task_d,-done)).
init(at(task_e,-done)).
%
%
goal(at(task_a,done)).
goal(at(task_b,done)).
goal(at(task_c,done)).
goal(at(task_d,done)).
goal(at(task_e,done)).
