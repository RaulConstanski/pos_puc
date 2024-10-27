# Fazer um programa que leia 5 inteiros
# Calcule a média deles
# e mostre os maiores e os menores que a média
 
numeros = []
soma = 0
 
# Leitura dos números
for i in range(1, 6):
    numero = int(input("Digite um número inteiro: "))
    soma += numero
    # numeros[0] = numero <-- ERRO
    numeros.append(numero)
 
# Calcular a média
media = soma / len(numeros)
print("Média:", media)
 
print("Maiores que a média: ")
for numero in numeros:
    if numero > media:
        print(numero, end = " ")
 
print("\n\nMenores que a média: ")
for numero in numeros:
    if numero < media:
        print(numero, end = " ")