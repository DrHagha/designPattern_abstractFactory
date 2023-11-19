from factory.abstractFactory import AbstractFactory

from product.A.abstractProductA import AbstractProductA
from product.A.concreateProductA1 import ConcreteProductA1
from product.B.abstractProductB import AbstractProductB
from product.B.concreateProductB1 import ConcreteProductB1

class ConcreateFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()
    
    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()