# coding: utf-8

# Run python in linux or mac os is
# Terminal>> cd to "location of py" >> python fcps.py

# ### Shahariar Rabby
# #### ID: 151-15-5424
# #### Sec: F
# #### Operating System

# **Implement the First Come First Serve (FCFS) non preemptive algorithm by taking user
# input of the arrival & burst time of different processes.**
import numpy as np

# **Taking user input in this step. Users need to enter all the value for **AT** and **BT**
# separate with spaces. Input must be a set of even numbers.**
print ("Enter All value with space")
inputs = np.array([int(x) for x in input().split()])


# **This step checking that user input **even number** of values. And showing the inputs.**
if len(inputs) % 2 == 1:
    print ("Please input correct value, May be you missed something \
    (You need to input even number of values, two for each process)")
else:
    print("Successfully inserted all values")


# In this step whole user 1D input is converted into a 2D array, Also showing the 2D output where each column represents a process.
#  Where first element is **Arrival time** AT **and the Second element is Burst time **BT ** **
process = inputs.reshape((int(len(inputs) / 2), 2))


# **This step is sorting the processes by their Arrival time** AT
fcps = np.sort(process, axis=0)


# **This step is calculating the completion time **CT**, We know that *Completion Time is the Time at which process completes its execution*.
# ** Also showning Completion Time for each process.
ct = []
for i in range(int(len(fcps))):
    if i == 0:
        ct.append(process[i][0] + process[i][1])
    else:
        ct.append(process[i][1] + ct[i - 1])
# printing Compltion time
j = 1
for i in ct:
    print ("Compltion time for P{} is: {}".format(j, i))
    j += 1


# **This step is calculating the Turn Around Time **TAT**,
# We know that *Turn Around Time is the Time Difference between completion time and arrival time.**
# Also showning Completion Time for each process.
# `Turn Around Time = Completion Time - Arrival Time`


tat = []
for i in range(int(len(fcps))):
    tat.append(ct[i] - process[i][0])
# printing Turn Around Time
j = 1
for i in tat:
    print ("Turn Around Time for P{} is: {}".format(j, i))
    j += 1


# **This step is calculating the average Turn Around Time for all the process and showing them.
# ** We know,
# `Average Turn Around Time = "sum of all Turn Around Time" DEVIDE by "Total number of process"`
avarage_TAT = round(np.mean(tat), 2)
print ("Average Turn Around Time for all process is: ", avarage_TAT)


# **This step is calculatin Waiting time for each process,
# Waiting Time(W.T) is the Time Difference between turn around time and burst time.**We know,
# `Waiting Time = Turn Around Time - Burst Time`
wt = []
for i in range(int(len(fcps))):
    wt.append(tat[i] - process[i][1])
# printing Waiting time
j = 1
for i in wt:
    print ("Waiting time for P{} is: {}".format(j, i))
    j += 1


# **This step is calculatin average Waiting time for each process.**We know,
# `Average Waiting Time = "sum of all Waiting Time" DEVIDE by "Total number of process"`
avarage_WT = round(np.mean(wt), 2)
print ("Average Waiting Time for all process is: ", avarage_WT)


# ### Final Answar:
print("Average Waiting Time for all process is: ", avarage_WT, "sec.")
print("Average Turn Around Time for all process is: ", avarage_TAT, "sec.")



# ## Thank You
# #### Shahariar Rabby
