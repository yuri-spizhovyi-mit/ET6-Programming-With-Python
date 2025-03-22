class Car:
    """Class representing a car"""
    
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def get_make(self):
        return self.make

    def get_model(self):
        """Return car's model"""
        return self.model

    def get_year(self):
        return self.year

    def get_mileage(self):
        return self.mileage

    def set_mileage(self, km):
        self.mileage = km

    def drive(self, km):
        self.mileage += km

    def age(self, current_year):
        return current_year - self.year

    def __str__(self):
        return f"Car: {self.make} {self.model} ({self.year}), Mileage: {self.mileage} km"


# first_car = Car("Toyota", "Corolla", 1999, 204000)
# print(first_car.get_make())
# first_car.set_mileage(220345)
# print(first_car)
# print(first_car.age(2025))
# first_car.drive(1000)
# print(f"After driving 1000 km: {first_car}")


class ElectricCar(Car):
    def __init__(self, make, model, year, mileage, battery_capacity, charge_level=100):
        super().__init__(make, model, year, mileage)
        self.battery_capacity = battery_capacity
        self.charge_level = charge_level

    def get_battery_info(self):
        return f"Battery: {self.battery_capacity} kWh, Charge Level: {self.charge_level}%"
    
    def charge(self):
        self.charge_level = 100

    def drive_electric(self, km):
        self.charge_level -= int(km/10)
        if self.charge_level < 0:
            self.charge_level = 0
        self.mileage += km

    def __str__(self):
        return (f"Electric Car: {self.make} {self.model} ({self.year}), "
                f"Mileage: {self.mileage} km, "
                f"Battery: {self.battery_capacity} kWh, "
                f"Charge Level: {self.charge_level}%")


my_electric = ElectricCar('Tesla', 'Model 3', 2021, 30000, 75)
print(my_electric)

my_electric.drive_electric(50)
print(my_electric.get_battery_info())

my_electric.charge()
print(my_electric)
