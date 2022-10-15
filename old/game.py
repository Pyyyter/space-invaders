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
while true
def tiro(background,teclado,janela,tiro,navinha, vetor):
    if teclado.key_pressed("SPACE"):
        tiro sdkajsdkjaf
        posição tiro asdkjaskjfkajk
        vetor.append(tiro)
        
    for i in vetor:
        i.y = i.y - (vy-385) * janela.delta_time()
        i.draw()
        if i.y <= 0:
            vetor.pop(i)
        
    janela.update()

        # if vetor[i].y < 0:
        #     vetor.pop(i)