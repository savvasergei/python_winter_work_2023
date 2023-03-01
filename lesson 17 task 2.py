
def fu(*args, **kwargs):
    res = ''
    for x in args:
        if type(x) == str:
            res += x.upper()
    for x in kwargs:
        if type(kwargs[x]) == str:
            res += kwargs[x].upper()
    return res
a = fu(1,2, 'abc', a = 3, b = 'def')
print(list(a))