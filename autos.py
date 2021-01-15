
class Auto(object):
    def __init__(self, make, model, year, color, num_wheels):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.num_wheels = num_wheels

    def drive(self):
        print(f'Driving {self.make} {self.model} {self.add_str()} ')

    def add_str(self):
        pass


class Truck(Auto):

    def __init__(self, make, model, year, color, num_wheels, bed_size):
        super().__init__(make, model, year, color, num_wheels)
        self.bed_size = bed_size

    def add_str(self):
        return f'Truck with {self.bed_size} bed size'


class SUV(Auto):
    def __init__(self, make, model, year, color, num_wheels, num_passengers):
        super().__init__(make, model, year, color, num_wheels)
        self.num_passengers = num_passengers

    def add_str(self):
        return f'SUV capable of carrying upto {self.num_passengers} passengers'


if __name__ == '__main__':
    suv = SUV('Toyota', 'LandCruiser', '2019', 'Blue', 4, 6)
    truck = Truck('Ford', 'F-150', '2019', 'Blue', 4, 'Large')

    suv.drive()

    truck.drive()
