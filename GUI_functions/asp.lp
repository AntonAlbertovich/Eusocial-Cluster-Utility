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
connection(home, mac_a).
connection(mac_a, mac_b).
connection(mac_a, mac_c).
connection(home, mac_b).
connection(mac_b, mac_a).
connection(mac_b, mac_c).
connection(home, mac_c).
connection(mac_c, mac_a).
connection(mac_c, mac_b).
connection(home, mac_d).
connection(home, mac_e).
holds(F,0) :- init(F).
#program step(t).
{ move(X,Y,t) : task(X), location(Y)} :- holds(on(X,M),t-1), connection(M, Y).
0{ turn(X,Y,t)}1 :- status(Y), task(X), holds(on(X,Z),t), valid_on(X, Z).
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
holds(on(X,Y),t) :- move(X,Y,t).
holds(on(X,Z),t) :- holds(on(X,Z),t-1), not moved(X,t).
holds(at(X,Y),t) :- turn(X,Y,t).
holds(at(X,Z),t) :- holds(at(X,Z),t-1), not turned(X,t).
cost_valid_on(X, Y, Z1) :- thread_cost(X, Z1), machine_threads(Y, Z2), Z1 <= Z2.
sum_valid_on(X1, X2, Y, Z) :- cost_valid_on(X1, Y, Z1), cost_valid_on(X2, Y, Z2), X1 != X2,  Z = Z1+Z2, machine_threads(Y, Z4), Z <= Z4.
-sum_valid_on(X1, X2, Y):- task(X1), task(X2), machine_threads(Y, Z), not sum_valid_on(X1, X2, Y, Z).
-turned_at(X1, X2,  M, t) :- turned(X1, t), holds(on(X1,M),t), holds(on(X2,M),t), turned(X2, t), X1 != X2, -sum_valid_on(X1, X2, M, Z).
valid_on(X, Y) :- thread_cost(X, Z1), machine_threads(Y, Z2), Z1 <= Z2.
valid_os(X, M, S, t) :- os_needed(X, S), turned_at(X, M, t), os_on(M, S), not -os_needed(X).
:- os_needed(X, S), turned_at(X, M, t), not os_on(M, S), not -os_needed(X).
#program check(t).
:- query(t), goal(F), not holds(F,t).
#show move/3.
#show turned_at/3.
#program base.
task(prog_py_1_py).
task(prog_py_2_py).
task(prog_f90_1_f90).
task(prog_f90_2_f90).
task(prog_cpp_1_cpp).
task(prog_asm_1_asm).
task(prog_asm_2_asm).
task(prog_py_3_py).
task(prog_cpp_2_cpp).
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
-os_needed(prog_py_1_py).
-os_needed(prog_py_2_py).
-os_needed(prog_f90_1_f90).
-os_needed(prog_f90_2_f90).
-os_needed(prog_cpp_1_cpp).
-os_needed(prog_asm_1_asm).
-os_needed(prog_asm_2_asm).
-os_needed(prog_py_3_py).
-os_needed(prog_cpp_2_cpp).
os_on(mac_a, ubuntu_DE).
os_on(mac_b, centOS_7_DE).
os_on(mac_c, centOS_7_NE).
os_on(mac_d, ubuntu_DE).
os_on(mac_e, ubuntu_DE).
thread_cost(prog_py_1_py, 1).
thread_cost(prog_py_2_py, 1).
thread_cost(prog_f90_1_f90, 1).
thread_cost(prog_f90_2_f90, 1).
thread_cost(prog_cpp_1_cpp, 1).
thread_cost(prog_asm_1_asm, 1).
thread_cost(prog_asm_2_asm, 1).
thread_cost(prog_py_3_py, 1).
thread_cost(prog_cpp_2_cpp, 1).
machine_threads(mac_a, 8).
machine_threads(mac_b, 4).
machine_threads(mac_c, 4).
machine_threads(mac_d, 4).
machine_threads(mac_e, 4).
init(on(prog_py_1_py, home)).
init(at(prog_py_1_py, -done)).
init(on(prog_py_2_py, home)).
init(at(prog_py_2_py, -done)).
init(on(prog_f90_1_f90, home)).
init(at(prog_f90_1_f90, -done)).
init(on(prog_f90_2_f90, home)).
init(at(prog_f90_2_f90, -done)).
init(on(prog_cpp_1_cpp, home)).
init(at(prog_cpp_1_cpp, -done)).
init(on(prog_asm_1_asm, home)).
init(at(prog_asm_1_asm, -done)).
init(on(prog_asm_2_asm, home)).
init(at(prog_asm_2_asm, -done)).
init(on(prog_py_3_py, home)).
init(at(prog_py_3_py, -done)).
init(on(prog_cpp_2_cpp, home)).
init(at(prog_cpp_2_cpp, -done)).
goal(at(prog_py_1_py, done)).
goal(at(prog_py_2_py, done)).
goal(at(prog_f90_1_f90, done)).
goal(at(prog_f90_2_f90, done)).
goal(at(prog_cpp_1_cpp, done)).
goal(at(prog_asm_1_asm, done)).
goal(at(prog_asm_2_asm, done)).
goal(at(prog_py_3_py, done)).
goal(at(prog_cpp_2_cpp, done)).
