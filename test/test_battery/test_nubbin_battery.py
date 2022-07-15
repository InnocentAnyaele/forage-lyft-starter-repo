import unittest
from datetime import datetime
from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def battery_should_be_serviced(self):
        current_date = datetime.today()
        last_service_date = current_date.replace(year=current_date.year - 3)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery)

    def battery_should__not_be_serviced(self):
        current_date = datetime.today()
        last_service_date = current_date.replace(year=current_date.year + 8)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery)

    def battery_should_be_serviced(self):
        current_date = datetime.today()
        last_service_date = current_date.replace(year=current_date.year - 4)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery)

    def battery_should__not_be_serviced(self):
        current_date = datetime.today()
        last_service_date = current_date.replace(year=current_date.year - 2)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery)


if __name__ == '__main__':
    unittest.main()
