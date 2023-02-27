class Cercle:
    
    def __init__(self,Rayon,aire,circonférense,diam):
        self.rayon = 0
        self.air = 0
        self.diameter = 0
        self.circonferescence = 0

    def AfficherInfo(self,aire,circonférense,diam,Rayon):
        self.rayon = Rayon
        self.air = aire
        self.circonferescence = circonférense
        self.diameter = diam
        print(Rayon,aire,circonférense,diam)


    def changer_le_rayon(self):
        self.rayon = 0
                
    def circonférence(self,aire,circonférense):
        circonférense = circonférense + self.rayon + aire 
        return(circonférense)
    
    def aire(self, aire, ciconférense):
        aire = aire + self.rayon + ciconférense
        return(aire) 
    
    def diamètre(self,aire,circonférense,diam):
        diam = diam +  self.rayon + aire + circonférense
        return(diam)

instance = Cercle(Rayon=4,aire=7,circonférense=9,diam=8)

print(instance.AfficherInfo(Rayon=4, aire=5,circonférense=9,diam=8))