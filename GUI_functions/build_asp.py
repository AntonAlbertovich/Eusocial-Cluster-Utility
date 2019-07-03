import pickle
if __name__ == "__main__":
    
    input_file= open("GUI_functions/Cluster_details.bin", "rb")
    all_macs= list(pickle.load(input_file))
    input_file.close()
    input_file= open("GUI_functions/Tasks_details.bin", "rb")
    all_jobs= list(pickle.load(input_file))
    input_file.close()

    asp_file = open("GUI_functions/asp.lp", 'w')

    asp_file.write("#include <incmode>. \n")

    asp_file.write("#program base. \n")
    asp_file.write("% Define\n")
    asp_file.write("status(-done).\n")
    asp_file.write("status(done).\n")
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
        asp_file.write("connection(home, "+mac+").\n")
        for j in range(len(all_macs[i][2])):
            mac1 = all_macs[i][2][j]
            mac1.replace(" ", "")
            mac1.lower()
            asp_file.write("connection("+mac+", "+mac1+").\n")
    

    asp_file.write("holds(F,0) :- init(F).\n")

    asp_file.write("#program step(t).\n")
    asp_file.write("{ move(X,Y,t) : task(X), location(Y)} :- holds(on(X,M),t-1), connection(M, Y).\n")
    asp_file.write("0{ turn(X,Y,t)}1 :- status(Y), task(X), holds(on(X,Z),t), valid_on(X, Z).\n")

    asp_file.write(":- move(X,Y,t), holds(on(X,Y1),t-1), Y == home.\n")

    asp_file.write(":- turn(X,Y,t), holds(at(X,done),t-1).\n")
    asp_file.write(":- turn(X,Y,t), holds(on(X,M),t), depends_on(X, X1), not holds(on(X1,M),t-1).\n")

    asp_file.write("moved(X,t) :- move(X,Y,t).\n")
    asp_file.write("turned(X,t) :- turn(X, Y, t).\n")

    asp_file.write("turned_at(X, M, t) :- turned(X, t), holds(on(X,M),t).\n")
    
    asp_file.write("turned_with_2(M, X, X1, Z, t) :- turned(X,t), holds(on(X,M),t), thread_cost(X, C), turned(X1,t), holds(on(X1,M),t), thread_cost(X1, C1), X != X1, Z = C + C1.\n")
    asp_file.write("turned_with_3(M, X, X1, X2, Z, t) :- turned(X,t), holds(on(X,M),t), thread_cost(X, C), turned_with_2(M, X1, X2, C1, t), X != X1, X != X2, Z = C + C1.\n")
    asp_file.write("turned_with_4(M, X, X1, X2, X3, Z, t) :- turned(X,t), holds(on(X,M),t), thread_cost(X, C), turned_with_3(M, X1, X2, X3, C1, t), X != X1, X != X2, X != X3, Z = C + C1.\n")

    asp_file.write(":- turned_with_2(M, X, X1, Z, t), machine_threads(M, C), Z > C.\n")
    asp_file.write(":- turned_with_3(M, X, X1, X2, Z, t), machine_threads(M, C), Z > C.\n")
    asp_file.write(":- turned_with_4(M, X, X1, X2, X3, Z, t), machine_threads(M, C), Z > C.\n")
    asp_file.write(":- turned(X,t), holds(on(X,M),t), thread_cost(X, C), turned_with_4(M, X1, X2, X3, X4, C1, t), X != X1, X != X2, X != X3, X != X4.\n")

    asp_file.write(":- turned_at(X, M, t), cuda_not_on(M),  cuda_needed(X).\n")
    asp_file.write(":- turned_at(X, M, t), spacy_not_on(M),  spacy_needed(X).\n")
    asp_file.write(":- turned_at(X, M, t), psutil_not_on(M),  psutil_needed(X).\n")
    asp_file.write(":- turned_at(X, M, t), clingo_not_on(M),  clingo_needed(X).\n")
    asp_file.write(":- move(X, Z, Y1), turned(X, Y2), Y1 == Y2.\n")
    asp_file.write(":- move(X, Z1, Y), move(X, Z2, Y), Z1 != Z2.\n")
    asp_file.write(":- turned(X1, T1), turned(X2, T2), depends_on(X2, X1), T1 >= T2, moved(X2,T).\n")
    asp_file.write("holds(on(X,Y),t) :- move(X,Y,t).\n")
    asp_file.write("holds(on(X,Z),t) :- holds(on(X,Z),t-1), not moved(X,t).\n")


    asp_file.write("holds(at(X,Y),t) :- turn(X,Y,t).\n")
    asp_file.write("holds(at(X,Z),t) :- holds(at(X,Z),t-1), not turned(X,t).\n")

    asp_file.write("valid_on(X, Y) :- thread_cost(X, Z1), machine_threads(Y, Z2), Z1 <= Z2.\n")
    asp_file.write(":- os_needed(X, S), turned_at(X, M, t), not os_on(M, S), not -os_needed(X).\n")


    asp_file.write("#program check(t).\n")
    asp_file.write(":- query(t), goal(F), not holds(F,t).\n")

    asp_file.write("#show move/3.\n")
    asp_file.write("#show turned_at/3.\n")

    asp_file.write("#program base.\n")

    for i in range(len(all_jobs)):
        job = all_jobs[i][0]
        job = job.replace(" ", "")
        job = job.replace(".", "_")
        job = job.lower()
        asp_file.write("task("+job+").\n")

    asp_file.write("os(ubuntu_DE).\n")
    asp_file.write("os(centOS_7_DE).\n")
    asp_file.write("os(centOS_7_NE).\n")
    asp_file.write("os(debian).\n")
    asp_file.write("os(red_hat).\n")
    asp_file.write("os(no_os).\n")

    for i in range(len(all_jobs)):
        job = all_jobs[i][0]
        job = job.replace(" ", "")
        job = job.replace(".", "_")
        job = job.lower()
        for j in range(len(all_jobs[i][3])):
            if all_jobs[i][3][j] == "CUDA":
                asp_file.write("cuda_needed("+job+").\n")
            elif all_jobs[i][3][j] == "psutil":
                asp_file.write("psutil_needed("+job+").\n")
            elif all_jobs[i][3][j] == "spaCy":
                asp_file.write("spacy_needed("+job+").\n")
            elif all_jobs[i][3][j] == "clingo":
                asp_file.write("clingo_needed("+job+").\n")
    
    for i in range(len(all_macs)):
        mac = all_macs[i][0]
        mac.replace(" ", "")
        mac.lower()
        for j in range(len(all_macs[i][3])):
            if all_macs[i][3][j] == "CUDA":
                asp_file.write("cuda_on("+mac+").\n")
            elif all_macs[i][3][j] == "psutil":
                asp_file.write("psutil_on("+mac+").\n")
            elif all_macs[i][3][j] == "spaCy":
                asp_file.write("spacy_on("+mac+").\n")
            elif all_macs[i][3][j] == "clingo":
                asp_file.write("clingo_on("+mac+").\n")



    asp_file.write("cuda_not_on(X) :- location(X), not cuda_on(X).\n")
    asp_file.write("spacy_not_on(X) :- location(X), not spacy_on(X).\n")
    asp_file.write("psutil_not_on(X) :- location(X), not psutil_on(X).\n")
    asp_file.write("clingo_not_on(X) :- location(X), not clingo_on(X).\n")


    for i in range(len(all_jobs)):
        job = all_jobs[i][0]
        job = job.replace(" ", "")
        job = job.replace(".", "_")
        job = job.lower()
        if all_jobs[i][1][1] == "Ubuntu 18.04 [Desktop Edition]":
            asp_file.write("os_needed("+job+", ubuntu_DE).\n")
        elif all_jobs[i][1][1] == "CentOS 7 [Desktop Edition]":
            asp_file.write("os_needed("+job+", centOS_7_DE).\n")
        elif all_jobs[i][1][1] == "CentOS 7 [Node/server Edition]":
            asp_file.write("os_needed("+job+", centOS_7_NE).\n")
        elif all_jobs[i][1][1] == "Unlisted Debian based OS":
            asp_file.write("os_needed("+job+", debian).\n")
        elif all_jobs[i][1][1] == "Unlisted Red Hat based OS":
            asp_file.write("os_needed("+job+", red_hat).\n")
        elif all_jobs[i][1][1] == "N/A":
            asp_file.write("-os_needed("+job+").\n")
    
    for i in range(len(all_macs)):
        mac = all_macs[i][0]
        mac.replace(" ", "")
        mac.lower()
        if all_macs[i][7] == "Ubuntu 18.04 [Desktop Edition]":
            asp_file.write("os_on("+mac+", ubuntu_DE).\n")
        elif all_macs[i][7] ==  "CentOS 7 [Desktop Edition]":
            asp_file.write("os_on("+mac+", centOS_7_DE).\n")
        elif all_macs[i][7] == "CentOS 7 [Node/server Edition]":
            asp_file.write("os_on("+mac+", centOS_7_NE).\n")
        elif all_macs[i][7] == "Unlisted Debian based OS":
            asp_file.write("os_on("+mac+", debian).\n")
        elif all_macs[i][7] == "Unlisted Red Hat based OS":
            asp_file.write("os_on("+mac+").\n")
    
    for i in range(len(all_jobs)):
        job = all_jobs[i][0]
        job = job.replace(" ", "")
        job = job.replace(".", "_")
        job = job.lower()
        thread = str(all_jobs[i][4])
        asp_file.write("thread_cost("+job+", "+thread+").\n")


    for i in range(len(all_jobs)):
        job0 = all_jobs[i][0]
        job0 = job0.replace(" ", "")
        job0 = job0.replace(".", "_")
        job0 = job0.lower()
        for j in range(len(all_jobs[i][2])):
            job1 = all_jobs[i][2][j]
            job1 = job1.replace(" ", "")
            job1 = job1.replace(".", "_")
            job1 = job1.lower()
            asp_file.write("depends_on("+job0+", "+job1+").\n")
    

    for i in range(len(all_macs)):
        mac = all_macs[i][0]
        mac.replace(" ", "")
        mac.lower()
        thread = str(all_macs[i][6])
        asp_file.write("machine_threads("+mac+", "+thread+").\n")

    for i in range(len(all_jobs)):
        job = all_jobs[i][0]
        job = job.replace(" ", "")
        job = job.replace(".", "_")
        job = job.lower()
        asp_file.write("init(on("+job+", home)).\n")
        asp_file.write("init(at("+job+", -done)).\n")

    for i in range(len(all_jobs)):
        job = all_jobs[i][0]
        job = job.replace(" ", "")
        job = job.replace(".", "_")
        job = job.lower()
        asp_file.write("goal(at("+job+", done)).\n")

    asp_file.close()
