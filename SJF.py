
# coding: utf-8

# In[1]:

import numpy as np
print ("Enter All value with space")
inputss = [int(x) for x in input().split()] # Taking input, for python2 raw_input
inputs = np.array(inputss)


# In[2]:

inputs 


# In[3]:

process = inputs.reshape((int(len(inputs)/2), 2)) #converting 2d
process = process.tolist() #converting Normal list
# Adding Task number
# 
# 0 means adding to ) no index
#
for p in range(len(process)):
    process[p].insert(0, p+1)

process


# In[4]:

sjf = sorted(process,key=lambda x: (x[2],x[1])) 
#
# Sorting list by index 2 and then 1
# Index 0 = process no
# index 1 = AT
# index 2 = BT
#

sjf 


# In[5]:

ct = []
for i in range(int(len(sjf))):
    if i == 0: 
    # for first task ct is null so ct = at + bt of that process
        ct.append(sjf[i][1] + sjf[i][2])
    else:
        ct.append(sjf[i][2] + ct[i-1])

# printing Compltion time
for i in range(len(ct)):
    print ("Compltion time for P{} is: {}".format(sjf[i][0],ct[i]))


# In[6]:

tat = []
for i in range(int(len(sjf))):
    tat.append(ct[i] - sjf[i][1])
    
# printing Turn Around Time
for i in range(len(tat)):
    print ("Turn Around Time for P{} is: {}".format(sjf[i][0],tat[i]))

avarage_TAT = round(np.mean(tat),2)
print ("Average Turn Around Time for all process is: ",avarage_TAT)


# In[7]:

wt = []
for i in range(int(len(sjf))):
    wt.append(tat[i] - sjf[i][2])
    
# printing Waiting time
for i in range(len(wt)):
    print ("Waiting time for P{} is: {}".format(sjf[i][0],wt[i]))


# In[8]:

avarage_WT = round(np.mean(wt),2)
print ("Average Waiting Time for all process is: ",avarage_WT)

