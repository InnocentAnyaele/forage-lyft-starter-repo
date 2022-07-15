import unittest
from engine.sternman_engine import SternmanEngine


class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine())

    def test_engine_should_not_be_serviced(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine())

if __name__ == '__main__':
    unittest.main()
