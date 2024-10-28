#9. Elaborar um programa em Python que converta um número #decimal em hexadecimal,
#fazendo uso do método de divisões sucessivas.
# divisão inteira //
# resto %
# 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F

n = int(input("Digite um numero: "))
hexadecimal = "0123456789ABCDEF"
hexa = ""
while n > 0:
    resto = n % 16
    hexa = hexadecimal[resto] + hexa
    n = n // 16  

print(hexa)