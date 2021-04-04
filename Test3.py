"""
Test program 3:
4
****
***
**
*
"""
print("Enter the value:",end="")
a=int(input())
b=a
row=0
column = 0
while row<b:
    while column<a:
        print('*',end=" ")
        column+=1
    row+=1
    column=0
    if row >= 1:
        a = a - 1
    print("")