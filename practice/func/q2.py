list = [11,22,"kedar",44,55,"bhame",77,88,99,"end"]
# print(list)
def p_list(list,idx=0):
    if(idx == len(list)):
        return 
    
    print(list[idx],end=" ")
    p_list(list,idx+1)
p_list(list)