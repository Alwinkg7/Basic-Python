#multilevel

class vehicle:
    def vehicle_info(self):
        print("Inside vehicle class")

class car(vehicle):
    def car_info(self):
        print("Inside car class")

class Truck(car):
    def truck_info(self):
        print("Inside truck class")

obj =  Truck()
obj.vehicle_info()
obj.truck_info()
obj.car_info()