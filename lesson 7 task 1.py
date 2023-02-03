import math
s = list(map(int, input().split()))
lcm = math.lcm(*s)
print(lcm)