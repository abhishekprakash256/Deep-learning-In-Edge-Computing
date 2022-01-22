#all the imports that are needed 

import numpy as np
import random
import sys
import torch 
import ctypes
#import matplotlib as plt



#make function for the task generation in with the bits

def task_lst(time_slots):
    '''
    The function takes the time slot and generates the task randomly in each of the time slots from a dict that is given below
    '''

    bits_dict = {0: 2.0, 1: 2.1, 2: 2.2, 3: 2.3, 4: 2.4, 5: 2.5, 6: 2.6, 7: 2.7, 8: 2.8, 9: 2.9, 10: 3.0, 11: 3.1, 12: 3.2, 13: 3.3, 14: 3.4, 15: 3.5, 16: 3.6,
        17: 3.7, 18: 3.8, 19: 3.9, 20: 4.0, 21: 4.1, 22: 4.2, 23: 4.3, 24: 4.4, 25: 4.5, 26: 4.6, 27: 4.7, 28: 4.8, 29: 4.9, 30: 5.0}  # the dict of the task
    task_lst = []
    
    # the bits of the task, the task are in Mbits
    task_lst.append(bits_dict[(random.randint(0, 30))]) #taking the bits of the task and appending to the list

    #task_lst.append(task_and_time_slot_lst_2)
    return task_lst


#make the class for the mobile device 

class Mobile_device():
    '''
    the mobile device should have a computational que and a transmission que 
    the calculation of the load should be done here in the load function
    the load should be passed to the action class to the algorithm to initialize the state to pass into the comments
    the task generater is not designed now for simplicity
    '''
    def __init__(self) -> None:
        pass

    computational_que = []  #the comp que
    transmission_que = []#the trans que

    
    #the load calculation variables
    #initially all wille be set to zero as no load is there

    wait_time_comp_processed_or_dropped = 0  # lm(compt) ∈ T
    processing_delay_comp_time_slots = 0  # comp δm (t)
    wait_time_trans_processed_or_dropped = 0# lm trans (comp)
    processing_delay_trans_time_slots = 0  # trans δm (t)


    # the load calculation list that contains all the values

    processing_delay_comp_time_slots_lst = []  # for the comp que
    processing_delay_trans_time_slots_lst = []  # for the trans que
    wait_time_comp_processed_or_dropped_lst = []  # for the comp que 
    wait_time_trans_processed_or_dropped_lst = [] # for the comp que


    def load_in_mobile(self,task, time):  #pass task and the time slot as well

        '''
        the load calcultion of the task , in the transmission que and the compulational ques 
        the wait time for the task in both ques
        the processing time for the task in both the ques
        '''
        
        # to check for the starting of the time slots if count = 0 then start the time slots and all will be zero, else set the calcuation as per load evaluations
        #count = 0

        # for the comp ques
        #print(time, task)
        self.wait_time_comp_processed_or_dropped  = min(time + self.processing_delay_comp_time_slots + (task[0]/(2.5*0.1)/0.297), time + 10 -1)
        self.wait_time_comp_processed_or_dropped_lst.append(self.wait_time_comp_processed_or_dropped)  #l comp
        self.processing_delay_comp_time_slots_lst.append(self.processing_delay_comp_time_slots)
        self.processing_delay_comp_time_slots = max(self.wait_time_comp_processed_or_dropped_lst) - time + 1  # equation 2
        #need to change the processing delay as make it positive before the appending 
        if self.processing_delay_comp_time_slots > 0:
            self.processing_delay_comp_time_slots_lst.append(self.processing_delay_comp_time_slots) 
        else:
            self.processing_delay_comp_time_slots_lst.append(0) 

        #wait_time_comp_processed_or_dropped = min(time + processing_delay_comp_time_slots + (task[0]/(2.5*0.1)/0.297), time + 10 -1)  # eq 6
        #wait_time_comp_processed_or_dropped_lst.append(wait_time_comp_processed_or_dropped)  #delata trans'''


        # for the trans slots time 
        self.processing_delay_trans_time_slots = 0
        self.wait_time_trans_processed_or_dropped = min(time + self.processing_delay_trans_time_slots + (task[0])/(14*0.1) -1 , time + 10 - 1 )
        self.wait_time_trans_processed_or_dropped_lst.append(self.wait_time_trans_processed_or_dropped)
        self.processing_delay_trans_time_slots_lst.append(self.processing_delay_trans_time_slots)

        self.processing_delay_trans_time_slots = max(self.wait_time_trans_processed_or_dropped_lst) - time + 1 #equation 5
        #make the time slots positive for every iteration as per formulae as per eq 5 
        if self.processing_delay_trans_time_slots > 0 :
            self.processing_delay_trans_time_slots_lst.append(self.processing_delay_trans_time_slots)
        else:
            self.processing_delay_trans_time_slots_lst.append(0)
        #wait_time_trans_processed_or_dropped = min(time + processing_delay_trans_time_slots + (task[0]/(14*0.1) -1) , time + 10 - 1 )
        #wait_time_trans_processed_or_dropped_lst.append(wait_time_trans_processed_or_dropped)
        #print(processing_delay_trans_time_slots,"trans")

        
        
        #make the appneding with the action from the algorithm and append into the ques and the calulate the values

        return task , time, self.wait_time_comp_processed_or_dropped, self.wait_time_trans_processed_or_dropped , self.processing_delay_comp_time_slots, self.processing_delay_trans_time_slots

    def task_offload(self,task_offload_var, task):
        '''
        the task offload function takes values from the action class and make the 
        '''
    
        #make the offload here to the ques

        if task_offload_var == 0:
            self.computational_que.append(task)
        else:
            self.transmission_que.append(task)
        return self.computational_que, self.transmission_que



