class a:
    pass

class b(a):
    pass

class c(a):
    pass

class d(b,c):
    pass

class e(d):
    pass

obj=e()
print(e.mro())
