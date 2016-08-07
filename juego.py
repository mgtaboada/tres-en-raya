from Tablero import *
from IA import *
from Casilla import *
from Movimiento import *
from Posicion import *
X = 1
O = 2
Jugador = 1
ia = 2
def mover_usuario(tablero):
    x_init = int(input("X inicial: "))
    y_init = int(input("Y inicial: "))
    x_fin = int(input("X final: "))
    y_fin = int(input("Y final: "))
    pos_init = Posicion(x_init, y_init)
    pos_fin = Posicion(x_fin, y_fin)
    mov = Movimiento(pos_init, pos_fin)
    tablero.mover_m(mov)
def mover_usuario_inicial(tablero):
    x_fin = int(input("X final: "))
    y_fin = int(input("Y final: "))
    tablero.mover_inicial(Posicion(x_fin,y_fin),Jugador)
def empezar(tablero):
    for i in range(2):
        if not tablero.fin_juego():
            mostrar(tablero)
            mover_usuario_inicial(tablero)
            tablero.mover_inicial(que_hacer_inicial(tablero),ia)
    for i in range(1):
        if not tablero.fin_juego():
            mostrar(tablero)
            mover_usuario_inicial(tablero)
            tablero.mover_inicial(que_hacer(tablero,ia).objetivo,ia)

def mostrar(tablero):
   tablero.imprimir_bonito()
tablero = Tablero()
empezar(tablero)
fin = False
while not fin:
    fin = tablero.fin_juego()
    if not fin:
        mostrar(tablero)
    fin = tablero.fin_juego()
    if not fin:
        mover_usuario(tablero)
    fin = tablero.fin_juego()
    if not fin:
        tablero.mover_m(que_hacer(tablero,ia))
mostrar(tablero)
print("Fin del juego!")
