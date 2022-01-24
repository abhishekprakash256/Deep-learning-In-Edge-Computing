## Project Description - 

The project deals with the problem of the task offloading in the edge devices , where we have certain time slots and the tasks are incoming with a time stamp that is proceed under a certain amount of time. The problem is deal with using the reinforcement learning techniques using the Double Q Deep learning model. For the simulation process we have edge and node devices that does the task processing. The task offloading decision is taken by the RL model that observes the state and the space and minimize the Q values and takes the task offloading decision based on the observable values.

### Steps - 

- The task is generated with the random function with the an unique id.
- Then the task are pushed to the Edge node where the loads are calculated and the calculated loads are send to the Deep Q model as the input.
- The edge device and node device have the queue that are used to store the task and process them that works in FIFO manner.
- The model observes the respective loads and calculates the optimal task processing strategy based on state space observation.
- Based on the decision made by the model the task is either dropped or processed locally or processed in the node device.



## Notes - 

- The files directory has the final files with included model and the exp_18.py, exp_19.py and dueling_q_model.py



## Illustration - 

![](/media/abhi/Share 2/ra_work/professor_zhnag_ra_work/paper_implementation/steps.png)





