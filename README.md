# 💻 CPU Scheduling and Banker's Algorithm Program README

This Python program, `main.py`, implements three Operating System algorithms: **FCFS**, **Preemptive SJF (SRTF)**, and the **Banker's Safety Algorithm**.

## 🚀 How to Run

1.  **Prerequisite:** Ensure **Python 3.x** is installed.
2.  **Save:** Save the provided code as `main.py`.
3.  **Execute:** Run the file from your terminal:
    ```bash
    python main.py
    ```

## ⚙️ Program Usage

The program starts with a menu. Enter the number corresponding to the algorithm you want to run (1, 2, or 3).

### 1 & 2: CPU Scheduling (FCFS / Preemptive SJF)

* **Input:** You will be prompted for the **number of processes** (N). For each process (P0, P1, P2...), you must enter its **Arrival time** and **Burst time**.
* **Output:** The program calculates and displays the **Gantt Chart** (process execution order and timings), the **Average Waiting Time**, and the **Average Turnaround Time**. 

### 3: Banker's Algorithm

* **Input:** You will be prompted for the **number of processes** (N) and the **number of resources** (M).
    * **Allocation Matrix:** N rows, M columns (resources currently held by each process).
    * **Maximum Matrix:** N rows, M columns (maximum resources each process can request).
    * **Available Vector:** 1 row, M columns (free resources in the system).
    * ***Note: Input values for matrices/vectors must be space-separated in a single line.***
* **Output:** The program calculates the **Need Matrix** and determines if the system is in a **SAFE** or **UNSAFE** state. If safe, it lists the **Safe Sequence**.