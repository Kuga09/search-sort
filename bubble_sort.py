list_1 = [18,42,23,10,66]
stop_flag = True
while stop_flag is True:
    stop_flag = False
    for i in range(0,len(list_1)-1):
        if list_1[i] > list_1[i+1]: 
            a=list_1[i+1]
            list_1[i+1]=list_1[i]
            list_1[i]=a
            stop_flag = True
print(list_1)