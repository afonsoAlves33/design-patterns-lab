from observer_pattern.subject_interface import ISubject
from observer_pattern.observer_interface import IObserver
import logging


class ShoppingCartGraphicInterface(IObserver):
    def update(self, subject: ISubject):
        print(f"(Observer) ShoppingCartGraphicInterface: updating frontend, items: {subject._items}")
        
        
class ShoppingCartLogger(IObserver):
    def update(self, subject: ISubject):
        """
        Update may have its own business logic:
        """
        
        if len(subject._items) > 0: 
            print(f"(Observer) ShoppingCartLogger: logging new list: {subject._items}")
            logging.info(f"Items list has been updated: {subject._items}")
        
    
        
    