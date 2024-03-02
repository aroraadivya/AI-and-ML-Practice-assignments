list1 = ["m","na","i","di"]
list2 = ["y","me","s","vya"]
list3=[]
list4=[i+j for i,j in zip(list1,list2)]
for i in range(len(list1)):
    list3.append(list1[i]+list2[i])

print(list3)
print(list4)

