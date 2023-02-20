a = []
def len_digits(x):
    if (x == 0):
        return a
    dig = x % 10
    a.append(dig)
    len_digits(x // 10)
n = int(input("Введите число: "))
len_digits(n)
print(len(a))