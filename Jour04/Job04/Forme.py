class Forme:
    def __init__(self,largeur,hauteur):
        self.largeur = largeur
        self.hauteur =  hauteur

    def air(self,largeur,hauteur):
        return 0
    
class Rectangle(Forme): 
    def air(self):
        self.aire =  self.largeur * self.hauteur
        return(self.aire)

instance = Rectangle(3,4)

print(instance.air())