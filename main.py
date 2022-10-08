from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
import game

################################ JANELA #######################################

# dimensões
gameall_width = 700
gameall_height = 1000

# janela do menu
janela = Window(gameall_width, gameall_height)
janela.set_title("Space Invaders")
background = Sprite("assets/Wall.jpg")

# pegando a entrada do usuário
teclado = janela.get_keyboard()
click = janela.get_mouse()

# janela settings
p_settings = True

# janela leaderboard
p_LeaderBoard = True

############################# FIM DA JANELA ###################################

# botoes de dificuldade
Facil = Sprite("assets/Facil.png")
Facil.set_position(gameall_width/2 - 200, 200)
Medio = Sprite("assets/Medio.png")
Medio.set_position(gameall_width/2 - Medio.width/2, 200)
Dificil = Sprite("assets/Dificil.png")
Dificil.set_position(gameall_width/2 + 80, 200)

################################ BOTÕES #######################################

# botao play
play = Sprite("assets/Jogar.png")
play.set_position(gameall_width / 2- Medio.width/2, 160)

# botao exit do settings
exits = Sprite("assets/Sair.png")
exits.set_position(gameall_width / 2- Medio.width/2, 510)

# botao leaderboard
leaderboard = Sprite("assets/Ranking.png")
leaderboard.set_position(gameall_width / 2- Medio.width/2, 360)

# botao exit
exit = Sprite("assets/Sair.png")
exit.set_position(gameall_width / 2- Medio.width/2, 460)

# botao exit do leaderboard
exitl = Sprite("assets/Sair.png")
exitl.set_position(gameall_width / 2- Medio.width/2, 510)

# botao settings
settings = Sprite("assets/Dificuldade.png")
settings.set_position(gameall_width / 2- Medio.width/2, 260)
p_settings = True
############################ FIM DOS BOTÕES ###################################

# SHIP
navinha = Sprite("assets/xwing.png")
navinha.x = gameall_width/2 - navinha.width/2
navinha.y = gameall_height - navinha.height - 10

# SHOOT
shoot = Sprite("assets\shoot.png")
shoot.x = navinha.x + shoot.width * 2
shoot.y = gameall_height - navinha.height - shoot.height * 2


while True:
    # draw all
    background.draw()
    play.draw()
    settings.draw()
    leaderboard.draw()
    exit.draw()

    # title
    janela.draw_text("INIMIGOS DO IMPÉRIO", gameall_width / 2 - 260, 50, size=50, color=(224, 224, 220), font_name="Arial",
                     bold=True, italic=True)

    # play
    if click.is_over_object(play) and click.is_button_pressed(True):
        janelagameall = Window(gameall_width, gameall_height)
        janelagameall.set_title("Space Invaders")
        while True:
            game.run(background,teclado,janelagameall,navinha)
            game.tiro(background,teclado,janelagameall,shoot,navinha)
            
            if teclado.key_pressed("ESC"):
                break
            janelagameall.update()
    
    # settings
    if click.is_over_object(settings) and click.is_button_pressed(True):
        if p_settings == True:
            p_settings = False
            winconfig = Window(gameall_width, gameall_height)
            winconfig.set_title("Space Invaders - Ramon")
            while True:
                # janela settings
                background.draw()
                exits.draw()
                winconfig.draw_text("Settings", gameall_width / 2- 140, 20, size=64, color=(224, 224, 220),
                                 font_name="Arial",
                                 bold=True, italic=False)
                winconfig.draw_text("Dificuldade", gameall_width / 2- 90, 130, size=32, color=(224, 224, 220),
                                 font_name="Arial",
                                 bold=True, italic=False)
                Facil.draw()
                Medio.draw()
                Dificil.draw()
                winconfig.update()
                if click.is_over_object(exits) and click.is_button_pressed(True):
                    break
        else:
            p_settings = True

    #leaderboard
    if click.is_over_object(leaderboard) and click.is_button_pressed(True):
        if p_LeaderBoard == True:
            p_LeaderBoard = False
            janelaLeaderBoard = Window(gameall_width,gameall_height)
            janelaLeaderBoard.set_title("Space Invaders")
            while True:
                background.draw()
                exitl.draw()
                janela.draw_text("Leader Board", gameall_width / 2 - 210, 50, size=64, color=(224, 224, 220),
                                 font_name="Arial",
                                 bold=True, italic=False)
                janela.update()
                if click.is_over_object(exitl) and click.is_button_pressed(True):
                    break
        else:
            p_LeaderBoard = True

    # botao exit
    if click.is_over_object(exit) and click.is_button_pressed(True):
        janela.close()


    janela.update()