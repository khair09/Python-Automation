"""
Test program 2:
5
*
**
***
****

"""
print("Enter the value:",end="")
a=int(input())                 #a=5
b=0                            #b=0
row=0
column = 0
while row<=a:
    while column<b:
        print('*',end=" ")
        column+=1
    row+=1
    if row > 1:
        column=0
        b+=1
        print("")
 """Another way """
"""        
print("Enter your value:", end=" ")
a = int(input())
for i in range(a):
    for j in range(i+1):
        print("*", end=" ")
    print()
"""
 
