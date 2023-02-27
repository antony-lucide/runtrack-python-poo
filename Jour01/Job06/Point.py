class Point:
   #La classe POint et les méthodes ci-dessous sont des cordonnées.
   #Permettant de définir des positions dans un axe, entre x et y.
   #Ensuite on définit des valeurs de base et on prints ses valeurs dans l'axe
    def __init__(self,y,x):
        self.cordX = x
        self.codY = y

    
    def AfficherLesPoints(self):
        print(self.cordX,self.codY)

    def AfficherX(self):
        print(self.cordX)
    
    def AfficherY(self):
        print(self.cordY)

    def changerX(self,x):
        self.cordX = x

    def changerY(self,y):
        self.cordY = y

résultat = Point(5,6)

print(résultat.AfficherLesPoints())

