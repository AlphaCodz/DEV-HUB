class Vehicle(object):  # no instance of this class should be created

    def __init__(self, typ, make, model, color, year, miles):
        self.typ = typ
        self.make = make
        self.model = model
        self.color = color.lower()
        self.year = year
        self.miles = miles

    def vehicle_print(self):
            print('Vehicle Type: ' + str(self.typ))
            print('Make: ' + str(self.make))
            print('Model: ' + str(self.model))
            print('Color: ' + str(self.color))
            print('Year: ' + str(self.year))
            print('Miles driven: ' + str(self.miles))


class GasVehicle(Vehicle):

    def __init__(self, fuel_tank, *args):
        self.fuel_tank = fuel_tank
        Vehicle.__init__(self, *args)

    def vehicle_print(self):
        Vehicle.vehicle_print(self)
        print('Fuel capacity (gallons): ' + str(self.fuel_tank))


class ElectricVehicle(Vehicle):

    def __init__(self, energy_storage, *args):
        self.energy_storage = energy_storage
        Vehicle.__init__(self, *args)

    def vehicle_print(self):
        Vehicle.vehicle_print(self)
        print('Energy Storage (Kwh): ' + str(self.energy_storage))


class HeavyVehicle(GasVehicle):  # no instance of this class should be created

    def __init__(self, max_weight, wheels, length, *args):
        self.max_weight = max_weight
        self.wheels = wheels
        self.length = length
        GasVehicle.__init__(self, *args)

    def vehicle_print(self):
        GasVehicle.vehicle_print(self)
        print('Maximum load (tons): ' + str(self.max_weight))
        print('Wheels: ' + str(self.wheels))
        print('Length (m): ' + str(self.length))


class ConstructionTruck(HeavyVehicle):

    def __init__(self, cargo, *args):
        self.cargo = cargo
        HeavyVehicle.__init__(self, *args)

    def vehicle_print(self):
        HeavyVehicle.vehicle_print(self)
        print('Cargo: ' + str(self.cargo))


class Bus(HeavyVehicle):

    def __init__(self, seats, * args):
        self.seats = seats
        HeavyVehicle.__init__(self, *args)

    def vehicle_print(self):
        HeavyVehicle.vehicle_print(self)
        print('Number of seats: ' + str(self.seats))


class HighPerformance(GasVehicle):  # no instance of this class should be created

    def __init__(self, hp, top_speed, *args):
        self.hp = hp
        self.top_speed = top_speed
        GasVehicle.__init__(self, *args)

    def vehicle_print(self):
        GasVehicle.vehicle_print(self)
        print('Horse power: ' + str(self.hp))
        print('Top speed: ' + str(self.top_speed))


class SportCar(HighPerformance):

    def __init__(self, gear_box, drive_system, *args):
        self.gearbox = gear_box
        self.drive_system = drive_system
        HighPerformance.__init__(self, *args)

    def vehicle_print(self):
        HighPerformance.vehicle_print(self)
        print('Gear box: ' + self.gearbox)
        print('Drive system: ' + self.drive_system)




bmw = GasVehicle(30, 'SUV', 'BMW', 'X5', 'silver', 2003, 120300)  # regular car
bmw.vehicle_print()
print
tesla = ElectricVehicle(85, 'Sport', 'Tesla', 'Model S', 'red', 2014, 1243)  # electric car
tesla.vehicle_print()
print
lambo = SportCar('manual', 'rear wheel', 650, 160, 23, 'race car', 'Lamborgini', 'Enzo', 'dark silver', 2014, 3500)  # sportscar
lambo.vehicle_print()
print
truck = ConstructionTruck('cement', 4, 12, 21, 190, 'transport', 'Dirt Inc.', 'Dirt Blaster 100', 'blue', 1992, 120030)  # Construction truck
truck.vehicle_print()