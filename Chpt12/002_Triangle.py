from math import sqrt

def is_valid(a, b, c):
    # 数でない
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        return False
    # 正でない
    if not all(x > 0 for x in (a, b, c)):
        return False
    # 辺の長さが三角形の成立条件を満たさない
    # a < b + c ⇔ 2a < a + b + c
    if not(2 * max(a, b, c) < (a + b + c)):
        return False
    return True

class Triangle:
    def __init__(self, a, b, c):
        print("Created!")
        if (is_valid(a, b, c) == False):
            print("Invalid value. Set to (0, 0, 0)")
            a = b = c = 0
        self.a = a
        self.b = b
        self.c = c

    def show_info(self):
        print(f"a = {self.a}, b = {self.b}, c = {self.c}")

    def area(self):
        s = (self.a + self.b + self.c) / 2
        S = sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        print(f"Area = {S}")

# ケース1:正常
t1 = Triangle(3,4,5)
t1.show_info()
t1.area()

# ケース2:文字
t2 = Triangle('a', 4, 5)
t2.show_info()
t2.area()

# ケース3:負数
t3 = Triangle(-1, 4, 5)
t3.show_info()
t3.area()

# ケース4:成立条件不成立
t4 = Triangle(9999, 4, 5)
t4.show_info()
t4.area()
