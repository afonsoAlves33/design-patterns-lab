from abc import ABC, abstractmethod
from observer_pattern.observer_interface import IObserver


class ISubject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """
    
    @abstractmethod
    def attach(self, observer: IObserver):
        """
        Attach an observer to the subject.
        """
        pass
    
    @abstractmethod
    def detach(self, observer: IObserver):
        """
        Detach an observer from the subject.
        """
        pass
    
    @abstractmethod
    def notify(self):
        """
        Notify all observers about an event.
        """
        pass
        
    