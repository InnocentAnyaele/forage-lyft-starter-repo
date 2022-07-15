import unittest
from engine.capulet_engine import CapuletEngine
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestCapuletEngine:
    def test_engine_should_be_serviced(self):
        engine = CapuletEngine(last_service_mileage=10000, current_mileage= 60000)
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
        
class TestSternmanEngine:
    def test_engine_should_be_serviced(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine())
        
    def test_engine_should_not_be_serviced(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine())


class TestWilloughbyEngine:
    def test_engine_should_be_serviced(self):
        engine = WilloughbyEngine(
            last_service_mileage=10000, current_mileage=60000)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        engine = WilloughbyEngine(
            last_service_mileage=10000, current_mileage=10000)
        self.assertFalse(engine.engine_should_be_serviced())

    def test_engine_should_be_serviced(self):
        engine = WilloughbyEngine(
            last_service_mileage=10000, current_mileage=80000)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        engine = WilloughbyEngine(
            last_service_mileage=10000, current_mileage=30000)
        self.assertFalse(engine.engine_should_be_serviced())


if __name__ == '__main__':
    unittest.main()