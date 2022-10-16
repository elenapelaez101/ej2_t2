
def separar(texto):
    trozos = texto.split("#")
    return trozos
    
def mayus (lista):
    new =[]
    for i in lista:
        cap = i.capitalize()
        new.append(cap)
    return new
def mods(listi):
    listi[0] = listi[0]+"..."
    for l in listi[1:]:
        l = l +"."
    print(listi)

        
    

t= separar("un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro")
print(t)
u = mayus(t)
mods(u)