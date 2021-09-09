import random

trans_que = []
comp_que = []

lst= [3,0,5,6,77,4,1,7,78]

for i in range(len(lst)):
    task_offload_var = random.randint(0,1) #random 
    if task_offload_var == 1:
        trans_que.append(lst[i])
    else:
        comp_que.append(lst[i])

print(trans_que)
print(comp_que)