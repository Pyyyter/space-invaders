from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.animation import *
from PPlay.collision import *
import main
 

def piupiu(nave, background, janela, teclado, velx , vely, lista, delay):
    if teclado.key_pressed("SPACE") and delay == 0:
        print("espaço funcionando")
        criartiro(lista, nave)
        delay = 300
    #tem tiro pra disparar
    if len(lista) > 0:
        for tiro in lista:
            tiro.draw()
            tiro.y -= vely * janela.delta_time()
            if tiro.y < -10:
                lista.remove(tiro)
    if delay > 0:
        delay -= 1
    return delay





def criartiro(lista, nave):
    tiro = Sprite("assets/shoot.png")
    tiro.x = nave.x + 39
    tiro.y = nave.y - nave.height/2
    lista.append(tiro)

def criaMatriz(linha,coluna,lista):
    for i in range (linha):
        list = []
        for j in range (coluna):
            alien = Sprite("assets/alien.png")
            alien.x = (120 * (i)) + 5
            alien.y = (100 * (j)) + 20
            list.append(alien)
        lista.append(list)



def movematriz(linha, coluna, lista, janela, vel, nave):
    colidiu = False
    for i in range(linha):
        for j in range(coluna):
            lista[i][j].x += 10*vel
            if (lista[i][j].x >= janela.width - 90 or lista[i][j].x <= 0):
                colidiu = True
    if colidiu == True:
        vel = vel*(-1)
        for i in range(linha):
            for j in range(coluna):
                lista[i][j].y += 30
    return vel

def printaMatriz(linha, coluna, lista, nave, crash):
    for i in range(linha):
        for j in range(coluna):
            lista[i][j].draw()
            if Collision.perfect_collision(lista[i][j], nave):
                crash = True
                return crash 