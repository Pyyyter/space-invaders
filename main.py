from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.animation import *
import menu
import funcoes



def jogo():
    lista_tiro = []
    delay = 0

    janela_j = Window(1280,720)

    #sprites
    nave = Sprite("assets/xwing.png")
    background = Sprite("assets\wall.jpg")
    nave.set_position(1280/2 - nave.width ,600)

    #Usuario
    teclado = Window.get_keyboard()
    click = Window.get_mouse()

    #variaveis
    velx = 300
    vely = 300


    while True:
        background.draw()
        nave.draw()

        if teclado.key_pressed("LEFT") and nave.x >= 0:
            nave.x -= velx * janela_j.delta_time()
        elif teclado.key_pressed("RIGHT") and nave.x <= 1280 - nave.width:
            nave.x += velx * janela_j.delta_time()


        delay = funcoes.piupiu(nave, background, janela_j, teclado, velx , vely, lista_tiro, delay)

        if teclado.key_pressed("ESC"):
            janela_j.close() 

        janela_j.update()