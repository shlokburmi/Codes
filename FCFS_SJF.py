def fcfs(at, bt):
    at_bt = {at[i]: bt[i] for i in range(len(at))}
    at = sorted(at_bt.keys())
    bt = [at_bt[a] for a in at]
    ct = [0] * len(at)
    tat = [0] * len(at)
    
    ct[0] = at[0] + bt[0]
    for i in range(1, len(at)):
        ct[i] = ct[i-1] + bt[i]
    
    for i in range(len(at)):
        tat[i] = ct[i] - at[i]
    return ct, tat
def sjf(at, bt):
    n = len(at)
    ct = [0] * n
    tat = [0] * n
    completed = [False] * n
    time = 0
    completed_count = 0
    
    while completed_count < n:
        available_processes = [(i, bt[i]) for i in range(n) if at[i] <= time and not completed[i]]
        
        if available_processes:
            shortest_job = available_processes[0][0]
            for i in range(1, len(available_processes)):
                if available_processes[i][1] < bt[shortest_job]:
                    shortest_job = available_processes[i][0]  
            time += bt[shortest_job]
            ct[shortest_job] = time 
            completed[shortest_job] = True
            completed_count += 1
        else:
            time += 1  
    
    for i in range(n):
        tat[i] = ct[i] - at[i]  
    
    return ct, tat
at=[6,2,3,1,1,5]
bt = [4, 5, 3, 1, 2, 6]
ct, tat = fcfs(at, bt)

print(" Completion Time FCFS:", ct)
print(" Turn Around Time FCFS:", tat)
ct, tat = sjf(at, bt)

print(" Completion Time SJF:", ct)
print(" Turn Around Time SJF:", tat)
