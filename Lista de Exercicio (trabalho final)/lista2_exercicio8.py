#8. Implemente um programa que solicite uma data com hora, pedindo em separado: dia,
#mês, ano, hora, minuto e segundo. Pergunte ao usuário que informação ele deseja
#acrescentar, e em qual quantidade. Informar a nova data de acordo com o solicitado pelo
#usuário.
#Ex.: Informada a data 31/12/2001 23:59:59, se o usuário pedir para acrescentar um
#segundo a data deve ser exibida como 01/01/2002 00:00:00.
#Para determinar se um ano é bissexto, execute estas etapas:
#1. Se o ano for uniformemente divisível por 4, vá para a etapa 2. Caso contrário, vá
#para a etapa 5.
#2. Se o ano for uniformemente divisível por 100, vá para a etapa 3. Caso contrário,
#vá para a etapa 4.
#3. Se o ano for uniformemente divisível por 400, vá para a etapa 4. Caso contrário,
#vá para a etapa 5.
#4. O ano é bissexto (tem 366 dias).
#5. O ano não é um ano bissexto (tem 365 dias).
#ENTRADA
# Solicita a data inicial do usuário
dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano: "))
hora = int(input("Informe a hora: "))
minuto = int(input("Informe o minuto: "))
segundo = int(input("Informe o segundo: "))

# Solicita a informação a ser adicionada
quantidade = int(input("Informe a quantidade a acrescentar: "))
tipo = input("Informe o tipo (segundo, minuto, hora, dia, mes, ano): ")

#PROCESSAMENTO
# Verifica se o ano é bissexto
# Solicita a data inicial do usuário
dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano: "))
hora = int(input("Informe a hora: "))
minuto = int(input("Informe o minuto: "))
segundo = int(input("Informe o segundo: "))

# Solicita a informação a ser adicionada
quantidade = int(input("Informe a quantidade a acrescentar: "))
tipo = input("Informe o tipo (segundo, minuto, hora, dia, mes, ano): ")

# Verifica se o ano é bissexto
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    bissexto = True
else:
    bissexto = False

# Calcula o número de dias no mês atual
if mes in [4, 6, 9, 11]:
    dias_no_mes = 30
elif mes == 2:
    dias_no_mes = 29 if bissexto else 28
else:
    dias_no_mes = 31

# Ajusta com base no tipo e quantidade
if tipo == 'segundo':
    segundo += quantidade
    minuto += segundo // 60
    segundo = segundo % 60

if tipo == 'minuto':
    minuto += quantidade
    hora += minuto // 60
    minuto = minuto % 60

if tipo == 'hora':
    hora += quantidade
    dia += hora // 24
    hora = hora % 24

if tipo == 'dia':
    dia += quantidade

if dia > dias_no_mes:
    mes += (dia - 1) // dias_no_mes
    dia = (dia - 1) % dias_no_mes + 1
    if mes > 12:
        ano += (mes - 1) // 12
        mes = (mes - 1) % 12 + 1

if tipo == 'mes':
    mes += quantidade
    ano += (mes - 1) // 12
    mes = (mes - 1) % 12 + 1

if tipo == 'ano':
    ano += quantidade

# Exibe a nova data
print(f"Nova data: {dia:02}/{mes:02}/{ano} {hora:02}:{minuto:02}:{segundo:02}")
