list = [1,2,3,2,1]
# list = [1,"Kedar","a","b","Kedar",1]
list2 = list.copy()
print("list = ", list)
print("list2 = ", list2)
list2.reverse()
if(list == list2):
    print("palindrome")
else:
    print("not palindrome")