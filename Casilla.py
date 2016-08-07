class Casilla:
    def __init__(self, ocupada, equipo):
        self.ocupada = ocupada
        self.equipo = equipo

    def esta_ocupada(self):
        return self.ocupada
    def ocupar(self, equipo):
        self.ocupada = True
        self.equipo = equipo
    def desocupar(self):
        self.ocupada = False
        self.equipo=0
