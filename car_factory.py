from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from datetime import datetime


class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(last_service_date, last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date))
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(last_service_date, current_mileage, last_service_mileage), SpindlerBattery(last_service_date, current_date))
    
    def create_palindrome(self, current_date, last_service_date, warning_light_is_on):
        return Car(SternmanEngine(last_service_date, warning_light_is_on), SpindlerBattery(last_service_date, current_date))
    
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(last_service_date, current_mileage, last_service_mileage), NubbinBattery(last_service_date. current_date))
    
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(last_service_date, last_service_mileage, current_mileage), NubbinBattery(last_service_date. current_date))