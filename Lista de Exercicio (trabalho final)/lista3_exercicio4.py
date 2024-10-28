#Peça 5 números ao usuário. Fazendo uso de laços, organize e mostre eles em ordem
#crescente.
#ENTRADA
n1 = input("Digite o primeiro número: ")
n2 = input("Digite o segundo número: ")
n3 = input("Digite o terceiro número: ")
n4 = input("Digite o quarto número: ")
n5 = input("Digite o quinto número: ")

ordenar = True
while ordenar == True:
    ordenar = False
    if n1 > n2:
        ntemp = n1
        n1 = n2
        n2 = ntemp
        ordenar = True
    if n2 > n3:
        ntemp = n2
        n2 = n3
        n3 = ntemp
        ordenar = True
    if n3 > n4:
        ntemp = n3
        n3 = n4
        n4 = ntemp
        ordenar = True
    if n4 > n5:
        ntemp = n4
        n4 = n5
        n5 = ntemp
        ordenar = True
print("Números em ordem crescente:", n1, n2, n3, n4, n5)