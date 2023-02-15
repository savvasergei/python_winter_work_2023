a = [[i]*i for i in range(1, 11)]
print(*a)
lst = []
for i in range(1, 11):
    lst.append([i] * i)
print(*lst)

