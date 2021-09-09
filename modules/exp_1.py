#make the system model with all the variables that is defined 
'''
 N = {1, 2, . . . , N } and a
set of mobile devices M = {1, 2, . . . , M } in an MEC system.
T = {1, . . . , T }, where each time slot has a duration of ∆
seconds. I
'''
#making the set of mobile devices -


#make a random number with the variable 
import random
import sys

'''
coding the FIFO logic use append to add in back and pop(0)

'''
def probablity_gen():
	return random.uniform(0, 1)

#making a mobile device

#time should be in seconds 

# the task comes in bits 

# the input to the mobile device should be the array of the time slots and tasks

def time_slot_gen(num): #change the time slots are per needs 
  time_slot_lst = []
  for i in range(0,num):
    time_slot_lst.append(random.randint(1,100))
  return time_slot_lst

def task_gen(num):
  task_slot_lst = []
  for i in range(0,num):
    task_slot_lst.append((random.randint(0,100))*8)
  return task_slot_lst


#making a episode
episode = 10
#generate the task and the time slots 



class mobile_device:
  global comp_que #if a task comes then apply the append or use pop(0) to exit
  global trans_que #if a task comes then apply the append or use pop(0) to exit
  global task_len , freq_of_cpu, l_comp , delta_comp_t #l_comp the to denote the time slot when task km (t) has either been processed or dropped, compδm (t) (in time slots) denote the number of time slots that task km (t) will wait for processing if it is placed in the computation queue
  task_len = random.randint(1,100)
  comp_que = []
  trans_que = []
  freq_of_cpu = 2.5 #2.5GHz
  def __init__(self, time_slot,probablity,task):
    self.time_slot = time_slot
    self.probablity = probablity
    self.task = task

    if probablity <= 0.3:
    	task = task
    else:
    	task = 0

 #make the que in the mobile device
  
 #if the task arrive then make a variable km(t)

 #make a logic for unique km_t generation
  def task_id_gen(task):
    if task !=0:
    	km_t = random.randint(1,1000) #(km_t denotes a unique index of the task)
    	#If there exists a new task km (t) at the beginning of time slot t, then λm(t) is equal to the size of task km (t).
    	task_len = 0
    else:
    	km_t = 0
    	l_comp = 0
    	task_len = task_len
    return km_t , task_len

  #task offloading decision 
  #generate a xm_t , if xm_t =1 process locally and xm_t comp_que then offload to the trans_que 

  def task_offload(task):
  	xm_t = random.randint(0,1)
  	if xm_t ==1 :
  		comp_que.append(task_len)
  	else:
  		trans_que.append(task_len)
  	return comp_que, trans_que

    #km(t) has not been completely processed by the end of time slot t + τm − 1, then it will be dropped immediately.




#sample devices 

m1 = mobile_device(0,probablity_gen(),1)

m2 = mobile_device(0,0,probablity_gen())

m_set = {m1,m2} 

print(m1.task_offload())
