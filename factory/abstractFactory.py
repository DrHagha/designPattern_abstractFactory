from __future__ import annotations
from abc import ABC, abstractmethod

from product.A.abstractProductA import AbstractProductA
from product.B.abstractProductB import AbstractProductB

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass
    
    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass