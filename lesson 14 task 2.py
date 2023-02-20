a = []
def sum_digits(x):
    if (x == 0):
        return a
    dig = x % 10
    a.append(dig)
    sum_digits(x // 10)
n = int(input("Введите число: "))
sum_digits(n)
print(sum(a))