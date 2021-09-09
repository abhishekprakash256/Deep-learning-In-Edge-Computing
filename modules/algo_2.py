'''
initialize the replay memory Dm for and Count = 0
Initilaize Netm with random theta m 
Initailaize Target Net m with random theta m-
while True do
    if recive a paramater_request from m, then
        send theta m to device m
    end if 
    if recive and expericence (sm(t), am(t), cm(t), sm(t+1))
    from m and coverage indicator = 0, then 
        store (sm(t), am(t),cm(t),sm(t+1)) in Dm;
        Sample a set of experince (denoted by I) from Dm:
        for each i do:
            Obtain experince (sm(i),am(i),cm(i),sm(i+1));
            Compute Q target according to 26
        end for 
        set vector Q Traget = (Q target, i I)
        Update theta m to minimize L(theta m , Q target ) in 24 
        count +=1
        if mod (Count, Replace_theshold) == 0  then 
            theta m- = theta m
        end if 
    end if 
end while







'''