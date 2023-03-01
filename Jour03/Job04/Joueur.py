class Joueur:

    def __init__(self,nom,numéro,position,nombre_de_buts,passe_décisives,carton_jaune,carton_rouge):
        self.nom = nom 
        self.numéro = numéro
        self.position = position
        self.buts = nombre_de_buts
        self.décisives = passe_décisives
        self.carton_jaune = carton_jaune
        self.carton_rouge = carton_rouge
    
    def marquerUnBut(self):
        return(self.buts + 1)

    def effectuer_Une_Passe_Decisive(self):
        return(self.décisives + 1)
    
    def recevoir_un_Carton_Rouge(self):
        return(self.carton_rouge + 1)
    
    def recevoir_un_Carton_Jaune(self):
        return(self.carton_jaune + 1)

    def afficher_stastistique(self):
        print(self.nom)
        print(self.numéro)
        print(self.buts)
        print(self.position)
        print(self.décisives)
        print(self.carton_jaune)
        print(self.carton_rouge)

class Equipe:
    def __init__(self,equipe):
        self.equipe = equipe
        self.liste_de_joueurs = []
    
    def ajouterJoueurs(self,equipe):
        self.liste_de_joueurs.append(equipe)
    
    def afficherJoueurs(self):
        for i in self.liste_de_joueurs:
            self.liste_de_joueurs[i].afficher_stastistique()
        
    def mettreAJourStastistiqueJoueur(self,nom,numéro,position,nombre_de_buts,passe_décisives,carton_jaune,carton_rouge):
        self.liste_de_joueurs[self.liste_de_joueurs(nom)].afficher_stastistique(nom,numéro,position,nombre_de_buts,passe_décisives,carton_jaune,carton_rouge)

instance = Joueur('John',50,'centre',80,30,3,4)
instance2 = Equipe('Team Betise')
print(instance2.ajouterJoueurs(instance))
print(instance.afficher_stastistique())


    
