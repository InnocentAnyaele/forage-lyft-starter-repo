from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire
from datetime import datetime


class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_state):
        engine = CapuletEngine(last_service_date, last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(tire_state)
        return Car(engine, battery, tire)
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_state):
        engine = WilloughbyEngine(
            last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = OctoprimeTire(tire_state)
        return Car(engine, battery, tire)
    
    def create_palindrome(self, current_date, last_service_date, warning_light_is_on, tire_state):
        engine = SternmanEngine(last_service_date, warning_light_is_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(tire_state)
        return Car(engine, battery, tire)
    
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_state):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date. current_date)
        tire = OctoprimeTire(tire_state)
        return Car(engine, battery, tire)
    
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_state):
        engine = CapuletEngine(last_service_date, last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date. current_date)
        tire = CarriganTire(tire_state)
        return Car(engine, battery, tire)
