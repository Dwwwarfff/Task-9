from Animal import Animal

class Horse(Animal):
    def __init__(self, food, location, is_pony=False):
        super().__init__(food, location)
        self._is_pony = is_pony

    def is_pony(self):
        return self._is_pony

    def set_is_pony(self, is_pony):
        self._is_pony = is_pony

    def make_noise(self):
        print("Лошадь ржёт")

    def eat(self):
        print(f"Лошадь жуёт {self.get_food()}")

    def sleep(self):
        print("Лошадь спит")
