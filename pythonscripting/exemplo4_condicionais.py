#estruturas condicionais
#entrada
nasc = int(input("Que ano você nasceu? "))
#processamento
idade = 2024 - nasc

fez_aniver = input("Fez aniversario esse ano?[s/n] ")
if fez_aniver == "n":
    idade = idade - 1

#saida
print(f"sua idade é: {idade}")