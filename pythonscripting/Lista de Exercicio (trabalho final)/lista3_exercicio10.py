#inconpleto
#10. Solicitar ao usuário duas datas e calcular a quantidade de dias entre elas (levar em
#consideração os anos bissextos).
# com def de funcao
def dias_do_mes(ano, mes):
# Verifica se o ano é bissexto
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        bissexto = True
    else:
        bissexto = False

# Calcula o número de dias no mês atual
    if mes in [4, 6, 9, 11]:  # Abril, Junho, Setembro, Novembro
        dias_no_mes = 30
    elif mes == 2:  # Fevereiro
        dias_no_mes = 29 if bissexto else 28
    else:  # Meses com 31 dias
        dias_no_mes = 31

    return dias_no_mes

# Função para calcular a quantidade de dias desde o início (01/01/0000) até uma data específica
def calcular_dias(dia, mes, ano):
    dias_totais = 0

# Adicionar dias de anos completos até o ano anterior
    for a in range(0, ano):
        dias_totais += 366 if (a % 4 == 0 and (a % 100 != 0 or a % 400 == 0)) else 365

# Adicionar dias de meses completos no ano atual
    for m in range(1, mes):
        dias_totais += dias_do_mes(ano, m)

# Adicionar dias do mês atual
    dias_totais += dia

    return dias_totais

dia1 = int(input("Digite o dia da primeira data: "))
mes1 = int(input("Digite o mês da primeira data: "))
ano1 = int(input("Digite o ano da primeira data: "))
if 1 <= mes1 <= 12 and 1 <= dia1 <= dias_do_mes(ano1, mes1):
    dia2 = int(input("Digite o dia da segunda data: "))
    mes2 = int(input("Digite o mês da segunda data: "))
    ano2 = int(input("Digite o ano da segunda data: "))
    diferenca_dias = abs(calcular_dias(dia2, mes2, ano2) - calcular_dias(dia1, mes1, ano1))
    print(f"\nA quantidade de dias entre as duas datas é: {diferenca_dias} dias.")
else:
    print("Data inválida. Verifique o dia e o mês.")

