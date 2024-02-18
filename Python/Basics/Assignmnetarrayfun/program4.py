def countnum(listnum, searchnum):
    count = 0
    for element in listnum:
        if element == searchnum:
            count += 1
    return count

listnum =[ ]
z=int(input("How many numbers you entered in list :"))
for i in range(1,z+1):
    y=int(input("Enter numbers:"))
    listnum.append(y)
searchnum= int(input("Enter number which you want to search :"))

result = countnum(listnum, searchnum)
print(f"The count of {searchnum} in the list is: {result}")

