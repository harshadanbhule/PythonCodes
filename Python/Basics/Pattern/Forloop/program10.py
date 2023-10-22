'''1  3  5
   7  9  11
   13  15  17'''

x=1
for i in range(3):
    for j in range(3):
        print(x,end="  ")
        x+=2
    print()
print()
