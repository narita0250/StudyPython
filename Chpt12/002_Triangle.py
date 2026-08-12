from math import sqrt

class Triangle:
    def __init__(self, a, b, c):
        print("Created!")
        self.a = a
        self.b = b
        self.c = c

    def show_info(self):
        print(f"a = {self.a}, b = {self.b}, c = {self.c}")

    def area(self):
        s = (self.a + self.b + self.c) / 2
        S = sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        print(f"Area = {S}")

t1 = Triangle(3,4,5)
t1.show_info()
t1.area()