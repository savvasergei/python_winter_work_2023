a, b = input().split()
abc = {}
xyz = {}
for i in a:
    if i not in abc:
        abc[i]=0
    abc[i]+=1
for j in b:
    if j not in xyz:
        xyz[j]=0
    xyz[j]+=1
if abc==xyz:
    print('true')
else:
    print('false')



