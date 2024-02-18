def outer():
    def inner1():
        print("in inner1 fun")
    inner2()
    def inner2():
        print("in inner2 fun")
    print("in outer fun")
outer()

'''UnboundLocalError: local variable 'inner2' referenced before assignment'''
#there are before assign the fun givr call the function

