from abc import ABC, abstractmethod


class Engine(ABC):
    """
    abstract engine
    """
    @abstractmethod
    def needs_service(self)-> bool:
        pass