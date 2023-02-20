def triangle(n):
    print('*' * n)
    if n >= 1:
        triangle(n - 1)
    print('*' * n)
print(triangle(int(input())))