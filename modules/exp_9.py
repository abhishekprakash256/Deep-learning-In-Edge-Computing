# make the time slots and task generator with the bits of the task as well
'''
Assumption
time slots are of 0.1 seconds
task bit are of the in {2.0, 2.1, . . . , 5.0} Mbits
time slots have the task probablity either 0 or 1 will decide later

'''

import random
import sys
import torch 
import numpy as np
#import matplotlib as plt

# we use this as the time slot like episode = 5, then 5 time slots
episode = 10


def task_and_time_slot(episode):

    bits_dict = {0: 2.0, 1: 2.1, 2: 2.2, 3: 2.3, 4: 2.4, 5: 2.5, 6: 2.6, 7: 2.7, 8: 2.8, 9: 2.9, 10: 3.0, 11: 3.1, 12: 3.2, 13: 3.3, 14: 3.4, 15: 3.5, 16: 3.6,
        17: 3.7, 18: 3.8, 19: 3.9, 20: 4.0, 21: 4.1, 22: 4.2, 23: 4.3, 24: 4.4, 25: 4.5, 26: 4.6, 27: 4.7, 28: 4.8, 29: 4.9, 30: 5.0}  # the dict of the task
    task_and_time_slot_lst = []
    for i in range(episode):
        task_and_time_slot_lst_2 = []
        task_and_time_slot_lst_2.append(i)  # time slots of the tasks

        task_and_time_slot_lst_2.append(random.randint(0, 1))  # a probablity of the task

        # the bits of the task, the task are in Mbits
        task_and_time_slot_lst_2.append(bits_dict[(random.randint(0, 30))])

        task_and_time_slot_lst.append(task_and_time_slot_lst_2)
    return task_and_time_slot_lst


task_and_time = task_and_time_slot(episode)

print("This is the generated task and time slot")
print(task_and_time)
print("End of the task and time")


#making the load matrix with all the values

def load_matrix(episode):
    load_mat = np.ones((episode , episode))
    return load_mat
#print(load_matrix(episode))
# making the mobile devices as per classes

