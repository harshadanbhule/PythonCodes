def outer():
    def inner():
        return outer

    return inner 

if __name__=="__main__":
    retObj=outer()
    retInner=retObj()
    print(retInner)

    #output:<function outer at 0x7f8166343d90>
