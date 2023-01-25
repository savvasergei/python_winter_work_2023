lst = []
while a := int(input()):
    lst.append(a)
    if a==0:
        break
print(__import__('statistics').mean(lst))


