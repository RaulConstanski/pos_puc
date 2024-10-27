#2. O IMC – Índice de Massa Corporal é um critério da Organização Mundial de Saúde
#para dar uma indicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC
#= peso / altura2. Implemente um programa que leia o peso e a altura de um adulto e mostre
#sua condição de acordo com a tabela abaixo.
#IMC em adultos Condição
#• Abaixo de 18,5 – Abaixo do peso
#• Entre 18,5 e 25 – Peso normal
#• Entre 25 e 30 – Acima do peso
#• Acima de 30 – Obeso
#ENTRADA
p = float(input("Qual seu peso? (em KG) "))
a = int(input("Qual é sua altura? (em cm) "))
a = a/100
#PROCESSAMENTO
imc = p / (a ** a)
if imc <= 18.5:
    rimc = "Abaixo do peso"
elif imc <= 25:
    rimc = "Peso normal"
elif imc <= 30:
    rimc = "Acima do peso"
else:
    rimc = "Obeso"

print(f"Seu IMC é: {rimc} no valor de", imc)