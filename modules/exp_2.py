#make a random number with the variable 
import random
import sys


#making a episode
episode = 10
#generate the task and the time slots 




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


def task_prob_gen(num):
	task_prob_lst = []
	for i in range(0,num):
		task_prob_lst.append(random.random())
	return task_prob_lst

#print(task_prob_gen(episode))
#print(task_gen(episode))
#print(time_slot_gen(episode))


#making the mobile device classes 

class mobile_device:

  global comp_que #if a task comes then apply the append or use pop(0) to exit
  global trans_que #if a task comes then apply the append or use pop(0) to exit
  global task_len , freq_of_cpu, l_comp , delta_comp_t #l_comp the to denote the time slot when task km (t) has either been processed or dropped, compδm (t) (in time slots) denote the number of time slots that task km (t) will wait for processing if it is placed in the computation queue
  global bits_of_task, processing_density , task_bits 


  #task_bits = {2.0, 2.1, . . . , 5.0} Mbits
  #task_len = random.randint(1,100)
  
  comp_que = []
  trans_que = []

  freq_of_cpu = 2.5 #2.5GHz change this is for the data per process per seconds 
  processing_density = 0.297 # gigacycles per Mbits [4]


  
  def __init__(self, time_slot,probablity,task):
    self.time_slot = time_slot
    self.probablity = probablity
    self.task = task

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