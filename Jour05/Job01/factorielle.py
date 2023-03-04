def factorielle(n):
    if n == 0:
        return 1
    else:
        return  n * factorielle(n-1)
    
#def Factorielle(n):
    #if n == 1:
        #return(n)
    #return(n*Factorielle(n-1))

enter =  int(input("Veuillez entrer un nombre: "))

print(factorielle(enter))