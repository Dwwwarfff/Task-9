from Vet import Veterinarian
from Cat import Cat
from Dog import Dog
from Horse import Horse

""" Создать класс Animal и расширяющие его классы Dog, Cat, Horse. Класс Animal содержит переменные food, location и 
методы makeNoise, eat, sleep. Метод makeNoise, например, может выводить на консоль "Такое-то животное спит". Dog, Cat, 
Horse переопределяют методы makeNoise, eat. Добавьте переменные в классы Dog, Cat, Horse, характеризующие только этих 
животных. Создайте класс Ветеринар, в котором определите метод void treatAnimal(Animal animal). Пусть этот метод 
распечатывает food и location пришедшего на прием животного. В методе main создайте массив типа Animal, в который 
запишите животных всех имеющихся у вас типов. В цикле отправляйте их на прием к ветеринару."""

if __name__ == '__main__':
    animals = [Dog('Косточки', 'Конуре', 'Пудель'),
               Horse('Сено', 'Поле', is_pony=True),
               Cat('Вискас', 'Подвалe', 'Рыжий')]

    vet = Veterinarian()

    for animal in animals:
        vet.treat_animal(animal)
