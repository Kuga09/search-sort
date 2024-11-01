list_1=[18,42,23,10,66]
sorted_list=[]
while len(list_1)>0:
    min=list_1[0]
    for i in range(0,len(list_1)):
        if min > list_1[i]:
            min=list_1[i]
    sorted_list.append(min)
    list_1.remove(min)
print(sorted_list)