f = open("demo.txt","a+")
# nonlocal i =2

f.write("\n hi i am here.")
f.seek(0)
data = f.read()
print(data)
f.close