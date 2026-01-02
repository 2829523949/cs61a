def Newton(f,df):
    def correct(x):
        return x-f(x)/df(x)
    return correct
def improve(a,b):
    def true(c):
        while not a(c):
            c=b(c)
        return c
    return true
