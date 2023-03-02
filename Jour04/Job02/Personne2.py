class Personne:

    def __init__(self):
        self.age = 14

    def afficherAge(self):
        print(self.age)
    
    def bonjour(self):
        print('hello')
    
    def modifierAge(self,entier):
        self.age  = entier
    
class Eleve(Personne):

    def allerEnCours(self):
        print('je vais en cours')
    
    def afficherAge(self):
        print('jai',self.age,'ans')
    
class Professeur(Personne):

    def MatiereEnseignée(self,matière):
        self.__Matière_Enseignée = matière
        self.enseigner = print('Le Cours va commencer')
    

instance = Personne()
instance2 = Eleve()

instance.afficherAge()
    