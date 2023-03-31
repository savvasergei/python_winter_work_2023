matrix = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
            ]

def rotated(mtrx):
    res = zip(*mtrx[::-1])
    return [list(i) for i in res]
    # return map(list, list_of_tuples)

print(list(rotated(matrix)))