#check for the time slot calculations as wells in the above calculations as well , pass task and the time slot as well in load calculation functions as well





#the class for the node device 


class Node_device():
    def __init__(self) -> None:
        pass
    edge_node_que = [] # the edge node que
    b_n =1  #set of the active ques can be dynamic
    q_edge = 0 # q_edge for the start
    q_edge_lst = []
    e_edge = 0 #number of the bits that are dropped
    l_edge = 0 #denote the time slot when this task has either been processed or dropped by edge node n
     # the list to store the value of the l_edge
    l_edge_lst = []

    def load_in_node(self,task, time):
        self.l_edge_lst.append(self.l_edge)
        #print(self.l_edge)
        self.q_edge = self.q_edge + task[0] - (2.5*0.1/0.297) - 0
        self.l_edge = (max(self.l_edge_lst) + 1)  # the l_edge calcualtion as per eq_n 9 

        return self.q_edge, self.l_edge


#add the model in the simulation to make the decisions
'''
The model will be here 







'''



#The class for the Algo 2 for the model training 

class Algo_2_train():
    '''
    Implementation of the Algorithm 2 -> Algorithm 2 DRL-Based Algorithm at Edge Node n ∈ N
    '''


    def __init__(self) -> None:
        pass

    def get_experience(self,experience):
        #print(experience)
        return experience


    def get_paramater(self,paramater_request):

        '''
        Initialize replay memory Dm for m ∈ Mn and Count := 0;
        2:Initialize Netm with random θm for m ∈ Mn ;
        3:Initialize Target Netm with random θ−
        m for m ∈ Mn ;
        '''
        while True:
            
            if  paramater_request:
                print('got the paramater request')
                # if receive a parameter request from m ∈ Mn then
                # Send θm to device m;
                
            
            #recive a experience from the Algo 1 the out from the main
            if  self.get_experience:
                out = self.get_experience #get the experience for the Algo 1 and pass to Algo 2
                #print(out.value)
                #value2 = ctypes.cast(memory_address, ctypes.py_object).value
            break
        
        
        
        return "in"

        
            








































#The class for the Algo 1 

