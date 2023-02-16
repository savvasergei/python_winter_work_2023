def fun(n):
    for x in range(1, n):
        if x%2 == 0:
            yield x
        else:
            yield -x
g = fun(int(input()))
for i in g:
    print(str(i), end = ' ')