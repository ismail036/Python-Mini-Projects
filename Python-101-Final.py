list2 = []

def flatten(l):
    for i in l:
        if type(i) == list :    
            flatten(i)
        else:
            list2.append(i)



flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])

print(list2)
           
