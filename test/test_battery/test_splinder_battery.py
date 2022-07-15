import unittest
from datetime import datetime
from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def battery_should_be_serviced(self):
        current_date = datetime.today()
        last_service_date = current_date.replace(year=current_date.year - 3)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery)

    def battery_should__not_be_serviced(self):
        current_date = datetime.today()
        last_service_date = current_date.replace(year=current_date.year + 8)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery)

    def battery_should_be_serviced(self):
        current_date = datetime.today()
        last_service_date = current_date.replace(year=current_date.year - 4)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery)

    def battery_should__not_be_serviced(self):
        current_date = datetime.today()
        last_service_date = current_date.replace(year=current_date.year - 2)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery)


if __name__ == '__main__':
    unittest.main()
