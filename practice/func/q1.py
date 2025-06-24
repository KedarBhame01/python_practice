#Write a recursive function to calculate the sum of first n natural numbers.
n=4
def calc_sum(n):
    print(n)
    if(n == 1):
        return 1
    return (n + calc_sum(n-1))
print(calc_sum(n))