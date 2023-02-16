x = list(map(int, input()))
def fu():
    res = []
    for i in x:
        if i%2!=0:
            res.append(i)
    yield res
gf = fu()
for x in gf:
    print(x)


