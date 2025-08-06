from abc import ABC, abstractmethod

from product_interface import IProduct


class ICreator(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """
    
    @abstractmethod
    def factory_method(self) -> IProduct:
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass
            
    @abstractmethod
    def operation(self):
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """
        
        class_that_does_something = self.factory_method()
        
        return f"(Creator) [doing my operation]:  I rely on factory_method, this is an example of me using it for something: \n{class_that_does_something.operation()}"
         