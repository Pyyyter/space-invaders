from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.animation import *
from pygame import mixer
import menu
import funcoes




def jogo():
    lista_tiro = []
    delay = 0
    v = []  
    crash = False
    contamove = 0
    janela_j = Window(1920,1080)
    conta2 = 0
    mixer.init()
    linha = 4
    coluna = 10

    #sprites
    nave = Sprite("assets/xwing.png")
    background = Sprite("assets\walljogo.png")
    nave.set_position(janela_j.width/2 - nave.width/2 ,950)

    #Usuario
    teclado = Window.get_keyboard()
    click = Window.get_mouse()

    #variaveis
    velx = 300
    vely = 300
    veli = 60
    mixer.music.load('assets/game.mp3')
    mixer.music.set_volume(0.2)
    mixer.music.play()

    while True:
        background.draw()
        nave.draw()



        if teclado.key_pressed("LEFT") and nave.x >= 0:
            nave.x -= velx * janela_j.delta_time()
        elif teclado.key_pressed("RIGHT") and nave.x <= janela_j.width - nave.width:
            nave.x += velx * janela_j.delta_time()



        if conta2 == 0:
            funcoes.criaMatriz(coluna, linha, v)
            conta2 += 1



        delay = funcoes.piupiu(nave, background, janela_j, teclado, velx , vely, lista_tiro, delay)



        crash  = funcoes.printaMatriz(coluna, linha, v, nave, crash)



        if contamove >= 15 :
            veli = funcoes.movematriz(coluna, linha, v, janela_j, veli, nave)
            contamove = 0
        contamove += 1

        

        if crash:
                background = Sprite("assets/fail.png")
                mixer.music.load('assets/loss.mp3')
                mixer.music.set_volume(0.2)
                mixer.music.play()
                while True:
                    background.draw()
                    janela_j.update()


        if teclado.key_pressed("ESC"):
            janela_j.close()




        janela_j.update()
