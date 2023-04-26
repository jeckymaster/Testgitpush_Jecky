# Round Robin CPU Scheduling Algorithm

This program takes a plaintext file in CSV format containing a list of processes with their arrival time and burst time as input. The Round Robin algorithm is used to schedule the CPU for executing these processes.

## Requirements
To run the program, the Python environment should be set up with version 3.7. Additionally, Flask should be installed by running the command 
-!pip install Flask before executing app.py.

## How to Use
Execute the program using the command python app.py, which will run the program on a development server with the help of Flask app and "index.html". 
Two parameters need to be provided:

- The path to the input file in CSV format.
- The time quantum to be used by the Round Robin algorithm.

The program reads the input file and stores the processes in a queue called the ready queue, which is a FIFO queue. The program initializes the clock to 0, which is the starting time of the simulation. The clock is used to timestamp all events for the processes, such as creation time and completion time.

### The Round Robin algorithm executes in a main loop with the following steps:

1. Check if there are any processes in the ready queue. If the queue is empty, wait until a new process arrives.
2. If there is at least one process in the ready queue, dequeue the first process from the queue and assign it to the CPU for a time slice equal to the time quantum.
3. Update the clock by the time quantum, which represents the amount of time that the CPU has spent executing the process.
4. If the process has completed its execution, record the completion time of the process and calculate the turnaround time and waiting time.
5. If the process has not completed its execution, put it back into the ready queue, and the process will be executed again later.
6 .If there are other processes waiting in the ready queue, dequeue the next process and assign it to the CPU for execution.
7. If there are no other processes waiting in the ready queue, wait until a new process arrives.


Once all processes have completed their execution, the program computes the performance evaluation criteria, such as CPU utilization, throughput, average waiting time, and average turnaround time. The program then prints out these values to the port page through Flask and result.html as the output of the Round Robin CPU scheduling algorithm.

#### Terms for input and processes:
- Clock                   : timestamps all events for processes, such as creation time, completion time, etc.
- Process Creator         : creates processes at arrival time
- CPU                     : runs processes for a time slice (time quantum)
- Queue                   : FIFO ready queue used by both the process creator and CPU
- Process Arrival Time    : arrival time of new processes into the ready queue
- Process Service Time    : amount of time required by the processes to complete execution
- Time Quantum            : time each process can spend in the CPU, before it is removed
- Context Switch          : number of times a process is switched
- Completion Time         : Time at which process completes its execution.

#### Terms for output:

- CPU Utilization         : uses of CPU for the whole process
- Throughput              : completion time / clock
- Average Waiting Time    : Time Difference between completion time and arrival time. Turn Around Time = Completion Time – Arrival Time
- Average Turnaround Time : Time Difference between turn around time and burst time. Waiting Time = Turn Around Time – Burst Time

