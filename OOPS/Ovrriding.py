class Birds:
    def birds(self):
        print("Birds are in different types")
    def flights(self):
        print("There are birds that can fly and some cannot")

class Sparrow(Birds):
    def flights(self):
        print('Sparrows fly')

class Ostrich(Birds):
    def flights(self):
        print('Ostrich cannot fly')

obj = Birds()
obj.birds()
obj.flights()

obj1 = Sparrow()
obj1.birds()
obj1.flights()

obj2 = Ostrich()
obj2.birds()
obj2.flights()