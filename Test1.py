"""
Test program:
r=3, C=4
****
****
****

"""
r=int(input())
c=int(input())

row=0
while row<r:
    column = 0
    while column<c:
        print('*',end=" ")
        column+=1
    row+=1
    print("")