# dimensões
janela_largura = 700
janela_altura = 1000

#velocidade
vx = 400
vy = 400

def run(background,teclado,janela,spaceship):
    background.draw()
    spaceship.draw()
    if teclado.key_pressed("A") and spaceship.x > 10:
        spaceship.x = spaceship.x - vx * janela.delta_time()
    if teclado.key_pressed("D") and spaceship.x /2 < 290:
        spaceship.x = spaceship.x + vx * janela.delta_time()

def shoot(background,teclado,janela,shoot,spaceship):
    if teclado.key_pressed("SPACE"):
        shoot.x = spaceship.x + shoot.width * 2 + spaceship.width/2 - 20
        shoot.y = janela_altura - spaceship.height - shoot.height
        while True:
            run(background,teclado,janela,spaceship)
            shoot.draw()
            shoot.y = shoot.y - vy * janela.delta_time()
            if shoot.y < 0:
                break
            janela.update()
