class Drone(Car, FlyingMachine):
    def __init__(self, make, model, year, altitude):
        super().__init__(make, model, year)
        self.altitude = altitude

    def increase_altitude(self, increase_by):
        self.altitude += increase_by
        print(f"Altitude increased by {increase_by}. Current Altitude: {self.altitude}")
