w = input()
c = []
v = []
for i in w:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        c.append(i)
    else:
        v.append(i)
if abs(len(c) - len(v)) <=1:
    from itertools import zip_longest
    x = [item for lists in zip_longest(v,c, fillvalue="") for item in lists]
    print(''.join(x))
else:
    print('impossible')


