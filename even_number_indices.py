list1 =  [1 , 3 , 5 , 8 , 10 , 13 , 18 , 36 , 78 ]
list2 = []
for l in list1[::2]:
    if l % 2 == 0:
        list2.append(l)

print list2
