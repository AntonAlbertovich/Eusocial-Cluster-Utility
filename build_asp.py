import pickle
if __name__ == "__main__":
    
    input_file= open("GUI_functions/Cluster_details.bin", "rb")
    all_macs= list(pickle.load(input_file))
    input_file.close()
    input_file= open("GUI_functions/Tasks_details.bin", "rb")
    all_jobs= list(pickle.load(input_file))
    input_file.close()

    asp_file = open("asp.lp")

    asp_file.write("  \n"

    asp_file.write("#include <incmode>. \n")

    asp_file.write("#program base. \n")
    asp_file.write("% Define\n")
    asp_file.write("status(-done).\n")
    ssp_file.write("tatus(done).\n")
    asp_file.write("location(home).\n")
    for i in range(len(all_macs)):
        mac = all_macs[i][0]
        mac.replace(" ", "")
        mac.lower()
        asp_file.write("location("+mac+").\n")
    
    for i in range(len(all_macs)):
        mac = all_macs[i][0]
        mac.replace(" ", "")
        mac.lower()
        for j in range(len(all_macs[i][2])):
            mac1 = all_macs[i][2][j]
            mac1.replace(" ", "")
            mac1.lower()
            asp_file.write("connection("+mac+", "+mac1+").\n")
    

    asp_file.write("holds(F,0) :- init(F).\n")

    asp_file.write("#program step(t).\n")
    asp_file.write("{ move(X,Y,t) : task(X), location(Y)} :- holds(on(X,M),t-1), connection(M, Y).\n")
    asp_file.write("0{ turn(X,Y,t)}1 :- status(Y), task(X), holds(on(X,Z),t), valid_on(X, Z), valid_os(X, Z).\n")

    asp_file.write(":- move(X,Y,t), holds(on(X,Y1),t-1), Y == home.\n")

    asp_file.write(":- turn(X,Y,t), holds(at(X,done),t-1).\n")
    asp_file.write(":- turn(X,Y,t), holds(on(X,M),t), os_needed(X,Z1), os_on(M,Z2), Z1 != Z2.\n")
    asp_file.write(":- turn(X,Y,t), holds(on(X,M),t), depends_on(X, X1), not holds(on(X1,M),t-1).\n")

    asp_file.write("moved(X,t) :- move(X,Y,t).\n")
    asp_file.write("turned(X,t) :- turn(X, Y, t).\n")

    asp_file.write("turned_at(X, M, t) :- turned(X, t), holds(on(X,M),t).\n")

    asp_file.write(":- turned_at(X, M, t), cuda_not_on(M),  cuda_needed(X).\n")
    asp_file.write(":- turned_at(X, M, t), spacy_not_on(M),  spacy_needed(X).\n")
    asp_file.write(":- turned_at(X, M, t), psutil_not_on(M),  psutil_needed(X).\n")
    asp_file.write(":- turned_at(X, M, t), clingo_not_on(M),  clingo_needed(X).\n")

    asp_file.write(":- move(X, Z, Y1), turned(X, Y2), Y1 == Y2.\n")
    asp_file.write(":- move(X, Z1, Y), move(X, Z2, Y), Z1 != Z2.\n")
    asp_file.write(":- move(X, Z, Y1), move(X, Z, Y2), Y1 != Y2.\n")

    asp_file.write(":- turned(X1, T1), turned(X2, T2), depends_on(X2, X1), T1 >= T2, moved(X2,T).\n")

    asp_file.write("holds(on(X,Y),t) :- move(X,Y,t).\n")
    asp_file.write("holds(on(X,Z),t) :- holds(on(X,Z),t-1), not moved(X,t).\n")


    asp_file.write("holds(at(X,Y),t) :- turn(X,Y,t).\n")
    asp_file.write("holds(at(X,Z),t) :- holds(at(X,Z),t-1), not turned(X,t).\n")


    asp_file.write(":- turned(X1, T1), turned(X2, T2), sum_valid_on(X1, Y, Z1), sum_valid_on(X2, Y, Z2), X1 != X2, T1 == T2,  Z = Z1+Z2, machine_threads(Y, Z4), Z > Z4.\n")

    asp_file.write("sum_valid_on(X, Y, Z1) :- thread_cost(X, Z1), machine_threads(Y, Z2), Z1 <= Z2.\n")
    asp_file.write("sum_valid_on(X1, X2, Y, Z) :- sum_valid_on(X1, Y, Z1), sum_valid_on(X2, Y, Z2), X1 != X2,  Z = Z1+Z2, machine_threads(Y, Z4), Z <= Z4.\n")

    asp_file.write("valid_on(X, Y) :- thread_cost(X, Z1), machine_threads(Y, Z2), Z1 <= Z2.\n")
    asp_file.write("valid_os(X, Y) :- os_needed(X, Z1), os_on(Y, Z2), Z1 == Z2.\n")

    asp_file.write("#program check(t).\n")
    asp_file.write(":- query(t), goal(F), not holds(F,t).\n")

    asp_file.write("#show move/3.\n")
    asp_file.write("#show turned_at/3.\n")

    asp_file.write("#program base.\n")

    for i in range(len(all_jobs)):
        job = all_jobs[i][0]
        job.replace(" ", "")
        job.lower()
        asp_file.write("task("+job+").\n")

    asp_file.write("os(ubuntu_DE).\n")
    asp_file.write("os(centOS_7_DE).\n")
    asp_file.write("os(centOS_7_NE).\n")
    asp_file.write("os(debian).\n")
    asp_file.write("os(red_hat).\n")

    for i in range(len(all_jobs)):
        job = all_jobs[i][0]
        job.replace(" ", "")
        job.lower()
        asp_file.write("task("+job+").\n")
        for j in range(len(all_macs[i][2])):
            if all_macs[i][2][j] == "CUDA":
                asp_file.write("cuda_needed("+job+").\n")
            elif all_macs[i][2][j] == "psutil":
                asp_file.write("psutil_needed("+job+").\n")
            elif all_macs[i][2][j] == "spaCy":
                asp_file.write("spacy_needed("+job+").\n")
            elif all_macs[i][2][j] == "clingo":
                asp_file.write("clingo_needed("+job+").\n")
    
    for i in range(len(all_macs)):
        mac = all_macs[i][0]
        mac.replace(" ", "")
        mac.lower()
        for j in range(len(all_macs[i][2])):
            mac1 = all_macs[i][2][j]
            mac1.replace(" ", "")
            mac1.lower()
            asp_file.write("connection("+mac+", "+mac1+").\n")

    cuda_on(mac_a).

    cuda_on(mac_b).
    spacy_on(mac_b).
    psutil_on(mac_b).
    clingo_on(mac_b).

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
