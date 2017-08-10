
# coding: utf-8

# ### Shahariar Rabby
# #### ID: 151-15-5424
# #### Sec: F
# #### Operating System

# **Implement the First Come First Serve (FCFS) non preemptive algorithm by taking user
# input of the arrival & burst time of different processes.**

# In[ ]:

import numpy as np


# **Taking user input in this step. Users need to enter all the value for **AT** and **BT** spear with spaces. Input must be a set of even numbers.**

# In[ ]:

print ("Enter All value with space")
inputs = np.array([int(x) for x in input().split()])


# **This step checking that user input **even number** of values. And showing the inputs.**

# In[ ]:

if len(inputs)%2 == 1:
    print ("Please input correct value, May be you missed something (You need to input even number of values, two for each process)")
else:
    print("Successfully inserted all values")
inputs


# **In this step whole user 1D input is converted into a 2D array, Also showing the 2D output where each column represents a process. Where first element is **Arrival time** AT **and the Second element is Burst time **BT ** **

# In[ ]:

process = inputs.reshape((int(len(inputs)/2), 2)).tolist()

for p in range(len(process)):
    process[p].insert(0, p+1)

process


# **This step is sorting the processes by their Arrival time** AT

# In[ ]:

fcfs = sorted(process,key=lambda x: (x[1],x[2],x[0]))
fcfs


# **This step is calculating the completion time **CT**, We know that *Completion Time is the Time at which process completes its execution*. ** Also showning Completion Time for each process.

# In[ ]:

ct = []
for i in range(int(len(fcfs))):
    if i == 0:
        ct.append(fcfs[i][1] + fcfs[i][2])
    else:
        ct.append(fcfs[i][2] + ct[i-1])

# printing Compltion time
# printing Compltion time
for i in range(len(ct)):
    print ("Compltion time for P{} is: {}".format(fcfs[i][0],ct[i]))


# **This step is calculating the Turn Around Time **TAT**, We know that *Turn Around Time is the Time Difference between completion time and arrival time.**  Also showning Completion Time for each process. 
# 
# `Turn Around Time = Completion Time - Arrival Time`

# In[ ]:

tat = []
for i in range(int(len(fcfs))):
    tat.append(ct[i] - fcfs[i][1])
    
# printing Turn Around Time
for i in range(len(tat)):
    print ("Turn Around Time for P{} is: {}".format(fcfs[i][0],tat[i]))


# **This step is calculating the average Turn Around Time for all the process and showing them. ** We know,
# 
# `Average Turn Around Time = "sum of all Turn Around Time" DEVIDE by "Total number of process"`

# In[ ]:

avarage_TAT = round(np.mean(tat),2)
print ("Average Turn Around Time for all process is: ",avarage_TAT)


# **This stp is calculatin Waiting time for each process, Waiting Time(W.T) is the Time Difference between turn around time and burst time.**We know,
# 
# `Waiting Time = Turn Around Time - Burst Time`

# In[ ]:

wt = []
for i in range(int(len(fcfs))):
    wt.append(tat[i] - fcfs[i][2])
    
# printing Waiting time
for i in range(len(wt)):
    print ("Waiting time for P{} is: {}".format(fcfs[i][0],wt[i]))


# **This step is calculatin average Waiting time for each process.**We know,
# 
# `Average Waiting Time = "sum of all Waiting Time" DEVIDE by "Total number of process"`

# In[ ]:

avarage_WT = round(np.mean(wt),2)
print ("Average Waiting Time for all process is:",avarage_WT)


# ### Final Answar:

# In[ ]:

print ("Average Waiting Time for all process is: ",avarage_WT,"sec.")
print ("Average Turn Around Time for all process is: ",avarage_TAT,"sec.")


# ## Thank You
# #### Shahariar Rabby
