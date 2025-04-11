def round_robin(processes, n, quantum):
    bt = [process[2] for process in processes]
    wt = [0] * n
    tat = [0] * n
    rem_bt = bt.copy()
    arrival_time = [process[1] for process in processes]

    t = 0
    queue = []
    remaining_processes = n
    process_index = 0

    while remaining_processes > 0:
        while process_index < n and processes[process_index][1] <= t:
            queue.append(process_index)
            process_index += 1

        if queue:
            i = queue.pop(0)

            if rem_bt[i] > quantum:
                t += quantum
                rem_bt[i] -= quantum
                while process_index < n and processes[process_index][1] <= t:
                    queue.append(process_index)
                    process_index += 1
                queue.append(i)
            else:
                t += rem_bt[i]
                wt[i] = t - arrival_time[i] - bt[i]
                rem_bt[i] = 0
                remaining_processes -= 1

    for i in range(n):
        tat[i] = bt[i] + wt[i]

    return wt, tat


processes = [
    ("P0", 0, 5),
    ("P1", 1, 3),
    ("P2", 2, 1),
    ("P3", 3, 2),
    ("P4", 4, 3)
]

n = len(processes)
quantum = 2

waiting_time, turnaround_time = round_robin(processes, n, quantum)

avg_waiting_time = sum(waiting_time) / n
avg_turnaround_time = sum(turnaround_time) / n

print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"{processes[i][0]}\t{processes[i][1]}\t\t{processes[i][2]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
