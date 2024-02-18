def outer():
    message="I am outer function"

    def inner():
        return message

    return inner

if __name__=="main":
    inner_function=outer()
    result=inner_function()
    print(result)
