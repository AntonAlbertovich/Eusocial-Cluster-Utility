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
connection(mac_a, mac_d).
connection(mac_a, mac_e).
connection(home, mac_b).
connection(mac_b, mac_a).
connection(mac_b, mac_c).
connection(mac_b, mac_d).
connection(mac_b, mac_e).
connection(home, mac_c).
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
turned_with_2(M, X, X1, Z, t) :- turned(X,t), holds(on(X,M),t), thread_cost(X, C), turned(X1,t), holds(on(X1,M),t), thread_cost(X1, C1), X != X1, Z = C + C1.
turned_with_3(M, X, X1, X2, Z, t) :- turned(X,t), holds(on(X,M),t), thread_cost(X, C), turned_with_2(M, X1, X2, C1, t), X != X1, X != X2, Z = C + C1.
turned_with_4(M, X, X1, X2, X3, Z, t) :- turned(X,t), holds(on(X,M),t), thread_cost(X, C), turned_with_3(M, X1, X2, X3, C1, t), X != X1, X != X2, X != X3, Z = C + C1.
:- turned_with_2(M, X, X1, Z, t), machine_threads(M, C), Z > C.
:- turned_with_3(M, X, X1, X2, Z, t), machine_threads(M, C), Z > C.
:- turned_with_4(M, X, X1, X2, X3, Z, t), machine_threads(M, C), Z > C.
:- turned(X,t), holds(on(X,M),t), thread_cost(X, C), turned_with_4(M, X1, X2, X3, X4, C1, t), X != X1, X != X2, X != X3, X != X4.
:- turned_at(X, M, t), cuda_not_on(M),  cuda_needed(X).
:- turned_at(X, M, t), spacy_not_on(M),  spacy_needed(X).
:- turned_at(X, M, t), psutil_not_on(M),  psutil_needed(X).
:- turned_at(X, M, t), clingo_not_on(M),  clingo_needed(X).
:- move(X, Z, Y1), turned(X, Y2), Y1 == Y2.
:- move(X, Z1, Y), move(X, Z2, Y), Z1 != Z2.
:- turned(X1, T1), turned(X2, T2), depends_on(X2, X1), T1 >= T2, moved(X2,T).
holds(on(X,Y),t) :- move(X,Y,t).
holds(on(X,Z),t) :- holds(on(X,Z),t-1), not moved(X,t).
holds(at(X,Y),t) :- turn(X,Y,t).
holds(at(X,Z),t) :- holds(at(X,Z),t-1), not turned(X,t).
valid_on(X, Y) :- thread_cost(X, Z1), machine_threads(Y, Z2), Z1 <= Z2.
:- os_needed(X, S), turned_at(X, M, t), not os_on(M, S), not -os_needed(X).
#program check(t).
:- query(t), goal(F), not holds(F,t).
#show move/3.
#show turned_at/3.
#program base.
task(nrpcpa_cpp).
task(wikipedia_gpu_py).
task(spacy_test_py).
task(psutil_example_py).
task(wikipedia_cpu_py).
task(fibinachi_nasm64bit_asm).
task(wikipedia_pull_py).
task(days_in_month_c).
task(timer_f90).
task(project_asm).
os(ubuntu_DE).
os(centOS_7_DE).
os(centOS_7_NE).
os(debian).
os(red_hat).
os(no_os).
cuda_needed(spacy_test_py).
spacy_needed(spacy_test_py).
cuda_on(mac_a).
spacy_on(mac_a).
psutil_on(mac_a).
clingo_on(mac_a).
cuda_on(mac_b).
spacy_on(mac_b).
psutil_on(mac_b).
clingo_on(mac_b).
cuda_not_on(X) :- location(X), not cuda_on(X).
spacy_not_on(X) :- location(X), not spacy_on(X).
psutil_not_on(X) :- location(X), not psutil_on(X).
clingo_not_on(X) :- location(X), not clingo_on(X).
-os_needed(nrpcpa_cpp).
os_needed(wikipedia_gpu_py, ubuntu_DE).
os_needed(spacy_test_py, ubuntu_DE).
-os_needed(psutil_example_py).
-os_needed(wikipedia_cpu_py).
-os_needed(fibinachi_nasm64bit_asm).
-os_needed(wikipedia_pull_py).
-os_needed(days_in_month_c).
-os_needed(timer_f90).
-os_needed(project_asm).
os_on(mac_a, ubuntu_DE).
os_on(mac_b, centOS_7_DE).
os_on(mac_c, centOS_7_NE).
os_on(mac_d, debian).
os_on(mac_e).
thread_cost(nrpcpa_cpp, 1).
thread_cost(wikipedia_gpu_py, 1).
thread_cost(spacy_test_py, 1).
thread_cost(psutil_example_py, 1).
thread_cost(wikipedia_cpu_py, 1).
thread_cost(fibinachi_nasm64bit_asm, 1).
thread_cost(wikipedia_pull_py, 1).
thread_cost(days_in_month_c, 1).
thread_cost(timer_f90, 1).
thread_cost(project_asm, 1).
depends_on(nrpcpa_cpp, project_asm).
depends_on(nrpcpa_cpp, fibinachi_nasm64bit_asm).
depends_on(spacy_test_py, wikipedia_pull_py).
machine_threads(mac_a, 8).
machine_threads(mac_b, 4).
machine_threads(mac_c, 4).
machine_threads(mac_d, 4).
machine_threads(mac_e, 8).
init(on(nrpcpa_cpp, home)).
init(at(nrpcpa_cpp, -done)).
init(on(wikipedia_gpu_py, home)).
init(at(wikipedia_gpu_py, -done)).
init(on(spacy_test_py, home)).
init(at(spacy_test_py, -done)).
init(on(psutil_example_py, home)).
init(at(psutil_example_py, -done)).
init(on(wikipedia_cpu_py, home)).
init(at(wikipedia_cpu_py, -done)).
init(on(fibinachi_nasm64bit_asm, home)).
init(at(fibinachi_nasm64bit_asm, -done)).
init(on(wikipedia_pull_py, home)).
init(at(wikipedia_pull_py, -done)).
init(on(days_in_month_c, home)).
init(at(days_in_month_c, -done)).
init(on(timer_f90, home)).
init(at(timer_f90, -done)).
init(on(project_asm, home)).
init(at(project_asm, -done)).
goal(at(nrpcpa_cpp, done)).
goal(at(wikipedia_gpu_py, done)).
goal(at(spacy_test_py, done)).
goal(at(psutil_example_py, done)).
goal(at(wikipedia_cpu_py, done)).
goal(at(fibinachi_nasm64bit_asm, done)).
goal(at(wikipedia_pull_py, done)).
goal(at(days_in_month_c, done)).
goal(at(timer_f90, done)).
goal(at(project_asm, done)).
