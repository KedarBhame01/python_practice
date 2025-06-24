with open("practice.txt",'w+') as f:
    f.write("Hi eyeryone\nwe are learning File I/O\nusing Java.\nI like programming in Java.\n")

with open("practice.txt","r+") as f:
    data = f.read()
    data2 = data.replace("Java","Python")
    f.write(data2)
    print(data2)
    
    data_finded = data2.find("learning")
    if data_finded != -1:
        print("Founded the word 'learning' at index: ",data_finded)
    f.seek(0)
    # print(data_finded)
    
data = True
line_no = 0
with open("practice.txt","r") as f:
    while data:
        data = f.readline()
        line_no += 1
        if data.find("learning") != -1:
            print("data found of line no : ",line_no)
            

        