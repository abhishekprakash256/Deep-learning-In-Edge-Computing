# all the imports of the model 
import os
import numpy as np
import torch as T
from torch._C import dtype
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


#creating a replay buffer classs for the model
class ReplayBuffer():
    def __init__(self, max_size, input_shape):
        self.mem_size = max_size
        self.mem_cntr = 0
        self.state_memory = np.zeros((self.mem_size, *input_shape), dtype= np.float32)  #getting the state from the memory
        self.new_state_memory = np.zeros((self.mem_size, *input_shape), dtype= np.float32)  #getting the new state from the memory
        self.action_memory = np.zeros(self.mem_size, dtype=np.int64) #action memory in the replay buffer
        self.reward_memory = np.zeros(self.mem_size,dtype= np.float32) #rewrad storge
        self.terminal_memory = np.zeros(self.mem_size,dtype= np.uint8) #terminal storge ----------------------------error


#a function to store the transition in the model
    def store_tranisition(self,state,action,reward,state_,done):  #state_ is for the new state
        index = self.mem_cntr % self.mem_size
        self.state_memory[index] = state
        self.new_state_memory[index] = state_
        self.reward_memory[index] = reward
        self.action_memory[index] = action
        self.terminal_memory[index] = done
        self.mem_cntr+=1

#random choice function for the buffer

    def sample_buffer(self,batch_size):
        max_mem = min(self.mem_cntr,self.mem_size)
        batch = np.random.choice(max_mem,batch_size, replace= False)
        states = self.state_memory[batch]
        actions = self.action_memory[batch]
        rewards = self.reward_memory[batch]
        states_ = self.new_state_memory[batch]
        terminal = self.terminal_memory[batch]

        return states,actions,rewards,states_,terminal

#start with the network 

class DuelingDeepNetwork(nn.Module):
    #learning rate , number of actions, name , input dims, chkpt_dir
    def __init__(self,lr,n_actions, name,input_dims,chkpt_dir):
        self.chkpt_dir = chkpt_dir
        self.checkpoint_file = os.path.join(self.chkpt_dir,name)  #save the network state there 
 
        #make the layers of the network as
        self.fc1 = nn.Linear(*input_dims,512)     #the input layer -----------------------
        self.V = nn.Linear(512,1)                 #the value layer
        self.A = nn.Linear(512, n_actions)        #the action layer

        self.optimizer = optim.Adam(self.parameters(), lr=lr)  # optmizer
        self.loss = nn.MSELoss()  #loss function 
        self.device = T.device('cuda:0' if T.cuda.is_available() else 'cpu')
        self.to(self.device)  #sending the network to the device 

    #making the feed forward network 
    def forward(self,state):
        flat1 = F.relu(self.fc1(state))
        V = self.V(flat1)
        A = self.A(flat1)

        return V, A

    # save for the check points 
    def save_checkpoint(self):
        print('---saving--the--checkpoint----')
        T.save(self.state_dict(),self.checkpoint_file)

    # load the check point file 

    def load_checkpoint(file):
        print('-------loading--the--checkpoint----------------------')
        self.load_state_check(T.load(self.checkpoint_file))

# making the agent in the network 
class Agent():
    def __init__(self,gamma, epsilon,lr,n_actions,input_dims,mem_size,batch_size,  #make the directory before running the network otherwise gives error
     eps_min = 0.01, eps_dec = 5e-7, replace = 1000, chkpt_dir= 'tmp/dueling_dqqn'): # for the hyperparamaters , replcae as per Algo
        self.gamma = gamma
        self.epsilon = epsilon
        self.lr = lr
        self.n_actions = n_actions
        self.input_dims = input_dims
        self.batch_size =  batch_size
        self.eps_min = eps_min
        self.eps_dec = eps_dec
        self.replace_target_cnt = replace 
        self.chkpt_dir = chkpt_dir
        self.action_space = [i for i in range(self.n_actions)]  #making the action space 

        self.memory = ReplayBuffer(mem_size,input_dims)  #replay buffer  ---------------------------------------error
        
        self.q_eval = DuelingDeepNetwork(self.lr , self.n_actions, input_dims= self.input_dims , name = 'task_offload_dqn_eval' , chkpt_dir = self.chkpt_dir) # one network------------------------

        self.q_tar = DuelingDeepNetwork(self.lr , self.n_actions, input_dims= self.input_dims , name = 'task_offload_dqn_target' , chkpt_dir = self.chkpt_dir)  #2nd network

        #choosing the actions 
        def choose_action(self, observation) :
            if np.random.random() > self.epsilon:
                state = T.tensor([observation], dtype=T.float).to(self.q_eval.device)
                _,advantage = self.q_eval.forward(state)
                action = T.argmax(advantage).item()
            else:
                action = np.random.choice(self.action_space)

            return action   #returinin the action

        #storing the transition 
        def store_transistion(self,state,action,reward, state_,done): #state_ is for the new state
            self.memory.store_transitions(state,action,reward,state_,done)

        #replace the target network 
        def replace_target_network(self):
            if self.learn_step_counter % self.replace_target_cnt == 0:
                self.q_next.load_state_dict(self.q_eval.state_dict())

        #decrease the eplision rate of the exploratrion 
        def decrement_epsilon(self):
            self.epsilon = self.epsilon - self.eps_dec \
                if self.epsilon > self.eps_min else self.eps_min

        #saing the checkpoint 
        def save_models(self):
            self.q_eval.save_checkpoint()
            self.q_next.save_checkpoint()

        def load_models(self):
            self.q_eval.load_checkpoint()
            self.q_next.load_checkpoint()


        #learning of the agent 

        def learn(self):
            if self.memory.mem_cntr < self.batch_size:
                return

            self.q_eval.optimizer.zero_grad()

            self.replace_target_network()


            state, action,reward,new_state, done = \
                    self.memory.sample_buffer(self.batch_size)

            states = T.tensor(state).to(self.q_eval.device)
            
            actions = T.tensor(action).to(self.q_eval.device)

            dones = T.tensor(done).to(self.q_eval.device)

            rewards = T.tensor(reward).to(self.q_eval.device)

            states_ = T.tensor(new_state).to(self.q_eval.device)


            #handles the array sizing and indices 

            indices = np.arange(self.batch_size)


            #passing the state to the network 

            V_s , A_s = self.q_next.forward(states) #current state 

            V_s_ , A_s_ = self.q_next.forward(states_) #next state 

            V_s_eval , A_s_eval = self.q_eval.forward(states_)  #eval of the next state 

            q_pred = T.add(V_s, (A_s - A_s.mean(dim=1, keepdim= True)))[indices,actions]  #The action and the batch sizes

            q_next = T.add(V_s_, (A_s_- A_s_.mean(dim=1, keepdim= True)))

            q_eval = T.add(V_s_eval, (A_s_eval- A_s_eval.mean(dim=1, keepdim= True)))


            max_actions = T.argmax(q_eval,dim =1)

            q_next[dones] = 0.0

            q_traget = rewards+ self.gamma*q_next[indices,max_actions]


            #calculation of the loss function 

            loss = self.q_eval.loss(q_traget,q_pred).to(self.q_eval.device)

            #backporpogation

            loss.backward()

            self.q_eval.optimizer.step()

            self.learn_step_counter +=1 # steppin counter

            self.decrement_epsilon()













































 




        
        
    

