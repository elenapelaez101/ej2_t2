class Trasformar:
    def __init__(self, texto):
        self.texto = texto

    def separar(self):
        trozos = self.texto.split("#")
        print(trozos)
        

t= Trasformar("un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro")
t.separar()