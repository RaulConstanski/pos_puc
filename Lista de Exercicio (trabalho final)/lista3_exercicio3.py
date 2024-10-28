#3. Criar um jogo de pedra, papel, tesoura entre dois jogadores. Antes de começar o jogo,
#porém, deve ser escolhido a quantidade de pontos a serem feitos para vencer.
pontosfinal = int(input("O jogo vai até quantos pontos: >"))
pontosj1 = 0
pontosj2 = 0
while pontosj1 < pontosfinal and pontosj2 < pontosfinal:
    mao1 = input("Escolha jogador 1? [pedra, papel, tesoura] >")
    mao2 = input("Escolha jogador 2? [pedra, papel, tesoura] >")
    if mao1 == mao2:
        print("Empate, niguém pontua.")
    elif mao1 == "pedra" and mao2 == "tesoura" or mao1 == "papel" and mao2 == "pedra" or mao1 == "tesoura" and mao2 == "papel":
        pontosj1 += 1
        print(f"Jogador 1 ganhou 1 ponto. Resultado atual: J1 ={pontosj1} X J2 ={pontosj2}")
    else:
         pontosj2 += 1
         print(f"Jogador 2 ganhou 1 ponto. Resultado atual: J1 ={pontosj1} X J2 ={pontosj2}")
if pontosj1 == pontosfinal:
    print("Jogador 1 venceu!")
else:
    print("Jogador 2 venceu!")
