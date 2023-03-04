def list(n):
    if len(n) == 1:
        return n[0]
    if n[0] > n[1]:
        n[1] = n[0]
    return(list(n[1:]))


print(list([10,3,57,6,7,9]))