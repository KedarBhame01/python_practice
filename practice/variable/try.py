a = int("2577")
print("a = ",a)
b = int("2577")
print("a = ",b)
print("id(a)= ",id(a))
print("id(b)= ",id(b))
if id(a)==id(b):
    print("id of a and b are equal.")

