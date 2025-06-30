x = [1,2]
x_copy = x
print("Before changing x -")
print("x = ",x)
print("x = ",id(x))
print("x = ",x_copy)
print("x = ",id(x_copy))
# x = x + [3,4]
x += [3,4]
print("After changing x -")
print("x = ",x)
print("x = ",id(x))
print("x = ",x_copy)
print("x = ",id(x_copy))