class Cafe:
    def __init__(self, *menu):
        self.menu = list(menu)
    def __getitem__(self, i):
        return self.menu[i]
class Waiter:
    def __init__(self):
        self.work = 0
    def serve(self, menu, *customer):
        for i in customer:
            i.take(menu)
            self.work += 1
class Customer:
    def __init__(self):
        self.order = []
    def take(self, menu):
        self.order.append(menu)
service = Cafe('coffee', 'tea', 'soup', 'main dish', 'side dish')

Bartender = Waiter()
Ivan = Customer()
Alex = Customer()

Bartender.serve(service[2], Ivan)
Bartender.serve(service[3], Alex)

print(Ivan.order)
print(Alex.order)