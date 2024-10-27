#3. Criar um jogo de par ou ímpar, onde dois jogadores entram com seu palpite (par ou
#ímpar) e seus valores de 1 a 5. Tomar por base os nomes: Jogador 1 e Jogador 2. Caso
#um dos valores esteja fora dos parâmetros informados, mostrar uma mensagem
#informando que esta rodada não valeu. Caso contrário, informa qual jogador ganhou esta
#rodada.
#ENTRADA
p1 = (input("Qual o palpite do jogador 1? (par/impar): "))
if p1 == "par":
    p2 = "impar"
    print(f"O jogador 2 será {p2}")
else:
    p2 = "par"
    print(f"O jogador 2 será {p2}")
j1 = int(input("Qual a mão do jogador 1? "))
j2 = int(input("Qual a mão do jogador 2? "))
if j1 > 5 or j2 > 5:
    print("Os jogadores devem escolher entre 1 e 5. Jogo encerrado")
    SystemExit

s = j1 + j2
if s % 2 == 0:
    r = "par"
else:
    r = "impar"
if r == p1:
    print(f"O resultado é {r} e o ganhador é o jogador 1!")
else:
    print(f"O resultado é {r} e o ganhador é o jogador 2!")
