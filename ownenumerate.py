liste = ("a","b","c","d","e","f")


def own_Enumerate(list:list,start:int=0):
    locallist = list
    iteration = start
    enumerated_list =[]
    for i in range(start):
        locallist.pop(0)
    for i in locallist:
        enumerated_list.append((iteration,i))
        iteration+=1
    return(enumerated_list)

