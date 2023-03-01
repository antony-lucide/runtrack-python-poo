class Ville:

    def __init__(self,nom,nombre):
       self.__nom = nom
       self.__nombre = nombre

    def Accesseur_nom(self):
        return(self.__nom)
    
    def Accesseur_nombre(self):
        return(self.__nombre)
    
    def Mutateur_nom(self,nom):
        self.__nom = nom

    def Mutateur_nombre(self,nombre):
        self.__nombre = nombre
    

inst = Ville("Marseille",861635)
objet = Ville("Paris",1000000)
print(inst.Accesseur_nombre())
print(objet.Accesseur_nombre())

class Personne:

    def __init__(self,nom,age,ville):
        self.__name = nom
        self.__age = age
        self.__ville = ville

    def AjouterPopulation(self,ville):
       ville.Mutateur_nombre(ville.Accesseur_nombre()+1)


    

instance = Personne("John",45,Ville)
instance.AjouterPopulation(objet)
instance = Personne("Myrtille",4,Ville)
instance.AjouterPopulation(objet)
instance2 = Personne("Myrtille",18,Ville)
instance2.AjouterPopulation(inst)
print(objet.Accesseur_nombre())
print(objet.Accesseur_nombre())
print(inst.Accesseur_nombre())



