#6. Implemente um programa para calcular as raízes de uma equação do 2º grau, sendo que
#os valores dos coeficientes A, B, e C devem ser fornecidos pelo usuário, e os valores das
#raízes devem ser calculadas pela fórmula de Bhaskara, como segue:
#𝑥 = (-b±√b²-4ac)/2a
#ENTRADA
a = float(input("Qual o coeficiente A: "))
b = float(input("Qual o coeficiente B: "))
c = float(input("Qual o coeficiente C: "))
#PROCESSAMENTO
delta = b**2 - ( 4 * a * c)
if delta < 0:
    print(f"Delta {delta:.2f} é negativo, portanto não há solução real.")
    SystemExit
else:
    raizd = delta ** (1/2)
    x1 = (-b + raizd) /  2 * a
    x2 = (-b - raizd) /  2 * a 
    print(f"Delta = {delta:.2f}")
    print(f"Raiz do delta = {raizd:.2f}")
    print(f"X1 = {x1:.2f}")
    print(f"X2 = {x2:.2f}")
