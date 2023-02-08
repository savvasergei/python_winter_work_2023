a = {1:'G', 2:'C', 3:'T', 4:'A'}
b = {1:'C', 2:'G', 3:'A', 4:'T'}
res = []
res2 = []
n = input()
for i in n:
    if i in a.values():
        res.append(i)
    else:
        print('wrong character')
for j in res:
    if j == a[1]:
        res2.append(b[1])
    elif j == a[2]:
        res2.append(b[2])
    elif j == a[3]:
        res2.append(b[3])
    elif j == a[4]:
        res2.append(b[4])
print(''.join(res2))
