class Vehicule:

    def __init__(self,marque,année,prix):
        self.marque = marque
        self.année = année
        self.prix = prix
    
    def informationVehicule(self):
        print(self.marque,self.année,self.prix)
    
class Voiture(Vehicule):
    
    def __init__(self,marque,année,prix):
       Vehicule.__init__(self,marque,année,prix)
       self.portes = 4
     
    
    def informationVehicule(self):
        super().informationVehicule()
        print(self.portes)

instance = Voiture('Volvo','2002',40)

instance.informationVehicule()