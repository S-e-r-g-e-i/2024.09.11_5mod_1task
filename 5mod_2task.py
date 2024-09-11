# Домашняя работа по уроку "Специальные методы классов."

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def go_to(self, new_floor):
        if self.number_of_floors < new_floor:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)

h1 = House('ЖК Эльбрус', 10) # переопределяем параметры объекта
h2 = House('ЖК Акация', 20) # переопределяем параметры объекта

# __str__
print(h1)
print(str(h2)) # данная запись тоже корректна ??? - работает 

# __len__
print(len(h1))
print(len(h2))