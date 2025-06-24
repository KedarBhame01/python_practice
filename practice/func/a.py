list = [11, 22,33 ,44]
list2 = [4,4,4,4,3,3,3,2,2,1]
def find_len(a_list): #user define function
    # print(len(a_list)) #pre define function
    count = 0
    for item in a_list:
        count += 1
        print(item,end=" ")
    print()
    print("count = ",count)
find_len(list)
find_len(list2)
