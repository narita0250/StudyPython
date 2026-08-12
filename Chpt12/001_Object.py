class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")

    def show_info(self):
        print(f"Weight = {self.weight}, Color = {self.color}")

or1 = Orange(10, "dark")
or1.show_info()
