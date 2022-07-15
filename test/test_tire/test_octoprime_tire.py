import unittest
from tire.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_state = [1, 1, 1, 0]
        tire = OctoprimeTire(tire_state)
        self.assertTrue(tire)

    def test_tire_should_not_be_serviced(self):
        tire_state = [0, 0, 0, 0]
        tire = OctoprimeTire(tire_state)
        self.assertFalse(tire)

    def test_tire_should_be_serviced(self):
        tire_state = [1, 1, 1, 1]
        tire = OctoprimeTire(tire_state)
        self.assertTrue(tire)

    def test_tire_should_not_be_serviced(self):
        tire_state = [1, 0, 1, 0]
        tire = OctoprimeTire(tire_state)
        self.assertFalse(tire)


if __name__ == '__main__':
    unittest.main()
