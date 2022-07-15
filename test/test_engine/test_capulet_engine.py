import unittest
from engine.capulet_engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        engine = CapuletEngine(
            last_service_mileage=10000, current_mileage=60000)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        engine = CapuletEngine(
            last_service_mileage=10000, current_mileage=10000)
        self.assertFalse(engine.engine_should_be_serviced())

    def test_engine_should_be_serviced(self):
        engine = CapuletEngine(
            last_service_mileage=10000, current_mileage=80000)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        engine = CapuletEngine(
            last_service_mileage=10000, current_mileage=30000)
        self.assertFalse(engine.engine_should_be_serviced())



if __name__ == '__main__':
    unittest.main()
