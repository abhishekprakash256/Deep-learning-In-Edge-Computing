lst  = [1,2,3,4,5]

lst_2 = []

lst_prev = [0]


for i in range(len(lst)): 
    lst_prev.append(lst[i])
    for k in range(1):
        print(lst_prev[i])
    
    

    