class mobile_device:

  # if a task comes then apply the append or use pop(0) to exit
    global comp_que
  # if a task comes then apply the append or use pop(0) to exit
    global trans_que
  # l_comp the to denote the time slot when task km (t) has either been processed or dropped, compδm (t) (in time slots) denote the number of time slots that task km (t) will wait for processing if it is placed in the computation queue
    global freq_of_cpu
    global end_time  # t + τm − 1
    global deadline
    global wait_time_comp_processed_or_dropped  # lm(compt) ∈ T
    global processing_delay_comp_time_slots  # comp δm (t)
    global wait_time_trans_processed_or_dropped  # lm trans (comp)
    global processing_delay_trans_time_slots  # trans δm (t)

    deadline = 1  # for the 10 time slots

    # task_bits = {2.0, 2.1, . . . , 5.0} Mbits
    # task_len = random.randint(1,100)

    comp_que = []  # que for the comp
    trans_que = []  # que for the transmission

    freq_of_cpu = 2.5  # 2.5GHz this is in the clock cycles
    processing_density = 0.297  # gigacycles per Mbits

    def __init__(self, task_and_time):
        self.task_and_time = task_and_time
        # print(self.task_and_time)

 # make the que in the mobile device

 # if the task arrive then make a variable km(t)

 # make a logic for unique km_t generation and also setting the bits of the task as zero if we get 0 at that position

    def task_id_gen(self, task_and_time):
      # self.task_and_time = task_and_time
        for i in range(episode):
            if task_and_time[i][1] == 0:
                task_and_time[i].append(0)  # make the km_t as the 0
                task_and_time[i][2] = 0
            else:
              # here we append the km_t the unique id of the slor
                task_and_time[i].append(random.randint(1, 1000))
        return task_and_time

 # making the offload decision of the tasks in the ques

    def task_offload(self, task_and_time):

        processing_delay_comp_time_slots_lst = []  # for the comp que
        processing_delay_trans_time_slots_lst = []  # for the trans que
        wait_time_comp_processed_or_dropped_lst = []
        wait_time_trans_processed_or_dropped_lst = []
        trans_que_var_lst = []
      # making the lst to store the processing_delay_comp_time 
        for i in range(episode):

          # need to change as per the deep q of the
          # the mobile device will know before the

          # dummy test
           #make the processing delay time slot lst and the comp delay time slot lst as well
            task_offload_var = random.randint(0,1) #the x_m(t) the action will be changed later based on the model
            #print(task_offload_var)
            #make the processing delay time slot lst and the comp delay time slot lst as well
            if task_offload_var == 1 :
           
                
          # calualte the load for the comp que
                if len(wait_time_comp_processed_or_dropped_lst) == 0:
                    processing_delay_comp_time_slots = 0
                    wait_time_comp_processed_or_dropped  = min(task_and_time[i][0] + processing_delay_comp_time_slots + (task_and_time[i][2])/(2.5*0.1)/0.297, task_and_time[i][0] + 10 -1)
                    wait_time_comp_processed_or_dropped_lst.append(wait_time_comp_processed_or_dropped)
                    processing_delay_comp_time_slots_lst.append(processing_delay_comp_time_slots)
                #print(wait_time_comp_processed_or_dropped_lst)
        
                else:
                    #print(task_and_time[i][0])
                    #print(processing_delay_comp_time_slots)
                    processing_delay_comp_time_slots = max(wait_time_comp_processed_or_dropped_lst) - task_and_time[i][0] + 1  # equation 2
                    processing_delay_comp_time_slots_lst.append(processing_delay_comp_time_slots)
                    wait_time_comp_processed_or_dropped = min(task_and_time[i][0] + processing_delay_comp_time_slots + (task_and_time[i][2])/(2.5*0.1)/0.297, task_and_time[i][0] + 10 -1)
                    wait_time_comp_processed_or_dropped_lst.append(wait_time_comp_processed_or_dropped)
                    
     
            #do the append logic in for the comp que
                #print(task_and_time[i][2])
                comp_que.append(task_and_time[i][2])  #dummy testing for append of the bits
                #checking
                #print(i,comp_que,task_offload_var)
    
    
    
            else:
                if len(wait_time_trans_processed_or_dropped_lst)==0:
                    processing_delay_trans_time_slots = 0
                    wait_time_trans_processed_or_dropped = min( task_and_time[i][0] + processing_delay_trans_time_slots + (task_and_time[i][2])/(14*0.1) -1 , task_and_time[i][0] + 10 - 1 )
                    wait_time_trans_processed_or_dropped_lst.append(wait_time_trans_processed_or_dropped)
                    processing_delay_trans_time_slots_lst.append(processing_delay_trans_time_slots)
                else:
                    processing_delay_trans_time_slots = max(wait_time_trans_processed_or_dropped_lst) - task_and_time[i][0] + 1 #equation 5
                    processing_delay_trans_time_slots_lst.append(processing_delay_trans_time_slots)
                    wait_time_trans_processed_or_dropped = min( task_and_time[i][0] + processing_delay_trans_time_slots + (task_and_time[i][2])/(14*0.1) -1 , task_and_time[i][0] + 10 - 1 )
                    wait_time_comp_processed_or_dropped_lst.append(wait_time_trans_processed_or_dropped)
    
                #do the append logic for the trans que
    
                #trans_que.append(task_and_time[i][0])
                #now appending the time in this
                trans_que.append(task_and_time[i][2])
                #chekcing 
                #print(i,trans_que,task_offload_var)
                #trans_que.append(task_and_time[i][0])
            trans_que_var_lst.append(task_offload_var)
        #storing the values in this lst for the refrence
        trans_que_with_offload_var_lst = []
        #make the decision to offload to the edge node we define the ym(t)
        
        for j in range(len(trans_que)):
            small_lst = []
            #the decision variable made here 
            task_offload_trans_var = random.randint(0,1)
            small_lst.append(trans_que[j])
            small_lst.append(task_offload_trans_var)
            trans_que_with_offload_var_lst.append(small_lst)
            
        #print(trans_que)
        #print(comp_que)
        return trans_que_with_offload_var_lst,trans_que, comp_que , wait_time_comp_processed_or_dropped_lst , wait_time_trans_processed_or_dropped_lst , processing_delay_comp_time_slots_lst , processing_delay_trans_time_slots_lst

    #calculation of the length of the que
    '''
    qm,nedge(t) = qm,n(t edge− 1) + λedgem,n (t) + edge #−fn ∆ 1 (m ∈ Bn (t)) − em,n(t) edge
 
    
    '''

    #let the task dropped be zero for now
    def cal_length_que(self,trans_que_with_offload_var_lst):
        q_m_n_lst = []
        q_m_n = 0
        self.trans_que_with_offload_var_lst = trans_que_with_offload_var_lst
        #print(trans_que_with_offload_var_lst)
        for i in range(len(trans_que_with_offload_var_lst)):
            if i == 0 : 
                q_m_n_lst.append(0)
            elif i > 0:
                q_m_n= q_m_n_lst[i-1] + self.trans_que_with_offload_var_lst[i][0] + ((2.5*0.10/0.297 ) - 0)  #eq 8
                #print(q_m_n)
                q_m_n_lst.append(q_m_n)
        
        return q_m_n_lst

        
  

