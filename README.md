# Operating System Scheduling algorithms 
# First-Come, First-Served (FCFS) and Shortest Job First (SJF) Scheduling
# This code is for non-preemptive

**These algorithms are either non-preemptive or preemptive. Non-preemptive algorithms are designed so that once a process enters the running state, it cannot be preempted until it completes its allotted time, whereas the preemptive scheduling is based on priority where a scheduler may preempt a low priority running process anytime when a high priority process enters into a ready state.**


## First Come First Serve (FCFS)


Jobs are executed on first come, first serve basis.


It is a non-preemptive, pre-emptive scheduling algorithm.


Easy to understand and implement.


Its implementation is based on FIFO queue.


Poor in performance as average wait time is high.


## Shortest Job First (SJF)

**Shortest job first (SJF) or shortest job next, is a scheduling policy that selects the waiting process with the smallest execution time to execute next. SJN is a non-preemptive algorithm.**

Shortest Job first has the advantage of having minimum average waiting time among all scheduling algorithms. 

It is a Greedy Algorithm. 

It may cause starvation if shorter processes keep coming. This problem can be solved using the concept of aging.

It is practically infeasible as Operating System may not know burst time and therefore may not sort them. While it is not possible to 
predict execution time, several methods can be used to estimate the execution time for a job, such as a weighted average of previous execution times. SJF can be used in specialized environments where accurate estimates of running time are available.


### Limitation For SJF
 ***Only work when AT = 0 For all process***
