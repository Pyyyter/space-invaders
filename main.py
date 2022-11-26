from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.animation import *
from pygame import mixer
import menu
import funcoes




def jogo():
    janela_altura = 1080
    janela_largura = 1920
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
    background = Sprite("assets/walljogo.png")
    nave.set_position(janela_j.width/2 - nave.width/2 ,950)

    #Usuario
    teclado = Window.get_keyboard()
    click = Window.get_mouse()
    listatiro = []
    #variaveis
    total = linha * coluna
    totalpontos = linha * coluna
    velmonstro = 0.5
    velx = 300
    vely = 300
    veli = 0.5
    pontos = 0
    mixer.music.load('assets/game.mp3')
    mixer.music.set_volume(0.2)
    mixer.music.play()
    cooldown2 = 0
    cooldown = 0
    lifes = 1
    invincible = False
    countinvincible = 120
    while True:
        background.draw()
        nave.draw()


        #Mover nave
        if teclado.key_pressed("LEFT") and nave.x >= 0:
            nave.x -= velx * janela_j.delta_time()
        elif teclado.key_pressed("RIGHT") and nave.x <= janela_j.width - nave.width:
            nave.x += velx * janela_j.delta_time()
        # Atirar
        delay = funcoes.piupiu(nave, background, janela_j, teclado, velx , vely, lista_tiro, delay)



        # Criar matriz
        if conta2 == 0:
            funcoes.criaMatriz(coluna, linha, v)
            conta2 += 1
        
        
        # Mover matriz
        if contamove >= 3 :
            velmonstro = funcoes.movematriz(coluna, linha, v, janela_j, velmonstro, nave)
            contamove = 0
        contamove += 1
        
        
        # Printar matriz e checar derrota
        crash, pontos  = funcoes.printaMatriz(coluna, linha, v, nave, crash, lista_tiro, pontos)
        if pontos >= totalpontos:
            conta2 = 0
            v = []
            totalpontos += total

        
        # Finalizar jogo, se derrotado
        if crash or (lifes == 0):
                background = Sprite("assets/fail.png")
                mixer.music.load('assets/loss.mp3')
                mixer.music.set_volume(0.2)
                mixer.music.play()
                funcoes.colocar_ranking(pontos)
                listapontos = funcoes.translate("ranking.txt")
                while True:
                    
                    background.draw()
                    funcoes.printaranking(listapontos,janela_altura, janela_largura, janela_j)
                    janela_j.update()

                    if teclado.key_pressed("ESC"):
                        janela_j.close()


    
        cooldown, lifes,invincible, countinvincible = funcoes.monstroatira(v, nave, vely, janela_j, cooldown, listatiro, lifes, invincible, countinvincible)
        if teclado.key_pressed("ESC"):
            janela_j.close()
        janela_j.update()
