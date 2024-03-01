class NumbersList(list):
    def __init__(self, *args):
        super().__init__()
        for arg in args:
            if isinstance(arg, (int, float)):
                self.append(arg)

    def append(self, value):
        if isinstance(value, (int, float)):
            super().append(value)
        else:
            raise ValueError("Only numeric values (int and float) are allowed.")

    def extend(self, values):
        for value in values:
            self.append(value)

    def get_sum(self):
        return sum(self)

    def get_average(self):
        if len(self) == 0:
            return 0
        return sum(self) / len(self)


num_list = NumbersList(1, 2, 3, 4, 5.5)
print("Suma:", num_list.get_sum())
print("Media:", num_list.get_average())

try:
    num_list.append("abc")
except ValueError as e:
    print(f"Error: {e}")
