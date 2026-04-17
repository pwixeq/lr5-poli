from abc import ABC, abstractmethod

# базовый класс товаров
class Tovar(ABC):
    def __init__(self, name, id, price, kolvo):
        self.name = name
        self.id = id
        self.price = price
        self.kolvo = kolvo

    @abstractmethod
    def type_of_product(self):
        pass #возвращает тип товара

    def add_kolvo(self, amount):
        if amount <= 0:
            raise ValueError # количество добавляемого товара должно быть положительным числом
        else:
            self.kolvo += amount
            print(f'Товар {self.name} был увеличен на {amount}. Количество составляет {self.kolvo}.')

    def minus_kolvo(self, amount):
        if amount <= 0:
            raise ValueError
        if amount > self.kolvo:
            raise ValueError(f'Недостаточно товара {self.name}. Количество составляет {self.kolvo}.')
        self.kolvo -= amount
        print(f"Товар {self.name} уменьшен на {amount}. Теперь: {self.kolvo}.")

    def total_value(self):
        return self.price * self.kolvo

    def __str__(self): # возвращает удобно читаемое представление объекта
        return (f'[{self.type_of_product()}] {self.name} (ID: {self.id}), '
                f'Цена: {self.price} руб., Количество: {self.kolvo}, '
                f'Общая стоимость: {self.total_value()} руб.')

class Food(Tovar):
    def __init__(self, name, id, price, kolvo, srock):
        super().__init__(name, id, price, kolvo)
        self.srock = srock

    def type_of_product(self):
        return 'Продукты питания'

    def check(self, c_date):
        if c_date > self.srock: # проверка срока годности
            print(f'Товар {self.name} просрочен.')
            return False
        else:
            print(f'Товар {self.name} годен до {self.srock}.')
            return True

class Electronic(Tovar):
    def __init__(self, name, id, price, kolvo, garant):
        super().__init__(name, id, price, kolvo)
        self.garant = garant

    def type_of_product(self):
        return 'Электроника'

    def garant_check(self, months):
        if months <= 0:
            raise ValueError # срок гарантии должен быть положительным
        else:
            self.garant += months
            print(f'Гарантия на товар {self.name} продлена на {self.garant} месяцев. '
                  f'Гарантия общая: {self.garant} месяцев.')


if __name__ == '__main__':
    try:
        banana = Food('Бананы', '628602', 38, 100, '2026-01-31')
        phone = Electronic('Айфон', '345906', 89999, 50, 24)

        print(f'Информация о товарах')
        print(banana)
        print(phone)

        banana.type_of_product()
        phone.type_of_product()
        banana.check('2026-01-26')
        phone.garant_check(20)
        phone.minus_kolvo(2)
        banana.add_kolvo(30)
        banana.minus_kolvo(150)

    except ValueError as e:
        print(f'Ошибка: {e}')