m1 = mobile_device(task_and_time)


trans_que_new = (m1.task_offload(m1.task_and_time))

#print(m1.task_id_gen(m1.task_and_time))

print(trans_que_new)

print(m1.cal_length_que(trans_que_new[0]))

#print(m1.task_id_gen(m1.task_and_time))
#print(f'complete que= {trans_que_new}')
#print(f'upper trans que 1st element - {trans_que_new[0]}') 




class node_device:
    global edge_node_que #que in the edge node
    global b_n #denote the set of the active ques
    b_n =1  #set of the active ques
    edge_node_que = []
    global q_edge  #q_edge is the time slot at the at time slot 0 is 0
    q_edge = 0 # is taken as zero for the simplicity
    def __init__(self, node_trans_que):
        self.node_trans_que = node_trans_que

    #make a logic for the que length and updation of the length
    def task_id_gen_node(self,node_trans_que):
        #print(node_trans_que[1])
        #print(node_trans_que[2])

        node_trans_que = node_trans_que[0]
        #print(node_trans_que)
        for a in range(len(node_trans_que)):
            #make the unique if for the km(t) in the edge node
            if node_trans_que[a][1] == 0:
                node_trans_que[a][0] =0
            else:
                node_trans_que[a][1] = (random.randint(1, 1000))

        #-----------------------------to append time as well in the que--------------------------------------------------------#
        #working on this logic
        for b in range(0,episode):
            for z in range(0,len(node_trans_que)):
                if task_and_time[b][2] == node_trans_que[z][0]:
                    node_trans_que[z].append(task_and_time[b][0])
                else:
                    continue
        #make the logic to calculate the 

        #------------------------------------------------------------------#  

        return node_trans_que #node_trans_que[0]
        #the task are in the bits with the unique number integer value
    

    def task_dropping_and_processing(self,node_tras_que):
        self.node_trans_que = node_tras_que
        return node_tras_que

# make an instance

n1 = node_device(trans_que_new)

#print(n1.len_of_que(n1.node_trans_que))

print(n1.task_id_gen_node(n1.node_trans_que))



#-------------------------------------------------------for the sake of simplicity the load matrix is consider as 1 as there is only one ques and one load ---------------------------------#

#make the states and the input to the model

'''sm(t) = λm (t), δmcomp(t), δmtran(t), q m edge(t − 1), H(t) '''

#make the state and the inputs now 

# for the simplicity task bits dropped has been taken as 0
#action is a tuple of ym(t) and xm(t)

#am(t) = (xm (t), ym (t))  its a tuple 

#cost and delay calculation is 
#if xm(t) == 1
#Delaym(sm (t), am(t)) = lmcomp(t) − t + 1;
#else 
# eqn 16
#- make a simple state with one input
#


# we can access all the variables
class The_input(node_device,mobile_device):
    def __init__(self,task_and_time,trans_que):
        self.task_and_time = task_and_time
        self.trans_que = trans_que
    
    def input_state(self,task_and_time,trans_que):
        self.task_and_time
        self.trans_que
        return task_and_time , trans_que , 
        

 
inp_1 = The_input(task_and_time,trans_que)   
print(inp_1.input_state(task_and_time,trans_que))





























