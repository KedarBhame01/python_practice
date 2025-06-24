a = 0;
while a < 2:
    # print(a*5)
    if(a%2 == 0):
        print(a);
    a+=1
print("loop Ended")
list = [1,2,3,4,5]
for i in list:
    if(i == 2):
        continue;
    print(i);
    i+=1;
print("for loop Ended")