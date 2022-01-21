from os import system
from time import sleep
from random import randint

def checarPrincipal(valor, tabuleiro):
    sequencias = [
        # colunas
        [0,3,6],
        [1,4,7],
        [2,5,8],
        # diagonal
        [0,4,8],
        [2,4,6],
        # linhas
        [0,1,2],
        [3,4,5],
        [6,7,8]
    ]
    
    def validarSequencia(valor, sequencia):
        for posicao in sequencia:
            if tabuleiro[posicao] == valor:
                continue
            else:
                return False
        return True

    for sequencia in sequencias:
        if validarSequencia(valor,sequencia):
            return True 
        else:
            continue # proxima sequencia
    return False

def l():
    system("cls")

def mostrar(jogo):
    for posicao, valor in enumerate(tabuleiro):
        print(f"{    valor} ", end=' | ')
        if (posicao + 1) % 3 == 0:
            print("\n--------------")

def jogar(jogador,valor,tabuleiro):
    while True:
        mostrar(tabuleiro)
        jogada = int(input(f"Vez do {jogador} \nEm que posicao deseja jogar [Digite um numero e aperte a tecla Enter]: ")) -1
        if type(tabuleiro[jogada]) == int:
            tabuleiro[jogada] = valor
            break
        else:
            print(f"ERRO! A posição {jogada} está ocupada. Escolha uma posição que nao tenha sido jogada.\n")

def loading(frase):
    for i in range(0,3):
        print(frase,flush=True)
        sleep(1)
        frase += "."
        l()


# main
print("Bem vindo ao Jogo da Velha")
tabuleiro = [1,2,3,4,5,6,7,8,9]
# Jogar com computador ou jogar contra pessoa
modoDeJogo = int(input("Quer jogar com o computador [Digite 1] \nQuer jogar com outra pessoa [Digite 2] \nDigite sua opcao: "))
jogadas = 0
if modoDeJogo == 1:
    jogador = str(input("Digite seu nome: "))
    p1 = int(input(f"\n{jogador}, digite 1 para jogar com X, ou digite dois para jogar com O: "))
    if p1 == 1:
        p1 = "X"
        computador = "O"
    elif p1 == 2:
        p1 = "O"
        computador = "X"
    
    print(f"O {jogador} escolheu {p1} e o computador fica com {computador}\n",flush=True)
    sleep(3)
    l()
    
    loading("Iniciando o jogo.")

    condicao = "continua"
    contador = 0
    condicoes = [str(f"{jogador} venceu"), "O computador venceu"]
    while condicao == "continua":
        #jogador 1
        jogar(jogador,p1,tabuleiro)
        l()
        if checarPrincipal(p1,tabuleiro):
            condicao = str(f"{jogador} venceu")
            break

        jogadas += 1
        if jogadas == 9 and not condicao in condicoes:
            condicao = "Deu Velha"

        # computador
        loading("Estou pensando.")
        while True:
            jogada = randint(0,8)
            if type(tabuleiro[jogada]) == int:
                tabuleiro[jogada] = computador
                jogadas += 1
                break

        if checarPrincipal(computador,tabuleiro):
            condicao = "O computador venceu"
            break

        if jogadas == 9 and not condicao in condicoes:
            condicao = "Deu Velha"

if modoDeJogo == 2:
    #p1 = jogador1 e p2 = jogador2
    jogador1 = str(input("Jogador 1, digite seu nome: "))
    jogador2 = str(input("Jogador 2, digite seu nome: "))
    p1 = int(input(f"\n{jogador1}, digite 1 para jogar com X, ou digite dois para jogar com O: "))
    if p1 == 1:
        p1 = "X"
        p2 = "O"
    elif p1 == 2:
        p1 = "O"
        p2 = "X"
    print(f"O {jogador1} escolheu {p1} e o {jogador2} fica com {p2}\n",flush=True)
    sleep(3)
    l()
    loading("Iniciando o jogo.")

    condicao = "continua"
    contador = 0
    condicoes = [str(f"{jogador1} venceu"), str(f"{jogador2} venceu")]
    while condicao == "continua":
        #jogador 1
        jogar(jogador1,p1,tabuleiro)
        jogadas += 1
        l()
        if checarPrincipal(p1,tabuleiro):
            condicao = str(f"{jogador1} venceu")
            break

        if jogadas == 9 and not condicao in condicoes:
            condicao = "Deu velha"
            break

        # jogador 2
        jogar(jogador2,p2, tabuleiro)
        jogadas += 1
        if checarPrincipal(p2,tabuleiro):
            condicao = str(f"{jogador2} venceu")
            break
        l()

        if jogadas == 9 and not condicao in condicoes:
            condicao = "Deu velha"
            break

mostrar(tabuleiro)
print(condicao)