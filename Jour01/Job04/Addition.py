class Operation:
   #Ici on addictionne les deux nombres grâce à la fonction addition.
   #Ensuite on print le résultat. 
    def __init__(self):
        self.nombre1 = 1
        self.nombre2 = 2

    def addition(self):
       return(self.nombre1 + self.nombre2)

operateur = Operation()

print(operateur.addition())