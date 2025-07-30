from abc import ABC, abstractmethod


class IObserver(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """
    
    @abstractmethod
    def update(self):
        """
        Receive update from subject.
        """
        pass
    
