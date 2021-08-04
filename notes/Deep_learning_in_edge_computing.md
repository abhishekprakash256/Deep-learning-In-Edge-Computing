## Deep learning in Edge Computing



### Problems - 

- Mobile device model and task model what is the connection ?
- understand all the notation

### Notations - 

- We consider a set of edge nodes N = {1, 2, . . . , N }
- set of mobile devices M = {1, 2, . . . , M }
-  time slots T = {1, . . . , T }
-  Z++ to denote the set of positive integers.
- then we define a variable km(t) ∈ Z++ to denote the unique index of the task
- Let λm (t) (in bits) denote the number of bits of the newly arrived task at the beginning of time slot t ∈ T 
- km (t) to be from a discrete set Λ , {λ1 , λ2 , · · · , λ|Λ| } with |Λ| available values.
- processing density of ρm 
- deadline τm 
- λm (t)xm (t) is the number of bits arrived at the computation queue of mobile device m
- λm(t)(1 − xm (t)) is the number of bits arrived at the transmission queue of mobile device m.
-  Let fm device (in CPU cycles per second) denote the processing capacity of the CPU of mobile device m ∈ M.
- we define lm (t) ∈ T to denote the time slot when task km (t) has either been processed or dropped
- comp Let δm (t) (in time slots) denote the number of time slots that task km (t) will wait for processing if it is placed in the computation queue.
-  Let |hm,n |2 denote the channel gain from mobile device m ∈ M to edge node n ∈ N .
- Let P denote the transmission power of a mobile device. 
- transmission rate from mobile device m to edge node n, denoted by rm,n  tran (in bits per second), is computed as follows
-  W denotes the bandwidth allocated to a channel
- edge  a variable km,n (t) ∈ Z++ to denote the unique index of the task. 
- edge Let λm,n (t) ∈ Λ ∪ {0} (in bits) denote the number of bits arrived in the queue of mobile device m at edge node n at the beginning of time
- Let edge qm,n (t) (in bits) denote the length of the queue of mobile device m ∈ M at edge node n ∈ N at the end of time slot t ∈ T
- Let Bn (t) denote the number of active queues at edge node n in time slot t, i.e., Bn (t) = |Bn (t)|.
- edge Let fn (in CPU cycles per second) denote the processing capacity of edge node n.
- edge we define a variable lm,n (t) ∈ T to  denote the time slot when this task has either been processed or dropped by edge node n
- matrix H(t) denote the history of the load level
- It is a matrix with size T step × N . Let {H(t)}i,j denote the (i, j) element of H(t).
- Let S denote the discrete and finite state space of each mobile device,
  i.e., S = Λ × {0, 1, . . . , T }2 × QN × {0, 1, . . . , M }T step×N
- where Q denotes the set of the available values of the queue length at an edge node within the T time slots.
- Let A denote the action space, i.e., A = {0, 1} 1+N .
- A policy of device m ∈ M is a mapping from its state to its action, i.e., πm : S → A.
- The expectation E[·] 
-  Let θ m denote the parameter vector of the neural network of device m,
- A and V layer -> advantage and value layer
-  For mobile device m ∈ M, let Am (sm (t), a; θ m ) denote the action-advantage value of action a under state sm(t) ∈ S with network
  parameter vector θ m.
- Since there are E episodes, the computational complexity of the proposed algorithm is O(LKE|I|).
- let Mn ⊂ M denote the set of mobile devices whose training is performed by edge node n ∈ N ,
  i.e., Mn = {m ∈ M | nm = n}.
- maintains a replay memory Dm for device m ∈ Mn.
- an evaluation network, denoted by Netm , and a target network, denoted by Target Netm .
-  where E denotes the number of episodes. At the beginning of each episode, mobile
  device m ∈ M initializes the state.

### Formula - 

