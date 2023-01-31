s = input()
a = set()
b = set()
c = set()
for i in s:
    if i in 'a b c d e f g h i j k l m n o p q r s t u v w x y z':
        a.add(i)
print(' '.join(sorted(a)))
for j in s:
    if j in '1 2 3 4 5 6 7 8 9 0':
        b.add(j)
print(' '.join(sorted(b)))
for z in s:
    if z in ('; , : = + - _  @  $ .'):
        c.add(z)
print(' '.join(c))