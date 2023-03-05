import itertools
for x in itertools.permutations([50, 100, 200, 500, 1000, 5000], 3):
    print(sum(x), '\n')