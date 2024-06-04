class ElectricCar:
    def __init__(self, make, model, year, battery_size):
        self.make = make
        self.model = model
        self.year = year
        self.battery_size = battery_size
    
    def display_info(self):
        return self.make, self.model, self.year, self.battery_size

my_car = ElectricCar(make="Tesla", model="Model S", year=2023, battery_size=1000000)
print(my_car.display_info())
