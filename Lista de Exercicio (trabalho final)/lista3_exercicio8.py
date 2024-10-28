#8. Elaborar um programa que receba um número em binário, e #mostre o seu valor em
#decimal.

# ENTRADA
binario = str(input("Digite um número em binário: "))
posicao = 0
decimal = 0
# PROCESSAMETO
for i in range(len(binario)):
    posicao = len(binario) -1 -i
    decimal += int(binario[i]) * (2** posicao)

# Exibe o resultado
print(f"O valor em decimal é: {decimal}")
