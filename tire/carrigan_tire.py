from array import array
from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_state: array) -> None:
        self.tire_state = tire_state

    def tire_should_be_serviced(self):
        for tire in self.tire_state:
            if tire >= 0.9:
                return True
        return False

