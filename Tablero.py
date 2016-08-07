
import IA
from Casilla import *
class Tablero:
    def __init__(self):
        self.tablero = ([[Casilla(False,0),Casilla(False,0),Casilla(False,0)],
                         [Casilla(False,0),Casilla(False,0),Casilla(False,0)],
                         [Casilla(False,0),Casilla(False,0),Casilla(False,0)]])
    # Devuelve una copia del mismo tablero
    def copiar(self):
        aux = Tablero()
        for i in range(3):
            for j in range(3):
                aux.tablero[i][j] = (Casilla(self.tablero[i][j].esta_ocupada(),
                                             self.tablero[i][j].equipo()))
        return aux
    # mueve lo que haya en la posicion "actual" a la posicion "objetivo"
    def mover(self, actual, objetivo):
        c_actual = self.tablero[actual.x][actual.y]
        c_objetivo = self.tablero[objetivo.x][objetivo.y]
        c_objetivo.ocupar(c_actual.equipo())
        c_actual.desocupar()
    # mueve lo que diga el objeto movimento 
    def mover_m(self, movimiento):
        self.mover(movimiento.inicial, movimiento.objetivo  )

    # Devuelve una matriz análoga al tablero con el numero del equipo que esta en
    # cada posicion
    def matriz_equipos(self):
        matriz = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j].esta_ocupada():
                    matriz[i][j] = self.tablero[i][j].equipo()
                else:
                    matriz[i][j]=0
        return matriz
    # devuelve la Casilla que hay en la posicion dada
    def casilla(self,posicion):
        return self.tablero[posicion.x][posicion.y]
    # Muestra la matriz dada por pantalla
    def imprimir_tablero(self,m):
        print (40*"\n")
        print("""   0 | 1 | 2
        ------------
        0 %s |%s | %s
        ------------
        1 %s | %s | %s
        ------------
        2 %s | %s | %s""" %( m[0][0],
                             m[1][0],
                             m[2][0],
                             m[0][1],
                             m[1][1],
                             m[2][1],
                             m[0][2],
                             m[1][2],
                             m[2][2]))

    # Coloca una ficha del equipo dado en la posicion dada
    def mover_inicial(self,posicion,equipo):
        self.tablero[posicion.x][posicion.y].ocupar(equipo)
    # devuelve cierto si algun jugador ha terminado el juego
    def fin_juego(self):
        return IA.hay_linea_3(self)
    # Devuelve una matriz de caracteres con X para las posiciones de las fichas
    # de la IA, O para las posiciones del jugador y espacio para los vacíos
    def matriz_letras(self):
        matriz = [["","",""],["","",""],["","",""]]
        def a_letra(numero):
            if numero == 2:
                return "X"
            elif numero == 1:
                return "O"
            else:
                return " "
        for i in range(3):
            for j in range(3):
                if(self.tablero[i][j].esta_ocupada()):
                    matriz[i][j] = a_letra(self.tablero[i][j].equipo())
                else:
                    matriz[i][j] = " "
        return matriz
    # Muestra por pantalla el tablero con los caracteres especificados
    # en matriz_letras
    def imprimir_bonito (self):
        self.imprimir_tablero(self.matriz_letras())
