a = 133244459
b = str(a)
c = list(b)
counts = [[c.count(item), item] for item in set(c)]
counts.sort()
print(counts)

