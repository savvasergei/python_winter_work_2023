import re
a = input()
res = filter(lambda x: re.findall(r'[24680]', x), a)
print(*res)