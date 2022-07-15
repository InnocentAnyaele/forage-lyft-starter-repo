from abc import ABC, abstractclassmethod

class Tire(ABC):
    @abstractclassmethod
    def needs_service(self):
        pass