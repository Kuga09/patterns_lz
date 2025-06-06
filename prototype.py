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