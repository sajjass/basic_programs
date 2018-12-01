from __future__ import print_function

x=[[10,20,30],[40,50,60],[70,80,90]]
print(x)
print("Elements Row wise:")
for r in x:
    print(r)
print("Elements in Matrix style:")
for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j],end=' ')
    print()