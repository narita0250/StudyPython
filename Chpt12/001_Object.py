class Orange:
    def __init__(self, w, c):
        # 型チェック
        if not isinstance(w, (int, float)):
            print("Invalid weight. Set to (0, -)")
            w = 0
            c = '-'
        self.weight = w
        self.color = c
        print("Created!")

    def show_info(self):
        print(f"Weight = {self.weight}, Color = {self.color}")

or1 = Orange(10, "dark")
or1.show_info()

or2 = Orange("20", "Yellow")
or2.show_info()
