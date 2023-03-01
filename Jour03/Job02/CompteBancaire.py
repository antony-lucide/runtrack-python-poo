class CompteBancaire:

    def __init__(self,numéro,nom,prénom,solde):
       self.__numéro = numéro
       self.__nom = nom
       self.__prénom = prénom
       self.__solde = solde
       self.__découvert = False
    
    def afficher(self):
        print(self.__numéro,self.__nom,self._prénom,self.__solde)
    
    def afficherSolde(self):
        print(self.__solde)
    
    def versement(self,montant):
        self.__solde + montant
    
    def retrait(self,entier,montant):
        if self.__solde > montant :
             self.__solde - entier
        else:
            print('erreur')
    
    def agios(self,montant,entier):
        if self.solde > 0:
            self.solde - entier
    
    def virement(self,ref,compte,montant):
        if self.__solde > montant:
            self.__solde += compte
        elif self.__solde < montant:
            print('erreur')

instance = CompteBancaire(30450,'John','Duplot',70)
instance2 = CompteBancaire(34593,'josh','duplot',-0)
instance.virement('josh',8,9)
instance.afficherSolde()