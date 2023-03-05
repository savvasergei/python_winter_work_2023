class Person:
    def __init__(self, last, first, middle):
        self.last = last
        self.first = first
        self.middle = middle
    def info(self):
        return self.last[::-1], self.first[::-1], self.middle[::-1]
p = Person('ivanov','oleg','vasilych')
print(''.join(p.info()))
