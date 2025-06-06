# Импорт необходимых библиотек
import copy


class Engine:
    def __init__(self,horsepower,fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type

class Car:
    def __init__(self,make,model,engine):
        self.make = make
        self.model = model
        self.engine = engine

    # Возвращает полную копию этого объекта
    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"{self.make} {self.model}, мощность {self.engine.horsepower} л.с., мотор {self.engine.fuel_type}"

# Создание исходного объекта
original_car = Car("Toyota","Corolla",Engine(132,"Бензин"))

# Клонирование объекта
cloned_car = original_car.clone()

# Изменение данных в клонированном объекте 
cloned_car.make = "Honda"
cloned_car.model = "Civic"
cloned_car.engine.horsepower = 158
cloned_car.engine.fuel_type = "Дизель"

print(original_car)
print(cloned_car)