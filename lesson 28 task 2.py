line_1 = list(input())
line_2 = list(input())
counter = 0
for i in range(len(line_1)):
    if line_1[i] != line_2[i]:
        counter += 1
print(counter)