#2. Escreva um programa em Python que gera números entre 1000 e 1999 e mostra aqueles
#que divididos por 11 dão resto 5.
n1 = 1000

while  n1 <= 1999:
    if n1 % 11 == 5:
        print(F"Resto de {n1} é igual a 5.")
    n1 += 1
