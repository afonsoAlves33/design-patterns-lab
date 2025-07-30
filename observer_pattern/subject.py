from observer_pattern.observer_interface import IObserver
from observer_pattern.subject_interface import ISubject


class ShoppingCartHandler(ISubject):
    """
    A concrete subject example, responsible for containing business logic to
    change observed object/variable state and notifying its observers
    """
    def __init__(self):
        self._items = []
        self.__observers: list[IObserver] = []
        
        self.__out_of_stock_items = ["mouse", "keyboard"]
        pass
    
    
    def attach(self, observer) -> None:
        print("(Subject) ShoppingCartHandler: an observer was attached")
        self.__observers.append(observer)
        
    def detach(self, observer) -> None:
        print("(Subject) ShoppingCartHandler: an observer was detached")
        self.__observers.remove(observer)
        
        
    def notify(self) -> None:
        print("(Subject) ShoppingCartHandler: notifying all observers")
        for observer in self.__observers:
            observer.update(self)
            
    def add_item(self, item) -> None:
        if  item not in self.__out_of_stock_items:
            self._items.append(item)
            self.notify()
            
    def remove_item(self, item) -> None:
        if  item in self._items:
            self._items.remove(item)
            self.notify()
        
        
        
    
    
    
    
    
        
        

