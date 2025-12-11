# CPU SCHEDULING + BANKER'S ALGORITHM PROGRAM

# NON-PREEMPTIVE FCFS
def fcfs(processes):
    processes.sort(key=lambda x: x['arrival'])
    time = 0
    gantt = []
    
    for p in processes:
        if time < p['arrival']:
            time = p['arrival']
        start = time
        finish = start + p['burst']
        time = finish
        
        p['start'] = start
        p['finish'] = finish
        p['turnaround'] = finish - p['arrival']
        p['waiting'] = p['turnaround'] - p['burst']
        
        gantt.append((p['id'], start, finish))

    avg_wait = sum(p['waiting'] for p in processes) / len(processes)
    avg_tat = sum(p['turnaround'] for p in processes) / len(processes)

    return gantt, avg_wait, avg_tat



# PREEMPTIVE SJF (Shortest Remaining Time First)
def preemptive_sjf(processes):
    import heapq
    
    time = 0
    completed = 0
    n = len(processes)
    gantt = []
    
    for p in processes:
        p['remaining'] = p['burst']

    ready_queue = []
    visited = set()
    last_pid = None

    while completed < n:
        for p in processes:
            if p['arrival'] <= time and p['id'] not in visited:
                heapq.heappush(ready_queue, (p['remaining'], p['arrival'], p))
                visited.add(p['id'])

        if ready_queue:
            rem, arr, curr = heapq.heappop(ready_queue)

            if last_pid != curr['id']:  
                gantt.append([curr['id'], time, time + 1])
            else:
                gantt[-1][2] += 1  

            curr['remaining'] -= 1
            time += 1
            last_pid = curr['id']

            if curr['remaining'] == 0:
                curr['finish'] = time
                curr['turnaround'] = time - curr['arrival']
                curr['waiting'] = curr['turnaround'] - curr['burst']
                completed += 1
            else:
                heapq.heappush(ready_queue, (curr['remaining'], curr['arrival'], curr))
        else:
            time += 1

    avg_wait = sum(p['waiting'] for p in processes) / n
    avg_tat = sum(p['turnaround'] for p in processes) / n

    return gantt, avg_wait, avg_tat



# BANKER'S ALGORITHM
def bankers_safety(allocation, maximum, available):
    n = len(allocation)
    m = len(available)

    need = [[maximum[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]

    finish = [False] * n
    safe_sequence = []
    work = available.copy()

    while len(safe_sequence) < n:
        found = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                work = [work[j] + allocation[i][j] for j in range(m)]
                finish[i] = True
                safe_sequence.append(i)
                found = True

        if not found:
            return False, []

    return True, safe_sequence



# USER MENU
def main():
    print("=== CPU Scheduling & Banker's Algorithm ===")
    print("1. FCFS (Non-preemptive)")
    print("2. Preemptive SJF")
    print("3. Banker's Algorithm")
    choice = int(input("Choose option: "))

    if choice in [1, 2]:
        n = int(input("Enter number of processes: "))
        processes = []

        for i in range(n):
            arrival = int(input(f"Arrival time of P{i}: "))
            burst = int(input(f"Burst time of P{i}: "))
            processes.append({'id': f"P{i}", 'arrival': arrival, 'burst': burst})

        if choice == 1:
            gantt, avg_wait, avg_tat = fcfs(processes)
            print("\n--- FCFS RESULT ---")
        else:
            gantt, avg_wait, avg_tat = preemptive_sjf(processes)
            print("\n--- PREEMPTIVE SJF RESULT ---")

        print("\nGantt Chart:")
        for pid, start, end in gantt:
            print(f"{pid}: {start} -> {end}")

        print(f"\nAverage Waiting Time: {avg_wait:.2f}")
        print(f"Average Turnaround Time: {avg_tat:.2f}")

    elif choice == 3:
        print("\n--- BANKER'S ALGORITHM ---")
        n = int(input("Enter number of processes: "))
        m = int(input("Enter number of resources: "))

        print("\nEnter Allocation Matrix:")
        allocation = [list(map(int, input().split())) for _ in range(n)]

        print("\nEnter Maximum Matrix:")
        maximum = [list(map(int, input().split())) for _ in range(n)]

        print("\nEnter Available Resources:")
        available = list(map(int, input().split()))

        safe, seq = bankers_safety(allocation, maximum, available)

        print("\nNeed Matrix:")
        need = [[maximum[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]
        for i in range(n):
            print(f"P{i}: {need[i]}")

        if safe:
            print("\nSystem is in a SAFE state.")
            print("Safe Sequence:", " -> ".join(f"P{i}" for i in seq))
        else:
            print("\nSystem is in an UNSAFE state.")

    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
