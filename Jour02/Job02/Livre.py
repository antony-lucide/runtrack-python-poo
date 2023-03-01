class Livre:

    def __init__(self):
        self.__titre = "SCREAMS"
        self.__auteur = "Kevin Williamson"
        self.__nombre = 5

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

instance = Livre()

instance.changer_nombre(5)