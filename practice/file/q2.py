def count_even_no(list):
    count = 0
    for i in list:
        if int(i)%2 == 0:
            count += 1
    print(count)
    # return count
    
with open("q2.txt",'r') as f:
    data = f.read()
    
    list = data.split(',')
    print(list)
    count_even_no(list)
    
    
    # print(data)
    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == ','):
    #         print(num)
    #         num = ""
    #     else:
    #         num += data[i]
    