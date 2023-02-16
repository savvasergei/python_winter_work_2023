x = list(map(int, input().split()))
res1 = [i for i,j in enumerate(x) if j == min(x)]
res2 = [i for i,j in enumerate(x) if j == max(x)]
print(res1)
print(res2)
# a = []
# b = []
# for i,j in enumerate(x):
#     if j == min(x):
#         a.append(i)
#     if j == max(x):
#         b.append(i)
# print(a)
# print(b)