a = []
res = 0
for _ in range(int(input())):
    n = int(input())
    res += sum(el > n for el in a)
    a.append(n)

print(res)
