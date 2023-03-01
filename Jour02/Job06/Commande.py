
liste_de_plat = {'nom':'Oignon','prix':4,
                 'nom': 'Salade','prix':7,
                 'nom':'Pizza','prix':10,
                 'nom':'Tomate','prix':1}

class Commande:

    def __init__(self,commande,plat):
      self.__numéro_de_commande = commande
      self.__Statue =  "En_cours"
      self.__liste_de_plat_commander = plat

    def Ajouter(self,add):
       self.__liste_de_plat_commander += [add]

    def annuler(self,add):
       self.__liste_de_plat_commander -= [add]
    
    def total(self):
        résultat = 0
        for i in self.__liste_de_plat_commander:
            résultat +=  self.__liste_de_plat_commander[i]['prix'] + self.tva()
        return(résultat)
    
    def tva(self,prix):
     return (prix * 0,2) 

instance = Commande(8)

print(instance.Ajouter(6))