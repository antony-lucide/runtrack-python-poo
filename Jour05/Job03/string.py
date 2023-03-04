def String(string):
    if string == ():
        return(0)
    return(1+String(string[1:]))

print(String('michel'))