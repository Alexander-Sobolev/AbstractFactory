"""
Предоставление интерфейса для создания семейств связанных или зависимых
объектов без указания их конкретных классов.
"""

import abc


class AbstractFactory(metaclass=abc.ABCMeta):
    """
    Объявление интерфейса для методов, которые создают объекты.
    """

    @abc.abstractmethod
    def create_product_a(self):
        pass

    @abc.abstractmethod
    def create_product_b(self):
        pass


class ConcreteFactory1(AbstractFactory):
    """
    Внедрить операции по созданию конкретных объектов фабрики.
    """

    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    Внедрить операции по созданию конкретных объектов продукта.
    """

    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()


class AbstractProductA(metaclass=abc.ABCMeta):
    """
    Объявить интерфейс класса.
    """

    @abc.abstractmethod
    def interface_a(self):
        pass


class ConcreteProductA1(AbstractProductA):
    """
    Определить объект продукта, который будет создан соответствующей абстрактной фабрикой.
    Внедрить интерфейс AbstractProduct.
    """

    def interface_a(self):
        pass


class ConcreteProductA2(AbstractProductA):
    """
    Определить объект продукта, который будет создан соответствующей абстрактной фабрикой.
    Внедрить интерфейс AbstractProduct.
    """

    def interface_a(self):
        pass


class AbstractProductB(metaclass=abc.ABCMeta):
    """
    Объявить интерфейс класса.
    """

    @abc.abstractmethod
    def interface_b(self):
        pass


class ConcreteProductB1(AbstractProductB):
    """
    Определить объект продукта, который будет создан соответствующей абстрактной фабрикой.
    Внедрить интерфейс AbstractProduct.
    """

    def interface_b(self):
        pass


class ConcreteProductB2(AbstractProductB):
    """
    Определить объект продукта, который будет создан соответствующей абстрактной фабрикой.
    Внедрить интерфейс AbstractProduct.
    """

    def interface_b(self):
        pass


def main():
    for factory in (ConcreteFactory1(), ConcreteFactory2()):
        product_a = factory.create_product_a()
        product_b = factory.create_product_b()
        product_a.interface_a()
        product_b.interface_b()


if __name__ == "__main__":
    main()