
from Movimiento import *
from Posicion import *
from Tablero import *

# Matriz básica de la utilidad que tiene mover a cada posicion, basada en
# la cantidad de posiciones que se pueden amenazar desde cada posicion.
utilidad_base = [[0.75, 0.5, 0.75], [0.5, 1, 0.5], [0.75, 0.5, 0.75]]

# Devuelve un tablero con la misma distribución que el dado, salvo porque lo que haya en la posición "pos_actual" se habŕa movido a "pos_objetivo"
def sup(tablero,pos_actual, pos_objetivo):
    tablero_aux = tablero.copiar()
    tablero_aux.mover(pos_actual, pos_objetivo)
    return tablero_aux

# Devuelve 1 si la posicion "i" posiciones por delante según
# la "funcion_siguiente", está ocupada y tiene el mismo equipo que el dado,
# 0 en otro caso
def comprobar(tablero,funcion_siguiente, i,pos_inicial,equipo):
    hay_linea =(tablero.casilla(funcion_siguiente(pos_inicial,i)).equipo ==
                equipo and
                tablero.casilla(funcion_siguiente(pos_inicial,i)).esta_ocupada())
    if hay_linea:
        return 1
    else:
        return 0
# Devuelve 10 si la posicion dada no está ocupada y es parte de alguna linea
# que completa la posicion dada, si la posicion dada completaría una línea
# pero está ocupada devuelve 2, si no devuelve 0
def hay_linea_2(tablero, pos):
    linea_diagonal = False
    linea_horizontal = False
    linea_vertical = False
    linea_vertical = (tablero.tablero[pos.x][(pos.y+1)%3].esta_ocupada() and
                      tablero.tablero[pos.x][(pos.y+2)%3].esta_ocupada() and
                      tablero.tablero[pos.x][(pos.y+1)%3].equipo ==
                      tablero.tablero[pos.x][(pos.y+2)%3].equipo)
    linea_horizontal = (tablero.tablero[(pos.x+1)%3][pos.y].esta_ocupada() and
                        tablero.tablero[(pos.x+2)%3][pos.y].esta_ocupada() and
                        tablero.tablero[(pos.x+1)%3][pos.y].equipo ==
                        tablero.tablero[(pos.x+2)%3][pos.y].equipo)
    if pos.es_diagonal_principal():
        linea_diagonal =(
            tablero.tablero[(pos.x+1)%3][(pos.y+1)%3].esta_ocupada() and
            tablero.tablero[(pos.x+2)%3][(pos.y+2)%3].esta_ocupada() and
            tablero.tablero[(pos.x+1)%3][(pos.y+1)%3].equipo ==
            tablero.tablero[(pos.x+2)%3][(pos.y+2)%3].equipo)
    elif pos.es_diagonal_secundaria():
        linea_diagonal = (
            tablero.tablero[(pos.x-1)%3][(pos.y+1)%3].esta_ocupada() and
            tablero.tablero[(pos.x-2)%3][(pos.y+2)%3].esta_ocupada() and
            tablero.tablero[(pos.x-1)%3][(pos.y+1)%3].equipo ==
            tablero.tablero[(pos.x-2)%3][(pos.y+2)%3].equipo)
    resultado = linea_horizontal or linea_diagonal or linea_vertical
    if resultado and not tablero.tablero[pos.x][pos.y].esta_ocupada():
        return 10
    elif resultado:
        return 2
    else:
        return 0

# Devuelve cierto si hay alguna linea de tres en el tablero dado,
# falso en otro caso
def hay_linea_3(tablero):
    hay_linea_3 = False
    horizontal = 0
    vertical = 0
    diagonal_principal = 0
    diagonal_secundaria = 0
    for i in range(3):
        equipo_horizontal = tablero.tablero[0][i].equipo
        equipo_vertical = tablero.tablero[i][0].equipo
        diagonal_principal = (diagonal_principal +
                              comprobar(tablero,
                                        Posicion.siguiente_diagonal_principal,
                                        i,
                                        Posicion(0,0),
                                        tablero.tablero[0][0].equipo))
        diagonal_secundaria = (diagonal_secundaria +
                               comprobar(tablero,
                                    Posicion.siguiente_diagonal_secundaria,
                                    i,
                                    Posicion(0,2),
                                    tablero.tablero[0][2].equipo))
        # comprobar las lineas horizontal y vertical en la posicion i:
        for j in range(3):
            horizontal = (horizontal +
                          comprobar(tablero,
                                    Posicion.siguiente_horizontal,
                                    j,
                                    Posicion(0,i),
                                    equipo_horizontal))
            vertical = (vertical +
            comprobar(tablero,
                      Posicion.siguiente_vertical,
                      j,
                      Posicion(i,0),
                      equipo_vertical))
        hay_linea_3 = hay_linea_3 or (vertical == 3) or (horizontal ==3)
        horizontal = 0
        vertical = 0
    hay_linea_3 = (hay_linea_3 or
                   (diagonal_principal == 3) or
                   (diagonal_secundaria == 3))
    return hay_linea_3

# Devuelve 100 si resulta una linea de tres de mover lo que hay en la
# "pos_actual" a la "pos_objetivo"
def hace_linea_3(tablero,pos_actual, pos_objetivo):
    if hay_linea_3(tablero):
        print("[hace_linea_3] ya hay linea")
    tablero_aux = sup(tablero,pos_actual, pos_objetivo)
    if( hay_linea_3(tablero_aux)):
        return 100
    else:
        return 0

