class Tache:

    def __init__(self,titre,A_Faire):
      self.titre = titre
      self.statut = A_Faire

    

class Liste_de_tache:
   
    def __init__(self):
        self.tache = []

    def accesseur_tache(self):
        return(self.tache)
    
    def mutateur_tache(self,tache):
        self.tache = tache
    
    def accesseur_statut(self):
        return(self.statut)
    
    def AjouterTache(self,tache):
        self.tache.append(tache)
    
    def SupprimerTache(self,tache):
        self.tache.remove(tache)
    
    def marqueCommeFinie(self,tache,Finis):
        self.statut = Finis
    
    def afficherListe(self):
        for x in self.tache:
            print(x.titre)
    
    def filtertache(self,finis,filtre):
        résultat = []
        for i in self.tache:
            if i.accesseur.statut() == filtre:
                résultat += [i]
        return(résultat)

instance = Tache('Git','liste de tache')

instance2 = Liste_de_tache()

instance2.AjouterTache(instance)
instance2.afficherListe()