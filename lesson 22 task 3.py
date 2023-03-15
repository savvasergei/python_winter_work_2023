import keyword
a = keyword.kwlist
res = []
for i in a:
    if i not in res:
        res.append('kw')
print(res)