class Algo_1_Action():
    '''
    Implementation of the Algorithm 1 -> Algorithm 1 DRL-based Algorithm at Device m ∈ M
    '''
    def __init__(self) -> None:
        pass
    
    
    def train_and_action(self):
        
        m1 = Mobile_device()  #initialize the mobile device

        n1 = Node_device()  #initilaize the node device

        a2 = Algo_2_train() # for the Algo 2 to train the model
       
        state_prev = [[0,0,0,0,0]] # for storing the prevouis states 

        action_prev = [0] # for storing the previosy actions

        cost_prev  = [0] #for storing the cost of the prev 

        states= []  #for storing the current states

        out_load_lst_node_lst = [] #temprory list to store the load from the node devices

        time_slots = 1

        episode = 5

        delay = 0
        count=0
        for i in range(episode): 
            '''
            the algorithm 1 from the line 4 to 7 
            the state initilaization for the algorithm
            sm(t) = (λm (t) task, δmcomp(t) processing_delay_comp_time_slots  , δmtran (t) processing_delay_trans_time_slots, qmedge(t − 1) q_edge, H(t), 1) 
            '''
            state= []
            out_load_lst_mob = (m1.load_in_mobile(task_lst(i),i)) #the load list from the function of the mobile device
            #print(out_load_lst)

            out_load_lst_node = (n1.load_in_node(out_load_lst_mob[0],i)) #take the last value in append it in the lst
                
            out_load_lst_node_lst.append(out_load_lst_node[0]) #temporoy list to store the value of the ques from the edge node
                
            
            #make the state for passing into the model
            state.append(out_load_lst_mob[0][0])  #the state appending
            #print(out_load_lst_mob[0][0])
            state.append(out_load_lst_mob[4])
            #print(out_load_lst_mob[4])
            state.append(out_load_lst_mob[5])
            if i == 0:
                state.append(0)
            else:
                state.append(out_load_lst_node_lst[i-1])
            state.append(1)
                #print(out_load_lst_mob[5])

            states.append(state)  #state is initilaized for the current one 

            state_prev.append(state) #storing the values for the previous state to pass to the model
            
            
            for j in range(time_slots):

                #if device m has a new task arrival km (t) then 
                if True:  #if device m has a new task arrival km (t) then
                    
                    #the task offload decision in the 
                    '''
                    Send a parameter request to edge node nm ;
                    Receive network parameter vector θm;
                    '''

                    got_paramater = a2.get_paramater(True)  #sending the paramater and getting the values

                    print(got_paramater)



                    #make the action as per algo eq 22
                    task_offload_var = random.randint(0,1)  #random task variable  , model will take prediction here 

                    action_prev.append(task_offload_var)  # storing the values of the actions for the previous action

                    offloaded_task_ques = m1.task_offload(task_offload_var, out_load_lst_mob[0][0])  # the offloaded tasks in the ques

                    #print(offloaded_task_ques) #check for the task offload
                

                #observe the next state  
                #Observe a set of costs {cm(t0 ), t0 ∈ T e m,t };
                '''
                calculate the set of the costs as per eqn 15,16,17,18
                '''
                #make the delay calculation for the cost
                
                #making the observation for the precious state cost
                if count == 0:
                    delay = 0
                
                else:
                    if task_offload_var == 0: 
                        delay =  out_load_lst_node[1] - i +1 #change is at per eq 16


                    else:
                        # the delay as per eq 15 , lcomp - t + 1
                        #print('in')
                        #print(i)
                        delay = out_load_lst_mob[2] - (i-1) +1
                
                #print(state)
                count+=1
                cost = delay  # the cost per eq_n 17 and 18

                cost_prev.append(cost)
                
                '''
                 for each task km(t0 ) with t0 ∈ T e m,t do 12:
                Send (sm (t-1 ), am (t-1 ), cm(t-1), sm (t)) to nm ;
                '''

                for k in range(1):
                    '''
                    Send (sm (t0 ), am (t0 ), cm(t0 ), sm (t0 + 1)) to nm 
                    pass the following output to the neural network 
                    '''
                    experience = (state_prev[i], action_prev[i], cost_prev[i] , states[i])  # pass the data to the Nm as per Algo 1 as experience

                    a2.get_experience(experience)


                    
                    #print(out_data)

                    #print(a1.get_input(experience))


                


                   

                






              




        return states # the all states



  
a_1 = Algo_1_Action()
print(a_1.train_and_action())

