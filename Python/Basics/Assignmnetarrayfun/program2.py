def outer():
    def inner():
        return "Hello"
    return inner

ans=outer()
ret= ans()
print(ret)
