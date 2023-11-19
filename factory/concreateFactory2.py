
from factory.abstractFactory import AbstractFactory
from product.A.abstractProductA import AbstractProductA
from product.A.concreateProductA2 import ConcreteProductA2
from product.B.abstractProductB import AbstractProductB
from product.B.concreateProductB2 import ConcreteProductB2


class ConcreateFactory2(AbstractFactory):
    """
    Each Concrete Factory has a corresponding product variant.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()