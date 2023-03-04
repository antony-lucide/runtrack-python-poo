def entier(x,n):
    if n == 1:
        return x
    return(x * entier(x,n-1))

print(entier(4,6))