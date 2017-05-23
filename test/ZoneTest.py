import unittest

from MarsRover.Zone import Zone


class ZoneTest(unittest.TestCase):
    def test_zone_knows_coordinate_is_in_bounds(self):
        test_zone = Zone((2, 2))
        self.assertTrue(test_zone.is_coordinate_in_safe_zone((1, 1)))

    def test_zone_knows_coordinate_is_out_of_bounds(self):
        test_zone = Zone((2, 2))
        self.assertFalse(test_zone.is_coordinate_in_safe_zone((3, 1)))
        self.assertFalse(test_zone.is_coordinate_in_safe_zone((1, 3)))
        self.assertFalse(test_zone.is_coordinate_in_safe_zone((3, 3)))
        self.assertFalse(test_zone.is_coordinate_in_safe_zone((-1, 1)))
        self.assertFalse(test_zone.is_coordinate_in_safe_zone((1, -1)))


if __name__ == '__main__':
    unittest.main()
