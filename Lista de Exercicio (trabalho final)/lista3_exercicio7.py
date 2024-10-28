#7. Elaborar um programa que solicita várias palavras ao usuário, sendo que o critério de
#parada é digitar uma palavra vazia. Contar e exibir quantas letras A existem neste
#conjunto de palavras.
#
conta = 0
palavra = " "
while palavra != "":
    palavra = input("Digite uma palavra: [vazio para terminar] > ")
    for i in palavra:
        if i == "a":
            conta += 1
print(conta)