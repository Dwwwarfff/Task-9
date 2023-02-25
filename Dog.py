from Animal import Animal


class Dog(Animal):
    def __init__(self, food, location, breed):
        super().__init__(food, location)
        self._breed = breed

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        self._breed = breed

    def make_noise(self):
        print("Собака лает")

    def eat(self):
        print(f"Собака чавкает {self.get_food()}")

    def sleep(self):
        print("Собака дрыхнет")