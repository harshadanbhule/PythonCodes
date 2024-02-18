def outer():
    def inner(outer):
        print(outer)
        return inner
    
    return inner(outer)

if __name__=="__main__":
    retObj=outer()
    print(retObj)

#<function outer at 0x7f929452fd90>
#<function outer.<locals>.inner at 0x7f92943f20e0>
