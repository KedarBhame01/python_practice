# Changing tuple but showing error 
x = (1, [2, 3])
# x_copy = x
print("Before changing x -----------")
print("x =", x)
print("id(x) =", id(x))
# print("x_copy =", x_copy)
# print("id(x_copy) =", id(x_copy))

try:
    x[1] += [4,5]
except TypeError as e:
    print("Caught exception:", e)

print("After changing x -----------")
print("x =", x)
print("id(x) =", id(x))
# print("x_copy =", x_copy)
# print("id(x_copy) =", id(x_copy))
