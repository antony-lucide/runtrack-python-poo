class Personne:
   #La classe personne et le constructeur + la fonction se présenter permet d'afficher des informations rentré.
    def __init__(self,nom,prenom):
        self.prenom = prenom
        self.nom = nom

    
    def SePresenter(self):
        return(self.prenom + self.nom)

résultat = Personne("Goerge","Washington")

résultat2 = Personne("Williams","Petterson")

print(résultat.SePresenter())
print(résultat2.SePresenter())
