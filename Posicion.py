class Posicion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def es_centro(self):
        return self.x == 1 and self.y == 1

    def es_diagonal_principal(self):
        return self.x == self.y

    def es_diagonal_secundaria(self):
        return self.x + self.y ==2

    def equals(self,pos):
        return self.x == pos.x and self.y ==pos.y

    def siguiente_horizontal(self,i):
        return Posicion((self.x +i) % 3, self.y)

    def siguiente_vertical(self,i):
        return Posicion(self.x, (self.y + i )% 3)

    def siguiente_diagonal_principal(self,i):
        return Posicion((self.x + i) % 3, (self.y + i)%3)

    def siguiente_diagonal_secundaria(self,i):
        return Posicion((self.x -i) % 3, (self.y + i) % 3)
