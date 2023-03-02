class Forme:

    def air(self,largeur,hauteur):
        return 0
    
class Rectangle(Forme): 

    def __init__(self,largeur,hauteur) -> None:
        self.largeur = largeur
        self.hauteur  = hauteur

    def air(self,largeur,hauteur):
        self.aire =  self.largeur * self.hauteur
        return(self.aire)

class Cercle(Forme):

    def __init__(self,radius,largeur,hauteur):
        self.radius = radius
        self.largeur = largeur
        self.hauteur = hauteur
    
    def air(self, radius,largeur, hauteur):
        return  radius*(largeur*hauteur)



instance = Rectangle(3,4)
instance2 = Cercle(30,50,90)

print(instance.air(60,80))
print(instance2.air(30,40,90,30))