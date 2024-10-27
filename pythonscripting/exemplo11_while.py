nota1 = 0

while True:
    nota1 = float(input("Digite uma nota: "))
    if nota1 >= 0 and nota1 <= 10:
        break
    else:
        print("Digite uma nota de 0 a 10")
print("Nota válida")