# Импорт необходимых классов
from prototype import Engine, Car


def main():
    # Создание исходного объекта
    original_car = Car("Toyota", "Corolla", Engine(132, "Бензин"))

    # Клонирование объекта
    cloned_car = original_car.clone()

    # Изменение данных в клонированном объекте 
    cloned_car.make = "Honda"
    cloned_car.model = "Civic"
    cloned_car.engine.horsepower = 158
    cloned_car.engine.fuel_type = "Дизель"

    # Вывод результатов
    print(original_car)
    print(cloned_car)

if __name__ == "__main__":
    main()