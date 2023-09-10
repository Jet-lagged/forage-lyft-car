from abc import ABC, abstractmethod

class Battery(ABC):
    """
    abstract battery
    """
    @abstractmethod
    def needs_service(self)-> bool:
        pass