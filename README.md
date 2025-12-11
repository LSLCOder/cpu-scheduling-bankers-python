# 💻 CPU Scheduling and Banker's Algorithm Program

This Python program, `main.py`, implements three Operating System algorithms: **FCFS**, **Preemptive SJF (SRTF)**, and the **Banker's Safety Algorithm**.

## 🚀 How to Run

1. **Prerequisite:** Ensure **Python 3.x** is installed.
2. **Save:** Save the provided code as `main.py`.
3. **Execute:** Run the file from your terminal:
    ```bash
    python main.py
    ```

## ⚙️ Program Usage

The program starts with a menu. Enter the number corresponding to the algorithm you want to run (1, 2, or 3).

### 1 & 2: CPU Scheduling (FCFS / Preemptive SJF)

* **Input:** You will be prompted for the **number of processes (N)**. For each process (P0, P1, P2...), enter its:
  - **Arrival time**
  - **Burst time**
* **Output:** The program calculates and displays:
  - **Gantt Chart** (process execution order and timings)
  - **Average Waiting Time**
  - **Average Turnaround Time** 

### 3: Banker's Algorithm

* **Input:** You will be prompted for:
  - **Number of processes (N)**
  - **Number of resources (M)**
  - **Allocation Matrix:** N rows × M columns (resources currently held by each process)
  - **Maximum Matrix:** N rows × M columns (maximum resources each process can request)
  - **Available Vector:** 1 row × M columns (free resources in the system)

> **Note:** Input values for matrices/vectors must be space-separated in a single line.

* **Output:** The program calculates:
  - **Need Matrix**
  - Determines if the system is in a **SAFE** or **UNSAFE** state
  - If safe, lists the **Safe Sequence**

## 📂 Sample Input / Output

A sample output file (`sample_input_output.txt`) is included showing example runs for all algorithms, including:

* Entered processes (arrival time + burst time)
* Gantt Chart
* Average Waiting Time & Turnaround Time
* Banker's Algorithm matrices and safe sequence

## 🔗 Program Link

You can download or view the program here: https://github.com/LSLCOder/cpu-scheduling-bankers-python.git