# Devuelve cierto si hay alguna posicion en linea con la "pos" dada y que
# además tiene el mismo equipo
def es_parte_de_linea(tablero, pos, equipo):
    linea_diagonal = False
    linea_horizontal = False
    linea_vertical = False
    i = 0
    while i < 3:
        vertical = tablero.tablero[pos.x][(pos.y + i) % 3]
        horizontal = tablero.tablero[(pos.x + i) % 3][pos.y]
        linea_vertical = (linea_vertical or
                          (vertical.esta_ocupada() and
                           vertical.equipo == equipo))
        linea_horizontal = (linea_horizontal or
                            (horizontal.esta_ocupada() and
                             horizontal.equipo == equipo))
        if pos.es_diagonal_secundaria():
            diagonal = tablero.tablero[(pos.x -i) % 3][(pos.y + i) % 3]
            linea_diagonal = (linea_diagonal or
                              (diagonal.esta_ocupada() and
                               diagonal.equipo == equipo))
        elif pos.es_diagonal_principal():
            diagonal = tablero.tablero[(pos.x + i) % 3][(pos.y + i) % 3]
            linea_diagonal = (linea_diagonal or
                              (diagonal.esta_ocupada() and
                               diagonal.equipo == equipo))
        i += 1
    resultado = linea_horizontal or linea_diagonal or linea_vertical
    if resultado:
        return 5
    else:
        return 0

# Devuelve el numero de fichas que amenazan a la "pos" dada
def amenaza(tablero, pos):
    amenaza = 0
    i = 0
    while i < 3:
        if tablero.tablero[(pos.x+i)%3][pos.y].esta_ocupada():
            amenaza +=1
        if tablero.tablero[pos.x][(pos.y+i)%3].esta_ocupada():
            amenaza +=1
        if (pos.es_diagonal_principal() and
            tablero.tablero[(pos.x+i)%3][(pos.y+i)%3].esta_ocupada()):
            amenaza +=1
        elif( pos.es_diagonal_secundaria() and
              tablero.tablero[(pos.x-i)%3][(pos.y+i)%3].esta_ocupada()):
            amenaza +=1
        i +=1
    return amenaza

# Devuelve un valor numérico para la utilidad que tiene mover una ficha a la
# "pos" dada
def utilidad_mover_a(tablero, pos):
    return (utilidad_base[pos.x][pos.y] +
            amenaza(tablero, pos) +
            hay_linea_2(tablero, pos))

# Devuelve una matriz análoga al tablero con las utilidades que tiene mover a
# cada una de sus posiciones
def matriz_utilidad_a(tablero):
    matriz_utilidad = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            pos = Posicion(i,j)
            if tablero.tablero[i][j].esta_ocupada():
                matriz_utilidad[i][j] = 0
            else:
                matriz_utilidad[i][j]= utilidad_mover_a(tablero, pos)
    return matriz_utilidad

# Devuelve la posicion óptima a la que se debe mover
def mejor_utilidad_a(tablero):
    matriz_utilidad = matriz_utilidad_a(tablero)
    mejor_x = 0
    mejor_y = 0
    for i in range(3):
        for j in range(3):
            if (not tablero.tablero[i][j].esta_ocupada() and
                matriz_utilidad[i][j] > matriz_utilidad[mejor_x][mejor_y]):
                mejor_x=i
                mejor_y=j
    return Posicion(mejor_x, mejor_y)

# Devuelve un valor numérico para la utilidad que tiene mover la ficha
# del equipo dado  de la "pos" dada a la posicion "objetivo"
def utilidad_mover_desde(tablero,pos, objetivo,equipo):
    if (pos.equals(objetivo) or
        not tablero.tablero[pos.x][pos.y].esta_ocupada()):
        return -100
    base = utilidad_mover_a(tablero,pos)
    return (base -
            es_parte_de_linea(tablero, pos, equipo)+
            hace_linea_3(tablero, pos,objetivo))

# Devuelve una matriz análoga al tablero con las utilidades de mover
# las fichas del equipo dado a la posicion "objetivo"
def matriz_utilidad_desde(tablero, objetivo,equipo):
    matriz_utilidad = [[0,0,0],[00,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            if (tablero.tablero[i][j].equipo == equipo and
                tablero.tablero[i][j].esta_ocupada()):
                matriz_utilidad[i][j]= utilidad_mover_desde(tablero,
                                                            Posicion(i,j),
                                                            objetivo,
                                                            equipo)
    return matriz_utilidad

# Devuelve la posicion de la ficha del equipo dado que mayor utilidad tiene
# para mover a la posicion "objetivo"
def mejor_utilidad_desde(tablero, objetivo,equipo):
    matriz_utilidad = matriz_utilidad_desde(tablero,objetivo,equipo)
    mejor_x = 0
    mejor_y = 0
    for i in range(3):
        for j in range(3):
            if (tablero.tablero[i][j].esta_ocupada() and
                tablero.tablero[i][j].equipo == equipo and
                matriz_utilidad[i][j] > matriz_utilidad[mejor_x][mejor_y]):
                mejor_x=i
                mejor_y=j
    return Posicion(mejor_x, mejor_y)

# Devuelve un tipo movimiento con la posicion de la ficha que se debe mover y
# la posicion a la que debe moverse
def que_hacer(tablero,equipo_ia):
    objetivo = mejor_utilidad_a(tablero)
    inicial = mejor_utilidad_desde(tablero, objetivo,equipo_ia)
    return Movimiento(inicial, objetivo)

# Devuelve la posicion en la que debe colocarse la ficha
def que_hacer_inicial(tablero):
    return mejor_utilidad_a(tablero)
