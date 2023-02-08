f = open('../../AppData/Roaming/JetBrains/PyCharmCE2022.3/scratches/test2.txt', 'r', encoding='utf-8')
l = f.read()
d = {}
for el in l:
    if d.get(el, None):
        d[el] += 1
    else:
        d[el] = 1
x = sorted(d.items(), key=lambda x:x[1], reverse = True)
print(sorted(x, key= lambda y: (-y[1], y[0])))
f.close()