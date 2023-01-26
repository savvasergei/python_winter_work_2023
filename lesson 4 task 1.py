a, b, c = input().split()
abc = {}
for i in a:
    if i not in abc:
        abc[i]=0
    abc[i]+=1
for j in b:
    if j not in abc:
        abc[j]=0
    abc[j]+=1
for n in c:
    if n not in abc:
        abc[n]=0
    abc[n]+=1
if b=='+':
    print(int(a)+int(c))
elif b=='-':
    print(int(a)-int(c))
elif b=='*':
    print(int(a)*int(c))
elif b=='/':
    print(int(a)//int(c))
