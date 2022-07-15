from array import array
from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_state : array) -> None:
        self.tire_state = tire_state
    
    def tire_should_be_serviced(self):
        if sum(self.tire_state) >= 3:
            return True
        else:
            return False
        