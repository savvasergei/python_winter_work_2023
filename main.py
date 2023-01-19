x = int(input())
y = int(input())
a = (x+y)
b = (x-y)
c = (x*y)
d = (x/y)
e = (x//y)

if (a>b and a>c and a>d and a>e):
    print(a)
elif (b>a and b>c and b>d and b>e):
    print(b)
elif (c>a and c>b and c>d and c>e):
    print(c)
elif (d>a and d>b and d>c and d>e):
    print(d)
elif (e>a and e>b and e>c and e>d):
    print(e)
else:
    print(0)
