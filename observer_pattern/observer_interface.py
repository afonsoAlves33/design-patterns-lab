from abc import ABC, abstractmethod


class IObserver(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """
    
    @abstractmethod
    def update(self):
        """
        Receive update from subject.
        """
        pass
    
