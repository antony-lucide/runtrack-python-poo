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
    def __init__(self):
        Personne.__init__(self)

    def allerEnCours(self):
        print('je vais en cours')
    
    def afficherAge(self):
        print('jai',self.age,'ans')
    
class Professeur(Personne):

    def __init__(self,matière):
        Personne.__init__(self)
        self.__Matière_enseignée = matière

    def MatiereEnseignée(self,matière):
        self.enseigner = print('Le Cours va commencer')
    

instance = Personne()
instance2 = Eleve()
instance3 = Professeur('Math')

instance.bonjour()
instance2.modifierAge(15)
instance2.afficherAge()
instance2.allerEnCours()

instance3.bonjour()
instance3.MatiereEnseignée('Art')
instance3.modifierAge(56)
instance3.afficherAge()

