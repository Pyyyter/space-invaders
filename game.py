# dimensões
janela_largura = 700
janela_altura = 1000

#velocidade
vx = 400
vy = 400

def run(background,teclado,janela,navinha):
    background.draw()
    navinha.draw()
    if teclado.key_pressed("A") and navinha.x > 10:
        navinha.x = navinha.x - vx * janela.delta_time()
    if teclado.key_pressed("D") and navinha.x /2 < 290:
        navinha.x = navinha.x + vx * janela.delta_time()

def tiro(background,teclado,janela,tiro,navinha):
    if teclado.key_pressed("SPACE"):
        tiro.x = navinha.x + tiro.width * 2 + navinha.width/2 - 20
        tiro.y = janela_altura - navinha.height - tiro.height
        while True:
            run(background,teclado,janela,navinha)
            tiro.draw()
            tiro.y = tiro.y - vy * janela.delta_time()
            if tiro.y < 0:
                break
            janela.update()
