class Voiture:

    def __init__(self,marque,modèle,années,kilométrage):
        self.__marque = marque
        self.__modèle = modèle
        self.__années = années
        self.__kilométrage = kilométrage
        self.__en_marche = False
        self._reservoir = 50

    def attribut_marque(self):
        return(self.__marque)
    
    def attribut_modèle(self):
        return(self.__marque)
    
    def attribut_années(self):
        return(self.__marque)
    
    def attribut_kilométrage(self):
        return(self.__kilométrage)
    
    def attribut_en_marche(self):
        return(self.__en_marche)
    

    def mutateur_marque(self,marque):
        self.__marque = marque

    def mutateur_modèle(self,modèle):
        self.__modèle = modèle
    
    def mutateur_années(self,années):
        self.attribut_années = années
    
    def mutateur_kilométrage(self,kilométrage):
        self._kilométrage = kilométrage
    
    def mutateur_en_marche(self,en_marche):
        self.attribut_en_marche = en_marche
    
    def démarrer(self):
        if self._reservoir >= 5:
            self.__en_marche = True

    def arrêter(self):
        self.__en_marche = False
    
    def __verifier_plein(self):
        return(self._reservoir)
    
instance = Voiture("Volvo","Class G","2002",90)

print(instance.attribut_modèle())