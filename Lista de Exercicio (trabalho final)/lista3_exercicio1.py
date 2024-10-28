#1. Um determinado material radioativo perde metade de sua massa a cada 50 segundos.
#Dada a massa inicial, em gramas, fazer um algoritmo que determine o tempo necessário
#para que a massa se torne menor do que 0,5 grama. Imprima como dado de saída a massa
#final e o tempo calculado em segundos.
#ENTRADA
massa = float(input("Qual a massa inicial do material? >"))

cont = 0
segundos = 0
while massa > 0.5:
    massa = massa / 2
    cont += 1
segundos = cont * 50
print(f"Massa final = {massa} e tempo em segundos = {cont}")