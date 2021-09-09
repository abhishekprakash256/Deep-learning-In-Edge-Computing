#make the time slots and task generator with the bits of the task as well
'''
Assumption 
time slots are of 0.1 seconds
task bit are of the in {2.0, 2.1, . . . , 5.0} Mbits
time slots have the task probablity either 0 or 1 will decide later

'''

import random
import sys

episode = 1



def task_and_time_slot(episode):

	bits_dict = {0:2.0,1:2.1,2:2.2,3:2.3,4:2.4,5:2.5,6:2.6,7:2.7,8:2.8,9:2.9,10:3.0,11:3.1,12:3.2,13:3.3,14:3.4,15:3.5,16:3.6,17:3.7,18:3.8,19:3.9,20:4.0,21:4.1,22:4.2,23:4.3,24:4.4,25:4.5,26:4.6,27:4.7,28:4.8,29:4.9,30:5.0} # the dict of the task
	task_and_time_slot_lst = []
	for i in range(episode):
		task_and_time_slot_lst_2 = []
		task_and_time_slot_lst_2.append(i) #time slots of the tasks 

		task_and_time_slot_lst_2.append(random.randint(0,1))  #a probablity of the task

		task_and_time_slot_lst_2.append(bits_dict[(random.randint(0,30))]) #the bits of the task, the task are in Mbits

		
		task_and_time_slot_lst.append(task_and_time_slot_lst_2)
	return task_and_time_slot_lst



task_and_time = task_and_time_slot(episode) 

#print(task_and_time)



#making the mobile devices as per classes

class mobile_device:

  global comp_que #if a task comes then apply the append or use pop(0) to exit
  global trans_que #if a task comes then apply the append or use pop(0) to exit
  global freq_of_cpu #l_comp the to denote the time slot when task km (t) has either been processed or dropped, compδm (t) (in time slots) denote the number of time slots that task km (t) will wait for processing if it is placed in the computation queue
  global end_time #t + τm − 1
  global deadline #
  global wait_time_comp_processed_or_dropped  #lm(compt) ∈ T
  global processing_delay_comp_time_slots  # comp δm (t) 
  global wait_time_trans_processed_or_dropped #lm trans (comp)
  global processing_delay_trans_time_slots # trans δm (t) 
  
  deadline = 1 #for the 10 time slots

  #task_bits = {2.0, 2.1, . . . , 5.0} Mbits
  #task_len = random.randint(1,100)
  
  comp_que = []  #que for the comp
  trans_que = []  #que for the transmission

  freq_of_cpu = 2.5 #2.5GHz this is in the clock cycles
  processing_density = 0.297 # gigacycles per Mbits
  
  def __init__(self, task_and_time):
    self.task_and_time = task_and_time
    #print(self.task_and_time)

 #make the que in the mobile device
  
 #if the task arrive then make a variable km(t)

 #make a logic for unique km_t generation and also setting the bits of the task as zero if we get 0 at that position

  def task_id_gen(self,task_and_time):
  	#self.task_and_time = task_and_time
  	for i in range(episode):
  		if task_and_time[i][1] == 0:
  			task_and_time[i].append(0) #make the km_t as the 0
  			task_and_time[i][2] = 0
  		else:
  			task_and_time[i].append(random.randint(1,1000)) #here we append the km_t the unique id of the slor
  	
  	return task_and_time


 #making the offload decision of the tasks in the ques  
  def task_offload(self,task_and_time):

  	processing_delay_comp_time_slots_lst = []  #making the lst to store the processing_delay_comp_time

  	wait_time_comp_processed_or_dropped_lst = []
  	for i in range(episode):

  		#need to change as per the deep q of the 
  		#the mobile device will know before the 

  		#dummy test
  		task_offload_var = random.randint(0,1) #the x_m(t) the action will be changed later based on the model


  		#calualte the load 
  		if task_and_time[i][0] == 0:

  			processing_delay_comp_time_slots = 0

  			wait_time_comp_processed_or_dropped = min(task_and_time[i][0] + processing_delay_comp_time_slots + (task_and_time[i][2])/(2.5*0.1)/0.297, task_and_time[i][0] + 10 -1)  #processed or drop calculatinon by equation -1
  			
  			wait_time_comp_processed_or_dropped_lst.append(wait_time_comp_processed_or_dropped)
  			#print(wait_time_comp_processed_or_dropped_lst)
  		else:
  			
  			processing_delay_comp_time_slots = [max(wait_time_comp_processed_or_dropped_lst) - task_and_time[i][0] + 1]  # equation 2

	  		#define the wait time here if in 
	  		if task_offload_var == 0:
	  			trans_que.append(task_and_time[i][2])  #if xm(t) == 0 append in the transmisson que
	  			wait_time_comp_processed_or_dropped = 0  #if not placed in computational que

	  		else:
	  			comp_que.append(task_and_time[i][2])   #if the xm(t) ==1 append in the computational que
	  			#wait_time_processing = 


  	return trans_que,comp_que , wait_time_comp_processed_or_dropped_lst

  

  #def task_processing_comp(self,comp_que,task_and_time):
  	#for i in range(episode):
  		#print(i)








#make an instance


m1 = mobile_device(task_and_time)

#(m1.task_id_gen(m1.task_and_time))
#print(m1.task_offload(m1.task_and_time))


print(m1.task_id_gen(m1.task_and_time))
print(m1.task_offload(m1.task_and_time))
