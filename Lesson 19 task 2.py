class Fib:
    def __init__(self, n):
        self.n = n
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        fib = self.a
        if fib > self.n:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib
fib = Fib(10)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
