# num = int(input("Enter the no. "))
# i = 1
# sum = 0
# while(i <= num):
#     sum += i
#     i += 1
# print(sum)

# num = int(input("Enter number of where do you factorial want : "))
# fact = 1
# for i in range(1,num+1):
#     fact *= i
# print(fact)

i = 1
while (i < 5):
    while (i < 5):
        if (i < 5):
            if (i < 5):
                if (i < 5):
                    print(f"inside loop 5 i = {i}")
                    break
                    # i += 1
                print("inside loop 4")
                # i += 1
            print("inside loop 3")
            # i += 1    
        print("inside loop 2")
        i += 1
    print(f"inside loop 1 i = {i}")    
    i += 1
print("outside loop ")
