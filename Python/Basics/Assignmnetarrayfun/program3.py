'wap the function return the array of factorial of element'
import array as arr
def factorialnum(numbers):
    factanswer=arr.array('i',[])
    for element in numbers:
        n=element
        x=1
        for i in range(1,n+1):
            x*=i
        factanswer.append(x)
    return factanswer

numbers=arr.array('i',[ ])
z=int(input("how many numbers you enter:"))
for j in range(1,z+1):
    y=int(input("Enter number :"))
    numbers.append(y)
print(numbers)
answer=factorialnum(numbers)
print(answer)


