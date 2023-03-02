class Rectangle:

    def __init__(self,longueur,largeur):
        self.longueur = longueur
        self.largeur = largeur
    
    def périmètre(self,longueur,largeur):
        self.perim = longueur + largeur + longueur
    
    def surface(self,longueur,largeur):
        self.surface_perim = longueur * largeur

    def accesseur_longueur(self):
        return(self.longueur)

    def accesseur_largeur(self):
        return(self.largeur)
    
    def accesseur_périmètre(self):
        return(self.perim)

    def accesseur_surface(self):
        return(self.surface_perim)
    

    def mutateur_longueur(self,longueur):
        self.longueur = longueur

    def mutateur_largeur(self,largeur):
        self.largeur = largeur
    
    def mutateur_périmètre(self,perim):
        self.perim = perim

    def mutateur_surface(self,surface):
        self.surface_perim = surface
    
class Parallélépipède(Rectangle):

    def __init__(self,hauteur):
        super().__init__()
        self.hauteur = hauteur
    
    def Volume(self,longueur,largeur,hauteur):
        self.volume = longueur * largeur * hauteur


instance = Rectangle(30,40)
instance2 = Parallélépipède(20)

print(instance.accesseur_largeur())

