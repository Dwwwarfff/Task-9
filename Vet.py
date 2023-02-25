class Veterinarian:
    def __init__(self):
        pass

    def treat_animal(self, animal):
        print(f"Пришло животное, которое ест {animal.get_food()} и живет в {animal.get_location()}")
