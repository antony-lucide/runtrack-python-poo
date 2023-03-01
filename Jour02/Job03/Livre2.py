class Livre:

    def __init__(self):
        self.__titre = "SCREAMS"
        self.__auteur = "Kevin Williamson"
        self.__nombre = 5
        self.__disponible = True

    def retour_titre(self):
        return(self.__titre)
    
    def retour_auteur(self):
        return(self.__auteur)
    
    def retour_nombre(self):
        return(self.__nombre)

    def changer_titre(self,titre):
        self.__titre = titre
    
    def changer_auteur(self,auteur):
        self.__auteur = auteur
    
    def changer_nombre(self,nombre):
        if type(nombre) is int and nombre > 0:
            self.__nombre = nombre
        else: 
            print("erreur")
    
    def vérification(self):
        if self.__disponible == True:
            return(True)
        else:
            return(False)
 
    def emprunter(self):
        if self.vérification():
            self.__disponible = False
        else:
            print("erreur")


    def Rendre(self,livre):
        if self.vérification():
            print("erreur")
        else:
            self.__disponible = True
            

instance = Livre()

instance.changer_nombre(5)
instance.emprunter()
instance.emprunter()