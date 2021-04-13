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
 """   
 Another way
 c = '*'
 print("Enter your value:", end=" ")
 width = int(input())
 for i in range (0,width+1):
     print(c*width, end=" ")
     i -= 1
     width = width -1
     print()
"""
