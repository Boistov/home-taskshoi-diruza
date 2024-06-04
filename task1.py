class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

car = Car(make="Toyota", model="Camry", year=2019)
car1 = Car(make="Hyunday", model="Sonat", year=2018)

print(car.make, car.model, car.year)
print(car1.make, car1.model, car1.year)
