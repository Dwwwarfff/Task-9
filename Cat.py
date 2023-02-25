from Animal import Animal


class Cat(Animal):
    def __init__(self, food, location, color):
        super().__init__(food, location)
        self._color = color

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def make_noise(self):
        print("Кот мяукает")

    def eat(self):
        print(f"Кот ест {self.get_food()}")

    def sleep(self):
        print("Кот отдыхает")
