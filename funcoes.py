from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.animation import *
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

def criaMatriz(linha,coluna,lista,contador):
    if contador == 0:  
        for i in range (linha):
            for j in range (coluna):
                alien = Sprite("assets/alien.png")
                alien.x = 150 * (i+1)
                alien.y = 150 * (j+1)
                lista.append(alien)
        contador += 1
    return contador

def printaMatriz(linha, coluna, lista, contador):
    criaMatriz(linha, coluna, lista, contador)
    for i in lista:
        i.draw()