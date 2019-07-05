#include <incmode>. 
#program base. 
% A dynamically generated program.
% Made by build_asp.py using the data structures stored in Cluster_details.bin and Tasks_details.bin
% Define the fluents of the program.  
status(-done).
status(done).
location(home).
% location() describes the individual nodes/machines of a cluster.  
% home is the ECU master directory on one machine in a given cluster.  
% The machine which home is on is assumed to be directly connected to all other machines in the cluster.  
location(mac_a).
location(mac_b).
location(mac_c).
location(mac_d).
location(mac_e).
connection(home, mac_a).
connection(mac_a, mac_c).
connection(mac_a, mac_d).
connection(mac_a, mac_e).
connection(home, mac_b).
connection(home, mac_c).
connection(home, mac_d).
connection(home, mac_e).
holds(F,0) :- init(F).
#program step(t).
{ move(X,Y,t) : task(X), location(Y)} :- holds(on(X,M),t-1), connection(M, Y).
0{ turn(X,Y,t)}1 :- status(Y), task(X), holds(on(X,Z),t), valid_on(X, Z).
:- move(X,Y,t), holds(on(X,Y1),t-1), Y == home.
% Programs can not be moved back into the home directory.
:- turn(X,Y,t), holds(at(X,done),t-1).
% Programs can not be executed if they are already complete.
:- turn(X,Y,t), holds(on(X,M),t), depends_on(X, X1), not holds(on(X1,M),t-1).
moved(X,t) :- move(X,Y,t).
% moved() indicated what task X was moved at turn t.
turned(X,t) :- turn(X, Y, t).
% turn() indicated what task X was executed at what turn t.
turned_at(X, M, t) :- turned(X, t), holds(on(X,M),t).
% turned_at() indicated what task X was executed at Machine M at what turn t.
turned_with_2(M, X, X1, Z, t) :- turned(X,t), holds(on(X,M),t), thread_cost(X, C), turned(X1,t), holds(on(X1,M),t), thread_cost(X1, C1), X != X1, Z = C + C1.
turned_with_3(M, X, X1, X2, Z, t) :- turned(X,t), holds(on(X,M),t), thread_cost(X, C), turned_with_2(M, X1, X2, C1, t), X != X1, X != X2, Z = C + C1.
turned_with_4(M, X, X1, X2, X3, Z, t) :- turned(X,t), holds(on(X,M),t), thread_cost(X, C), turned_with_3(M, X1, X2, X3, C1, t), X != X1, X != X2, X != X3, Z = C + C1.
:- turned_with_2(M, X, X1, Z, t), machine_threads(M, C), Z > C.
:- turned_with_3(M, X, X1, X2, Z, t), machine_threads(M, C), Z > C.
:- turned_with_4(M, X, X1, X2, X3, Z, t), machine_threads(M, C), Z > C.
:- turned(X,t), holds(on(X,M),t), thread_cost(X, C), turned_with_4(M, X1, X2, X3, X4, C1, t), X != X1, X != X2, X != X3, X != X4.
% These rules allow for up to 4 task to be ran in parrallel on any one machine at a time,  
% if and only if the sum of the thread cost of said tasks does not add up to a number greater than  
% the core count of said machine. 
:- turned_at(X, M, t), cuda_not_on(M),  cuda_needed(X).
:- turned_at(X, M, t), spacy_not_on(M),  spacy_needed(X).
:- turned_at(X, M, t), psutil_not_on(M),  psutil_needed(X).
:- turned_at(X, M, t), clingo_not_on(M),  clingo_needed(X).
% This section will prevent a program which requires a given toolkit from being scheduled to run on a machine
%  which does not have said toolkit.
:- move(X, Z, Y1), turned(X, Y2), Y1 == Y2.
%  A program can not be moved and executed at the same time.
:- turned(X1, T1), turned(X2, T2), depends_on(X2, X1), T1 >= T2, moved(X2,T).
%  A program can executed before all of it's dependencies.
holds(on(X,Y),t) :- move(X,Y,t).
holds(on(X,Z),t) :- holds(on(X,Z),t-1), not moved(X,t).
holds(at(X,Y),t) :- turn(X,Y,t).
holds(at(X,Z),t) :- holds(at(X,Z),t-1), not turned(X,t).
valid_on(X, Y) :- thread_cost(X, Z1), machine_threads(Y, Z2), Z1 <= Z2.
:- os_needed(X, S), turned_at(X, M, t), not os_on(M, S), not -os_needed(X).
:- holds(on(X,M1),t), holds(on(X,M2),t), M1 != M2, holds(at(X,-done),t).
%  A program can not be duplicated if it has not been executed.
:- holds(on(X,M1),t), holds(on(X,M2),t), M1 != M2, task(X1), task(X2), not depends_on(X1, X), not depends_on(X2, X), X1 != X2, turned_at(X1, M1, T1), turned_at(X2, M2, T2).
%  A program can not be dupllicated if it is not the dependecy of at least two different later programs which are executed on atleast two diffent machines.
%  An unfinished program can not be at to two different locations at the same time.
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
psutil_on(mac_c).
clingo_on(mac_c).
clingo_on(mac_e).
% If a toolkit is not on on a machine then this rule is ture for that machine.
cuda_not_on(X) :- location(X), not cuda_on(X).
spacy_not_on(X) :- location(X), not spacy_on(X).
psutil_not_on(X) :- location(X), not psutil_on(X).
clingo_not_on(X) :- location(X), not clingo_on(X).
% If a task can only be executed on a specific OS then the rule os_needed() represents this in the model.
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
% Here the OS of each machine in the cluster is represented in the model.
os_on(mac_a, ubuntu_DE).
os_on(mac_b, centOS_7_DE).
os_on(mac_c, centOS_7_NE).
os_on(mac_d, debian).
os_on(mac_e).
% The thread_cost() rule represents how many threads a given task requires.
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
% The depends_on(X1, X2) rule represents that X2 must be exectued and on the machine executing X1.
depends_on(nrpcpa_cpp, project_asm).
depends_on(nrpcpa_cpp, fibinachi_nasm64bit_asm).
depends_on(spacy_test_py, wikipedia_pull_py).
% The machine_threads() rule represents how many cores on any given machine.
machine_threads(mac_a, 8).
machine_threads(mac_b, 4).
machine_threads(mac_c, 4).
machine_threads(mac_d, 4).
machine_threads(mac_e, 8).
% Initialization of the statuses of all tasks.
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
% Declartion of the goals of the system.
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
