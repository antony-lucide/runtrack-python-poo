class Rectangle:

    def __init__(self):
        self.__longueur = 5
        self.__largeur = 10
        
    def retour(self):
        return(self.__largeur)
    
    def retour2(self):
        return(self.__longueur)
    
    def modification(self,largeur):
        self.__largeur = largeur
    
    def modification2(self,longueur):
        self.__longueur = longueur

instance = Rectangle()

print(instance.retour())
