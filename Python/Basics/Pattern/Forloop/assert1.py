name = input("Enter your name: ")
age = int(input("Enter your age: "))  
assert age > 0, "Age is not positive"
if age > 18:
    print(name, "is eligible for voting")
else:
    print(name, "is not eligible for voting")

