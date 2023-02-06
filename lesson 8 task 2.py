a = list(map(int, input().split(',')))
b = list(map(int, input().split(',')))
c = list(map(int, input().split(',')))
s = list([sorted(a)]+[sorted(b)]+[sorted(c)])
print(sorted(s, key = len))






