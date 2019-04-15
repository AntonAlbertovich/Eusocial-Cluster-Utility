#############################################
#           Using Python 3.7                #
#############################################
import socket
from distributed_ledger_functions import view_distributed_public_ledger

def monitor_cluster_node_high_cpu_temp(node_name, test_interval, max_temp, password):
    import psutil
    import time
    import datetime
    import socket
    import os
    from distributed_ledger_functions import next_block
    core_count = 0
    data_structure = psutil.sensors_temperatures()
    sub_structure = data_structure.get("coretemp")
    for a in sub_structure:
        if a[0][0] =="C":
            core_count = core_count + 1

    max_recorded_temps_per_core = [0]*core_count
    ave_recorded_temps_per_core = [0]*core_count
    max_recorded_temps_clocked = [0]*core_count
    max_recorded_temps_job_time = [0]*core_count
    recorded_temp_all_cores = [[]]*core_count
    recorded_memory_usage = [0]*core_count
    recorded_utc = ["" for x in range(core_count)]

    #The need for this for loop is due to a tendency for the machine's sensors to report temperatures of about 20 degrees higher than acutal internal temperature.
    #after about 10 readings, serveyed temperatures are consistently within expected ranges.
    for i in range(0, 10):
        time.sleep(.30)
        data_structure = psutil.sensors_temperatures()

    job_start_time= time.clock_gettime(time.CLOCK_REALTIME)
    try:
        job_start_time = time.clock_gettime_ns(time.CLOCK_REALTIME)
    except AttributeError:
        print("Alert: [time.clock_gettime_ns] has experienced an AttributeError.\nDefaulting to: [time.clock_gettime]\nTime precision will be effected.")
        job_start_time = time.clock_gettime(time.CLOCK_REALTIME)
    ts = time.time()
    time_stamp1 = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    recorded_cycles = 0
    testing_phase = time.time() + 60*int(test_interval)
    danger_zone = int(max_temp)
    kill_command = "sshpass -p '"+password+"' sudo poweroff -f "
    while(time.time() < testing_phase):
        time.sleep(.5)
        data_structure = psutil.sensors_temperatures()
        sub_structure = data_structure.get("coretemp")
        try:
            servey_time = time.clock_gettime_ns(time.CLOCK_REALTIME)
        except AttributeError:
            print("Alert: [time.clock_gettime_ns] has experienced an AttributeError.\nDefaulting to: [time.clock_gettime]\nTime precision will be effected.")
            servey_time = time.clock_gettime(time.CLOCK_REALTIME)
        servey_cores= psutil.cpu_percent(interval = 1, percpu = True)
        memory_usage = psutil.virtual_memory().percent
        this_core = 0
        ts = time.time()
        time_stamp = str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
        for a in sub_structure:
            if a[0][0] == "C":
                if (int(a[1]) > danger_zone):

                    os.system(kill_command)
                    
                ave_recorded_temps_per_core[this_core] = ave_recorded_temps_per_core[this_core] + int(a[1])

                if int(max_recorded_temps_per_core[this_core]) <= int(a[1]):

                    max_recorded_temps_per_core[this_core] = a[1]
                    max_recorded_temps_clocked[this_core] = servey_time
                    max_recorded_temps_job_time[this_core] = servey_time - job_start_time
                    recorded_temp_all_cores[this_core] = servey_cores
                    recorded_memory_usage[this_core] = memory_usage
                    recorded_utc[this_core] = time_stamp
                this_core = this_core + 1
        recorded_cycles = recorded_cycles + 1
    ts = time.time()
    time_stamp2 = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    for a in range(0, core_count):
        ave_recorded_temps_per_core[a] = ave_recorded_temps_per_core[a]/recorded_cycles
    data_out = ("On node: %s \n" %(node_name))
    text = ""
    for a in range(0, core_count):
        text = ("Max recorded temp on Core %d =  %d C. \n" %(a, max_recorded_temps_per_core[a]))
        text = text + ("Average recorded temp on Core %d =  %d C. \n" %(a, ave_recorded_temps_per_core[a]))
        text = text + ("UTC time: %s. \n" %(recorded_utc[a]))
        text = text + ("CPU time: %d ns. \n" %(max_recorded_temps_clocked[a]))
        text = text + ("Job time: %d ns. \n" %(max_recorded_temps_job_time[a]))
        text = text + ("CPU usages %s. \n" %(recorded_temp_all_cores[a]))
        text = text + ("RAM usage: %d percent. \n" %(recorded_memory_usage[a]))
        data_out = data_out+text
    data_out = data_out + ("Monitoring stated: %s UTC. " %(time_stamp1))
    data_out = data_out + ("Monitoring ended: %s UTC. \n" %(time_stamp2))

    # Here the thermal data is sent to the blockchain
    next_block(data_out)

    return data_out


    #print("Hours: ", job_start_time3//3600000000000, "Minutes: ", job_start_time3//600000000000, "Seconds: ",job_start_time3 //1000000000)
    #print(psutil.sensors_temperatures())


