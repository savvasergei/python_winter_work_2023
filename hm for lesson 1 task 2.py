x = int(input())
y = int(input())
a = (x+y)
b = (x-y)
c = (x*y)
d = (x/y)
e = (x//y)

if (a>b and a>c and a>d and a>e and b>c and b>d and b>e):
    print(b)
elif (a>b and a>c and a>d and a>e and c>b and c>d and c>e):
    print(c)
elif (a>b and a>c and a>d and a>e and d>b and d>c and d>e):
    print(d)
elif (a>b and a>c and a> d and a>e and e>b and e>c and e>d):
    print(e)
elif (b>a and b>c and b>d and b>e and a>c and a>d and a>e):
    print(a)
elif (b>a and b>c and b>d and b>e and c>a and c>d and c>e):
    print(c)
elif (b>a and b>c and b>d and b>e and d>a and d>c and d>e):
    print(d)
elif (b>a and b>c and b>d and b>e and e>a and e>c and e>d):
    print(e)
elif (c>a and c>b and c>d and c>e and a>b and a>d and a>e):
    print(a)
elif (c>a and c>b and c>d and c>e and b>a and b>d and b>e):
    print(b)
elif (c>a and c>b and c>d and c>e and d>a and d>b and d>e):
    print(d)
elif (c>a and c>b and c>d and c>e and e>a and e>b and e>d):
    print(e)
elif (d>a and d>b and d>c and d>e and a>b and a>c and a>e):
    print(a)
elif (d>a and d>b and d>c and d>e and b>a and b>c and b>e):
    print(b)
elif (d>a and d>b and d>c and d>e and c>a and c>b and c>e):
    print(c)
elif (d>a and d>b and d>c and d>e and e>a and e>b and e>c):
    print(e)
elif (e>a and e>b and e>c and e>d and a>b and a>c and a>d):
    print(a)
elif (e>a and e>b and e>c and e>d and b>a and b>c and b>d):
    print(b)
elif (e>a and e>b and e>c and e>d and c>a and c>b and c>d):
    print(c)
elif (e>a and e>b and e>c and e>d and d>a and d>b and d>c):
    print(d)
else:
    print("two equal numbers")