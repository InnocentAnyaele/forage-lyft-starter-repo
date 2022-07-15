# from abc import ABC, abstractmethod
from servicable import Servicable

# class Car(ABC):
#     def __init__(self, last_service_date):
#         self.last_service_date = last_service_date

#     @abstractmethod
#     def needs_service(self):
#         pass


class Car(Servicable):
    def __init___(self, engine, battery):
        self.engine = engine
        self.battery = battery
    
    def needs_service(self):
        if self.engine.engine_should_be_serviced() or self.battery.battery_should_be_serviced():
            return True
        else: 
            return False