# n = int(input("Enter the number : "))
n = 5
def fact(num):
    # fact(num) =fact(num) * fact(num-1)
    # if(num == 1):
    #     return 1
    # return fact
    fact = 1
    for i in range(1,num+1):
        fact *= i
        # print(i)
    print(fact)
        
print(fact(n))

def usd_to_inr(amount,exchange_rate):
    inr = amount * exchange_rate
    print(amount,"usd =",inr,"inr = ")
    return inr
usd_to_inr(100,83.5)