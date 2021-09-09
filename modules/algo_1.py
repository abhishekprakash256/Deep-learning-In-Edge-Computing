'''
for i in time slots:
    initlaize sm(1)
        for time slots t in T do 
            if device m has new task arrival km(t) then 
                send the paramater request to the edge node nm:
                reciever network paramter vector theta m ;
                select an action am(t) according to 22
            end if
            observe the next state sm(t+1);
            observe a set of costs ({cm(t'), }) #t' is the prevoious value
            for each task km(t') with t', do 
                Send (sm(t'), am(t'), cm(t'), sm(t'+1)) to nm
            end for
        end for
end for
'''