from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.animation import *
from PPlay.collision import *
import main
 

def piupiu(nave, background, janela, teclado, velx , vely, lista, delay):
    if teclado.key_pressed("SPACE") and delay == 0:
        criartiro(lista, nave)
        delay = 100
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
    tiro.x = nave.x + nave.width/2 - 5
    tiro.y = nave.y - 5
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
            if lista[i][j] == 0:
                pass
            else:
                if lista[i][j].y >= janela.height/2:
                    lista[i][j].x += 20*vel
                else:
                    lista[i][j].x += 10*vel
                if (lista[i][j].x >= janela.width - 90 or lista[i][j].x <= 0):
                    colidiu = True
                if colidiu:
                    vel = vel*(-1)
                    for i in range(linha):
                        for j in range(coluna):
                            if lista[i][j] == 0:
                                pass
                            else:
                                lista[i][j].y += 30
                    colidiu = False    
    return vel

def printaMatriz(linha, coluna, lista, nave, crash, vetortiro, pontos):
    for i in range(linha):
        for j in range(coluna):
            if lista[i][j] == 0:
                pass
            else:
                lista[i][j].draw()
                if Collision.perfect_collision(lista[i][j], nave):
                        crash = True
                for k in range(len(vetortiro)):
                    if Collision.perfect_collision(lista[i][j], vetortiro[k]):
                        lista[i][j] = 0
                        vetortiro.pop(k)
                        pontos += 1
                        print(pontos)
                        break
    return crash, pontos