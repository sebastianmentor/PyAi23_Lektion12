from abc import ABC, abstractmethod
 
class Polygon(ABC):
 
    @abstractmethod
    def no_of_sides(self):
        pass
 
class Triangle(Polygon):
 
    def no_of_sides(self):
        print("I have 3 sides")
 
 
class Pentagon(Polygon):
 
    def no_of_sides(self):
        print("I have 5 sides")
 
 
class Hexagon(Polygon):
 
    def no_of_sides(self):
        print("I have 6 sides")
 
 
class Quadrilateral(Polygon):
 
    def no_of_sides(self):
        print("I have 4 sides")

class Cirkel(Polygon):

    def no_of_sides(self):
        print('Oppss')
 
R = Triangle()
R.no_of_sides()
 
K = Quadrilateral()
K.no_of_sides()
 
R = Pentagon()
R.no_of_sides()
 
K = Hexagon()
K.no_of_sides()

C = Cirkel()
C.no_of_sides()