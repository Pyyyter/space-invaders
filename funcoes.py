from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.animation import *
from PPlay.collision import *
from random import randrange
import main
 

def piupiu(nave, background, janela, teclado, velx , vely, lista, delay):
    if teclado.key_pressed("SPACE") and delay == 0:
        criartiro(lista, nave)
        delay = 100
    #tem tiro pra disparar
    if len(lista) > 0:
        for tiro in lista:
            tiro.draw()
            tiro.y -= vely* 10 * janela.delta_time()
            if tiro.y < -10:
                lista.remove(tiro)
    if delay > 0:
        delay -= 1
    return delay

def monstroatira(lista, nave, vely, janela,cooldown, listatiro, lifes, invincible, countinvincible):
    linha = randrange(0,len(lista)-1)
    coluna = randrange(0,len(lista[linha])-1)
    if lista[linha][coluna] != 0:
        if cooldown <= 0:
            listatiro.append(Sprite("assets\shoot.png"))
            listatiro[-1].x = lista[linha][coluna].x
            listatiro[-1].y = lista[linha][coluna].y
            cooldown = 100
        
    if len(lista) > 0:
        for tiro in listatiro:
            tiro.draw()
            tiro.y += vely* 10 * janela.delta_time()

    if countinvincible <=0:
        invincible = False
    for i in range(len(listatiro)):
        if not invincible:
            if listatiro[i].collided_perfect(nave): 
                listatiro.pop(i)
                lifes -= 1
                nave.set_position(janela.width/2 - nave.width/2 ,950) 
                invincible = True
                countinvincible = 130
    cooldown -= 1 
    countinvincible -=1
    return cooldown, lifes, invincible, countinvincible


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

def movematriz(linha, coluna, lista, janela, velmonstro, nave):
    colidiu = False
    for i in range(linha):
        for j in range(coluna):
            if lista[i][j] != 0:
                # if lista[i][j].y >= janela.height/2:
                lista[i][j].x += 10*velmonstro
                # else :
                #     for k in range (len(velmonstro)):
                #         velmonstro *= 2
                if (lista[i][j].x >= janela.width - 90 or lista[i][j].x <= 0):
                    colidiu = True
                if colidiu:
                    velmonstro = velmonstro*(-1)
                    for k in range(linha):
                        for j in range(coluna):
                            if lista[k][j] == 0:
                                pass
                            else:
                                lista[k][j].y += 30
                    colidiu = False    
    return velmonstro

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

def colocar_ranking(score):
    name = input('Qual seu nome? : ')
    ranking_r = open('ranking.txt', 'r')
    ranking_list = ranking_r.readlines()
    ranking_list.append(name + ':' + str(score) + ';')
    ranking_r.close
    ranking_w = open('ranking.txt', 'w')
    ranking_w.writelines(ranking_list)
    ranking_w.close()

def translate(file):
    arquivo = open(file)
    pontuacao = []
    for elemento in arquivo:
        temp = elemento.split(";")
        for i in temp:
            pontuacao.append(i)
    arquivo.close()
    return pontuacao

def printaranking(lista_ranking, janela_altura, janela_largura,janela):
    limite = 0 
    altura = 0
    for i,rankeado in enumerate(lista_ranking):
        if i == 0:
            continue
        if limite < 5:
            janela.draw_text(str(rankeado), janela_largura / 2 - 170, janela_altura/2 - 140 + altura, size=32, color=(224, 224, 220), font_name="Arial", bold=True, italic=False)
            limite += 1
            altura += 60