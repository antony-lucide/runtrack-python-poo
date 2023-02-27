class Personnage:
   #La class Personnage et les méthodes ci-dessous permettent de ce déplacer dans l'axe. 
    def __init__(self,x,y):
        self.position_1 = x
        self.position_2 = y

    def mouvement_haut(self):
        self.position_1 -= 1
    
    def mouvemement_bas(self):
        self.position_1 += 1
    
    def mouvement_droite(self):
        self.position_1 += 1
    
    def mouvement_gauche(self):
        self.position_1 -= 1
    
    def retour(self):
        return(self.mouvement_haut,self.mouvemement_bas,self.mouvement_gauche,self.mouvement_droite)
        

instances = Personnage(5,6)

print(instances.retour())