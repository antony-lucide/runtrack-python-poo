class Produit:
    
    def __init__(self,nom,prix,tax):
      self.nom = nom
      self.prixHT = prix
      self.tva = tax
    
    def CalculerPrixTTC(self):
       return(self.tva + self.prixHT)
    
    def afficher(self):
       print(self.nom,self.prixHT,self.tva)

instance2 = Produit("Euro",9,7)
instance = Produit(9,7,10)

instance2.afficher()
print(instance.CalculerPrixTTC())