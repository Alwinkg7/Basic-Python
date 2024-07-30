class vehicle:
    def vehicle_info(self):
        print("Vehicle Info")
class fourwheeler_vehicle(vehicle):
    def fourwheeler_vehicle_info(self):
        print('fourwheeler vehicle info: Kia')
class threewheeler_vehicle(vehicle):
    def threewheeler_vehicle_info(self):
        print('three wheeler vehicle info: Autorickshaw')
class twowheeler_vehicle(vehicle):
    def twowheeler_vehicle_info(self):
        print('two wheeler vehicle info: Activa 125')

obj = fourwheeler_vehicle()
obj.fourwheeler_vehicle_info()
obj.vehicle_info()

obj1 = threewheeler_vehicle()
obj1.threewheeler_vehicle_info()
obj1.vehicle_info()

obj2 = twowheeler_vehicle()
obj2.twowheeler_vehicle_info()
obj2.vehicle_info()