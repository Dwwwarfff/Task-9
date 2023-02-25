class Animal:
    def __init__(self, food, location):
        self._food = food
        self._location = location

    def get_food(self):
        return self._food

    def set_food(self, food):
        self._food = food

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location

    def make_noise(self):
        print("Животное гудит")

    def eat(self):
        print("Животное жрёт")

    def sleep(self):
        print("Животное дышит, храпит и спит")