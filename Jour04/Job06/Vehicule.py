class Vehicule:

    def __init__(self,marque,année,prix):
        self.marque = marque
        self.année = année
        self.prix = prix
    
    def informationVehicule(self,marque,année,prix):
        print(self.marque,self.année,self.prix)
    
class Voiture(Vehicule):
    
    def __init__(self, marque, année, prix):
       self.portes = 4
     
    
    def informationVehicule(self, marque, année, prix):
        return super().informationVehicule(self.marque,self.année,self.prix,self.portes)
    
instance = Voiture('Volvo','2002',40)

instance.informationVehicule('Volvo','2002',40)