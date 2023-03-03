import math

class Forme:
    def __init__(self) -> None:
        pass

    def air(self):
        return 0
    
class Rectangle(Forme): 

    def __init__(self,largeur,hauteur) -> None:
        self.largeur = largeur
        self.hauteur  = hauteur
        Forme.__init__(self)

    def air(self):
        self.aire =  self.largeur * self.hauteur
        return(self.aire)

class Cercle(Forme):

    def __init__(self,radius):
        Forme. __init__(self)
        self.radius = radius
        
    
    def air(self):
        return  self.radius**2*(math.pi)



instance = Rectangle(3,4)
instance2 = Cercle(30)

print(instance.air())
print(instance2.air())