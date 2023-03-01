class Personnage:

    def __init__(self,nom):
         self.nom = nom
         self.vie = 100

    def LowHP(self):
         self.vie - 30
    
    def name(self):
         print(self.nom)

class Jeu:
     
     def Choisir_Niveau(self,niveau):
        self.niveau = niveau
        if(self.niveau >= 20):
            self.niveau-= 40
            print('Niveau Insuffisant')
        elif(self.niveau >= 30):
            self.niveau -= 30
            print('Niveau Faible')
        elif(self.niveau <= 40):
            self.niveau -= 20
            print('Niveau random')
        elif(self.niveau <= 50):
            self.niveau -= 10
            print('Niveau Neutre')
        elif(self.niveau >= 60):
            self.niveau -= 5
            print('Difficulté Choisis, Passable')
        elif(self.niveau >= 70):
            self.niveau -= 1
            print('Niveau Difficile')
        else: 
            print('Erreur')
     
     def lancerjeux(self,niveau):
         self.alliés = niveau
         self.ennemi = niveau

instance = Personnage('Josh')
instance2 = Jeu()

instance2.Choisir_Niveau(70)