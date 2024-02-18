def outer():
    def inner():
        return "Hello"
    return inner()

ans=outer()
print(ans)
