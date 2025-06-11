# 4 ways to write string
a = 'kedar'
# b = ''kedar''
c = '''kedar'''
d = "kedar"
# e = ""Kedar""
f = """Kedar"""
# g = """"Kedar""""

print(a)
# print(b)
print(c)
print(d)
# print(e)
print(f)
# print(g)
b = "Hello"
print(f"id b = {id(b)}")
b= 6
print(f"id b = {id(b)}")
b = "Hello"
print(f"id b = {id(b)}")
b = 5
c = 6
c +=1
print(f"id b = {id(b)}")
print(f"id c = {id(c)}")
print(b)
print(id(b))

s = "hello"
s = "नमस्ते"
print(s)


str = "Kedar"
print(str[:5])
print(str[0:])
print(str[:-1])
print(str[-5:])
print(len(str))