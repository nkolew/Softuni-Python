import unittest

from project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.v = Vehicle(10.5, 3.2)

    def test_vehicle_init(self):
        vehicle = Vehicle(10.5, 3.2)
        self.assertEqual(
            (10.5, 3.2),
            (vehicle.fuel, vehicle.horse_power))

        self.assertEqual(
            (10.5, 1.25, 1.25),
            (vehicle.capacity, vehicle.fuel_consumption, vehicle.DEFAULT_FUEL_CONSUMPTION))

    def test_vehicle_drive_successful_when_enough_fuel(self):
        self.v.drive(5)
        self.assertEqual(4.25, self.v.fuel)

    def test_vehicle_drive_raises_when_not_enough_fuel(self):
        with self.assertRaises(Exception) as ctx:
            msg = "Not enough fuel"
            self.v.drive(10)
            self.assertEqual(10.5, self.v.fuel)
            self.assertEqual(msg, str(ctx.exception))

    def test_refuel_successful_when_valid_fuel(self):
        self.v.drive(2)
        self.v.refuel(1)
        self.assertEqual(9.0, self.v.fuel)

    def test_refuel_raises_when_too_much_fuel(self):
        self.v.drive(2)
        with self.assertRaises(Exception) as ctx:
            msg = "Too much fuel"
            self.v.refuel(10)
            self.assertEqual(msg, str(ctx.exception))
        self.assertEqual(8.0, self.v.fuel)

    def test_vehicle_string_representation(self):
        msg = "The vehicle has 3.2 horse power with 10.5 fuel left and 1.25 fuel consumption"
        self.assertEqual(msg, str(self.v))


if __name__ == "__main__":
    unittest.main()