- ![image-20210727173742923](file:///home/abhi/.config/Typora/typora-user-images/image-20210727173742923.png?lastModify=1628005852)

​                                                                                                  The task offloading to the queue

- ![image-20210803120921424](/home/abhi/.config/Typora/typora-user-images/image-20210803120921424.png)
- 

​                                                                                     ![image-20210803121030982](/home/abhi/.config/Typora/typora-user-images/image-20210803121030982.png)

- ![image-20210803122116679](/home/abhi/.config/Typora/typora-user-images/image-20210803122116679.png)
- ![image-20210803122907178](/home/abhi/.config/Typora/typora-user-images/image-20210803122907178.png)
- ![image-20210803124841439](/home/abhi/.config/Typora/typora-user-images/image-20210803124841439.png)
- ![image-20210803125243514](/home/abhi/.config/Typora/typora-user-images/image-20210803125243514.png)
- ![image-20210803125640614](/home/abhi/.config/Typora/typora-user-images/image-20210803125640614.png)
- ![image-20210803125952117](/home/abhi/.config/Typora/typora-user-images/image-20210803125952117.png)
- ![image-20210803130705635](/home/abhi/.config/Typora/typora-user-images/image-20210803130705635.png)
- ![image-20210803131119229](/home/abhi/.config/Typora/typora-user-images/image-20210803131119229.png)
- ![image-20210804100050404](/home/abhi/.config/Typora/typora-user-images/image-20210804100050404.png)
- ![image-20210804100655159](/home/abhi/.config/Typora/typora-user-images/image-20210804100655159.png)
- ![image-20210804102649196](/home/abhi/.config/Typora/typora-user-images/image-20210804102649196.png)
- ![image-20210804110444161](/home/abhi/.config/Typora/typora-user-images/image-20210804110444161.png)
- ![image-20210804111456138](/home/abhi/.config/Typora/typora-user-images/image-20210804111456138.png)
- ![image-20210804114412953](/home/abhi/.config/Typora/typora-user-images/image-20210804114412953.png)
- ![image-20210804121905747](/home/abhi/.config/Typora/typora-user-images/image-20210804121905747.png)
- ![image-20210804143757349](/home/abhi/.config/Typora/typora-user-images/image-20210804143757349.png)
- 

### Abstract-

- The offloading problem in the edge devices 

### Background and Motivation - 

- Device may not have enough power to process the data

- To facilitate efficient task processing, mobile edge computing (MEC) [1], also known as fog computing [2] and multi-access edge computing [3],
  is introduced.
  
- Two main questions - 
  - The first question is whether a mobile device should offload its task to an edge node or not. 
  - The second question is that if a mobile device decides to perform offloading, then which edge node should the device off-load its task to
  
-  When a large number of mobile devices offload their tasks to the same edge node, the load at that edge node can be high, and hence those offloaded tasks
  may experience large processing delay.
  
-  Designing such a distributed algorithm is challenging. 
  - This is because when a device makes an offloading decision, the device does not know a priori the load levels at the edge nodes, since the load also depends on the offloading decisions of other mobile devices. In addition, the load levels at the edge nodes may change over time.

- In this work, we focus on the task offloading problem in an MEC system and propose a distributed algorithm that addresses the unknown load level dynamics at the edge nodes.

-  we consider non-divisible tasks together with queuing systems and take into account the practical scenario where the processing and
  transmission of a task can continue for multiple time slots.

- This approach enables the agents to make decisions based on local observations without the knowledge of the system modeling and dynamics

  ### Solution Approach and Contributions

  -  In the proposed algorithm, each mobile device can determine the offloading decision in a decentralized manner using its information observed locally, including the size of its task, the information of its queues, and the historical load levels at the edge nodes. 
  - Task offloading Problem - We formulate a task offloading problem for non-divisible and delay-sensitive tasks. The problem takes into
    account the load level dynamics at the edge nodes and aims at minimizing the expected long-term cost of the tasks (considering the delay of the tasks and the penalties for those tasks being dropped).
  - DRL-based Task Offloading Algorithm:- To achieve the expected long-term cost minimization, we propose a model-free DRL-based distributed offloading algorithm that enables each mobile device to make its offloading decision without knowing the task models and offloading decisions of other mobile devices. To improve the estimation of the expected long-term cost in the proposed algorithm, we incorporate the long short-term memory (LSTM), dueling deep Q-network (DQN), and double-DQN techniques.
  - Performance Evaluation: We perform simulations and show that when compared with the potential game based offloading algorithm (PGOA) in [14] and the user-level online offloading framework (ULOOF) in [15], our proposed algorithm can better exploit the processing capacities of the mobile devices and edge nodes, and it can significantly reduce the ratio of dropped tasks and the average delay.

  ### System Model - 

  - We consider a set of edge nodes N = {1, 2, . . . , N } , set of mobile devices M = {1, 2, . . . , M }, set of time slots
    T = {1, . . . , T } ,  where each time slot has a duration of ∆ seconds. 

    ![](/home/abhi/Pictures/screen_5.png)

    ### Mobile Device Model - 

    - We focus on computational tasks of mobile devices, where each task is non-divisible such that it can either be processed
      locally or be offloaded to an edge node for processing.

    -  We assume that at the beginning of each time slot, a mobile device has a new task arrival with a certain probability.

    - When a mobile device has a new task arrival, it first needs to decide whether to process the task locally or offload it to an edge node. 

    -  If the mobile device decides to process the task locally, then its scheduler (see Fig. 1) will place the task to the computation queue for processing

    - Otherwise, the mobile device needs to decide which edge node the task is offloaded to.

      

    ### Task Model - 

    - At the beginning of time slot t ∈ T , if mobile device m ∈ M has a newly arrived task, then we define a variable km(t) ∈ Z++ to denote the unique index of the task. If mobile device m does not have a new task arrival at the beginning of time slot t, then km(t) is set to zero for presentation simplicity.
    -  If mobile device m does not have a new task arrival at the beginning of time slot t, then km(t) is set to 0
    - Let λm (t) (in bits) denote the number of bits of the newly arrived task at the beginning of time slot t ∈ T .
    -  If there exists a new task km (t) at the beginning of time slot t, then λm(t) is equal to the size of task km (t),  Otherwise, λm (t) is set to zero.
    -  We set the size of task km (t) to be from a discrete set Λ , {λ1 , λ2 , · · · , λ|Λ| } with |Λ| available values.
    - That is, if task km(t) has not been completely processed by the end of time slot t + τm − 1, then it will be dropped immediately.

    

    ### Task Offloading Decision - 

    - If mobile device m ∈ M has a newly arrived task km(t) at the beginning of time slot t ∈ T , then it needs to make the offloading decision for task km(t) as follows.

    - First, let binary variable xm(t) ∈ {0, 1} denote whether task km (t) is to be processed locally or offloaded to an edge node. We set xm (t) = 1 (or 0) if the task is to be processed locally (or to be offloaded to an edge node). At the beginning of time slot t, λm (t)xm (t) is the number of bits arrived at the computation queue of mobile device m, and λm(t)(1 − xm (t)) is the number of bits arrived at the transmission queue of mobile device m.

    - Second, if task km (t) is to be offloaded to an edge node, then let binary variable ym,n(t) ∈ {0, 1} denote whether task km(t) is offloaded to edge node n ∈ N or not. We set ym,n(t) = 1 if task km(t) is offloaded to edge node n, and ym,n (t) = 0 otherwise. Let ym (t) = (ym,n (t), n ∈ N ). Note
      that each task can be offloaded to one edge node, i.e., where the indicator 1(z ∈ Z) = 1 if z ∈ Z , and is equal to zero otherwise.

      ![image-20210727173742923](/home/abhi/.config/Typora/typora-user-images/image-20210727173742923.png)

      ### Computation Queue - 

      - The computation queue operates in a first-in first-out (FIFO) manner.
      - The value of fm device is a constant. At the beginning of time slot t ∈ T , if task km(t) is placed in the computation queue,
      - Without loss of generality, if either task km(t) is not placed in the comp computation queue or km(t) = 0, then we set lm (t) = 0.
      - comp Let δm (t) (in time slots) denote the number of time slots that task km (t) will wait for processing if it is placed
        in the computation queue. Note that mobile device m will comp compute the value of δm (t) before it decides the queue to place the task. Given lm comp(t0 ) for t0 < t, the value of δm comp (t) is computed as follows. For m ∈ M and t ∈ T
      - ![image-20210803120916462](/home/abhi/.config/Typora/typora-user-images/image-20210803120916462.png)
      
      ### Transmission Queue 
      
      - The transmission queue operates in a FIFO manner. The arrivals are the tasks to be offloaded to the edge nodes.
      - The wireless network link interface at the mobile device sends the tasks in the transmission queue to the chosen edge node. The wireless network model and the transmission rate from a mobile device to an edge node are as follows.
      -  We consider a wireless network model where mobile devices transmit on orthogonal channels. The wireless transmission from a mobile device to an edge node suffers from path loss and small-scale fading

  ### Edge node model - 

  - Each edge node n ∈ N maintains M queues, each queue corresponding to a mobile device in set M. We assume that after an offloaded task is received by an edge node in a time slot, the task will be placed in the corresponding queue at the edge node at the beginning of the next time slot.

  -  Specifically, if task km (t0) for t0 ∈ {1, 2, . . . , t − 1} is sent to edge node n in time slot t − 1, then km,n edge  (t) = km(t0 ).

  - edge slot t. If task km,n (t) is placed in the corresponding queue edge at the beginning of time slot t, then λm,n(t) is equal to the edge
     edge size of task km,n (t). Otherwise, λm,n(t) = 0.

    ### Queues at Edge Nodes

    - The queue associated with a mobile device at an edge node operates in a FIFO manner.
    - Among those queues at edge node n, we refer to the queue of mobile device m as an active queue in time slot t if
      either there is a task of mobile device m arrived at the queue edge in time slot t (i.e., λm,n (t) > 0) or the queue is non-empty
      edge at the end of time slot t − 1 (i.e., qm,n (t − 1) > 0). Let Bn (t) denote the set of active queues at edge node n in time slot t. That is, for n ∈ N and t ∈ T 
    - We consider a scenario where the tasks of mobile devices have the same priority.1 Each edge node has one CPU for processing the tasks in the queues. In each time slot t ∈ T , the active queues at edge node n ∈ N (i.e., the queues in set Bn (t)) equally share the processing capacity of the CPU at edge node n

    ### Task Processing or Dropping

    -  Due to the uncertain future load at edge node n, mobile device m and edge node n edge
      are unaware of the value of lm,n (t) until the associated task edge km,n (t) has either been processed or dropped. Without loss edge
       edge of generality, if km,n (t) = 0, then we set lm,n (t) = 0.
    - For the definition of variable lm,n (t), let b  lm,n (t) denote edge
      the time slot when the processing of task km,n (t) starts, i.e., for m ∈ M, n ∈ N , and t ∈ T ,
    - edge where we set lm,n(0) = 0. Specifically, the time slot when edge the processing of task km,n(t) starts is no earlier than the
      time slot when the task arrives in the queue or when each task arrived earlier has been processed or dropped.
    - edge Specifically, the size of task km,n (t) is no larger than the total processing capacity that edge node n allocated to mobile
      edge edge device m from time slot lm,n b (t) to lm,n (t), and it is larger
      edge edge than that from time slot b lm,n (t) to lm,n (t) − 1.

    

    ### Task offloading Problem in MEC - 

    - At the beginning of each time slot, each mobile device observes its state (e.g., task size, queue information). If there
      is a new task to be processed, then the mobile device chooses an action for the task.

    - The state and action will result in a cost (i.e., the delay of the task if the task is processed, or a penalty if it is dropped) for the mobile device. The objective of each device is to minimize its expected long-term cost by optimizing the policy mapping from states to actions.

      

      ### State - 

      - Let matrix H(t) denote the history of the load level (i.e., the number of active queues) of each edge node within the
        previous T step time slots (i.e., from time slot t − T step to time slot t − 1). It is a matrix with size T step × N . Let {H(t)}i,j
        denote the (i, j) element of H(t), which corresponds to the load level of edge node j in the ith time slot starting from time slot t − T step (i.e., time slot t − T step + i − 1). 
      - To obtain H(t), we assume that each edge node broadcasts its number of active queues at the end of each time slot. Even
        when all M queues at an edge node are active, the number of active queues can be represented by blog2 M c+1 bits. For
        example, if there are 1000 mobile devices, then a maximum of 10 bits are required. Hence, the broadcast of the number
        of active queues only incurs a small signaling overhead
      -  Note that mobile device m ∈ M can obtain state information comp tran λm (t), δm (t), and δm
         (t) through local observation at the beginning of time slot t. Meanwhile, mobile device m can edge compute q m (t − 1) locally according to (8).
      - Specifically, mobile device m is aware of the number of bits that it has transmitted to an edge node in each time slot. In addition, it can compute the number of bits that have been processed or being dropped by an each edge node in each time slot.3

      ### Action 

      - At the beginning of time slot t ∈ T , if mobile device m ∈ N has a new task arrival km (t), then it will choose actions for
        task km(t): (a) whether to process the task locally or offload it to an edge node, i.e., xm (t); (b) which edge node the task
        is offloaded to, i.e., y m (t). Hence, the action of device m in time slot t is represented by the following action vector:

      ### Cost - 

      - If a task has been processed, then the delay of the task is the duration between the task arrival and the time when the
        task has been processed.4 Let Delaym (sm (t), am (t)) (in time slots) denote the delay of task km (t), given state sm(t) and
        action am (t). For m ∈ M and t ∈ T , if xm (t) = 1, then

        ![image-20210804100632357](/home/abhi/.config/Typora/typora-user-images/image-20210804100632357.png)

      - Specifically, consider task km (t) arrived at the beginning of time slot t. If task km (t) is placed in the compu-
        comptation queue for local processing, then lm (t) is the time slot when the task has been processed. If task km(t) is placed in the transmission queue for offloading,then P n∈N PT t0 =t 1(km,n edge(t0 ) = km (t))lm,n edge (t0) is the time slot when the task has been processed. This is because 1(km,n edge (t0) = km (t)) = 1 indicates that task km(t) has arrived at the queue of edge node n ∈ N at the beginning
        of time slot t0 , and lm,n(t0 edge) is the time slot when the task of device m arrived at edge node n at the beginning of time slot t0 has been processed.

      - ![image-20210804101718154](/home/abhi/.config/Typora/typora-user-images/image-20210804101718154.png)

      - There is a cost cm (sm (t), am (t)) associated with task km(t). If task km (t) has been processed, then

      - In the remaining part of this work, we use the short form cm(t) to denote cm (sm (t), am (t)).

      

      ### Problem Formulation - 

      - A policy of device m ∈ M is a mapping from its state to its action, i.e., πm : S → A.

      - We aim to find the optimal policy πm ∗ for each device m such that its expected long-term cost is minimized, i.e.

        ![image-20210804102641037](/home/abhi/.config/Typora/typora-user-images/image-20210804102641037.png)

        ### DRL Problem - 

    - As deep Q-learning is a model-free approach, the proposed algorithm can address the complicated
      system setting and interaction among the mobile devices without a priori knowledge of the system and interaction
      dynamics. Meanwhile, the proposed algorithm can handle the potentially large state space of the system.

    - In the proposed algorithm, each mobile device aims to learn a mapping from each state-action pair to a Q-value,which characterizes the expected long-term cost of the state-action pair. 

    - Based on the mapping, each device can select the action inducing the minimum Q-value under its state to minimize
      its expected long-term cost. 

      

      ### N N

      - The objective of the neural network is to find a mapping from each state to a set of Q-values of the actions.
      - shows an illustration of the neural network of mobile device m ∈ M. Specifically, the state information is passed to the neural network through an input layer. 
      -  Then, we use an LSTM layer to predict the load levels (at the edge nodes) in the near future based on the load level history. After that, the
        mapping from all the states (except the load level history) and the predicted load levels to the Q-values are learned through two fully-connected (FC) layers.
      - Meanwhile, dueling DQN technique [25] is applied to improve the learning efficiency of the mapping from states to Q-values through
        an advantage and value (A&V) layer.
      - Finally, the Q-values of the actions are determined in the output layer.
      - Let θ m denote the parameter vector of the neural network of device m, which includes the weights of all connections and the
        biases of all neurons from the input layer to the A&V layer. The details of each layer are as follows.

      

      ### Input layer - 

      - This layer is responsible for taking the state as input and passing them to the following layers
      - For mobile device comp tran m ∈ M, the state information λm (t), δm (t), δm (t), and
        edge qm (t − 1) will be passed to the FC layer, and H(t) will be passed to the LSTM layer for load level prediction.

      ### LSTM layer - 

      - This layer is responsible for learning the dynamics of the load levels at edge nodes and predicting the load levels
        in the near future.
      - This is achieved by including an LSTM network [26], which is a widely used approach for learning
        the temporal dependence of sequential observations and predicting the future variation of time series.
      - ![image-20210804111842523](/home/abhi/.config/Typora/typora-user-images/image-20210804111842523.png)
      - Specifically, the LSTM network takes the matrix H(t) as input so as to learn the load level dynamics. Fig. 3 shows the
        structure of an LSTM network. The LSTM network contains T step
      - LSTM units, each of which contains a set of hidden neurons. Each LSTM unit takes one row of H(t) as input,
        we let {H(t)}i denote the ith row of H(t) in Fig. 3. These LSTM units are connected in sequence so as to keep track of
        the variations of the sequences from {H(t)}1 to {H(t)}T step 
      - The LSTM network will output the information that indicates the dynamics of the load levels in
        the future in the last LSTM unit, where the output will be passed to the next layer for further learning.

      ### FC layers - 

      - The two FC layers are responsible for learning the mapping from the state and the learned load level dynamics to the Q-
        values of the actions. Each FC layer contains a set of neurons with rectified linear unit (ReLU), which are connected with
        the neurons in the previous and following layers

      ### A & V and output layer - 

      - The A&V layer and the output layer implement the dueling-DQN technique [25] and determine the Q-value of each
        action as output
      - The main idea of the dueling-DQN is to first separately learn a state-value (i.e., the portion of the Q- value resulting from the state) and action-advantage values (i.e., the portion of the Q-value resulting from the actions).
      - It then uses the state-value and action-advantage values to determine the Q-values of state-action pairs. This technique
        can improve the estimation of the Q-values through separately evaluating the expected long-term cost resulting from
        a state and an action.
      -  The network A contains an FC network, and it is responsible for learning the action-
        advantage value of each action a ∈ A. 
      - The network V contains an FC network, and it is responsible for learning the state-value. For
        mobile device m, let Vm (sm (t); θ m) denote state-value of state sm (t) with network parameter vector θ m.
      - The values of Am (sm(t), a; θm) and Vm (sm(t); θm ) are determined by the parameter vector θ m and the neural network structure
        from the input layer to the A&V layer, where vector θ m is adjustable and will be trained in the DRL-based algorithm
      - Based on the A&V layer, for mobile device m ∈ M, the resulting Q-value of action a ∈ A under state sm (t) ∈ S in
        the output layer is given as follows
      - ![image-20210804114404168](/home/abhi/.config/Typora/typora-user-images/image-20210804114404168.png)
      - ![image-20210804121911343](/home/abhi/.config/Typora/typora-user-images/image-20210804121911343.png)

      

      ### DRL-Based Algo - 

      - In our proposed DRL-based algorithm, we let edge nodes help mobile devices to train the neural network to alleviate
        the computational loads at the mobile devices. 
      - Specifically, for each mobile device m ∈ M, there is an edge node
        nm ∈ N which helps device m with the training
      - The DRL-based algorithm to be executed at mobile device m ∈ M and edge node n ∈ N are given in Algorithms
        1 and 2, respectively. The key idea of the algorithm is to train the neural network using the experience (i.e., state,
        action, cost, and next state) of the mobile device to obtain the mapping from state-action pairs to Q-values, based on
        which the mobile device can select the action leading to the minimum Q-value under the observed state to minimize its
        expected long-term cost.
      - The replay memory Dm stores the observed experience (sm (t), am (t), cm(t), sm (t+1)) of mobile device m for some
        t ∈ T , where we refer (sm (t), am (t), cm(t), sm (t + 1)) as experience t of mobile device m.
      -  Meanwhile, the edge node n ∈ N maintains two neural networks for device
        m ∈ Mn , including an evaluation network, denoted by Netm , and a target network, denoted by Target Netm
      - evaluation network Netm is used for action selection. The target network Target Netm is used for characterizing a
        target Q-value, which approximates the expected long-term cost of an action under the observed state.
      -  Hence, the Q-values of Netmand Target Netm are represented by Qm (sm (t), a; θm ) and −Qm(sm (t), a; θm ) under observed state sm (t) ∈ S and action a ∈ A, respectively. The initialization of the replay memory Dm and two neural networks are given in steps
        1−3 in Algorithm.
      - 

​                      

