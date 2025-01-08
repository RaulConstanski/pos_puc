# Função para verificar se o ano é bissexto
def is_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            return False
        return True
    return False

# Função para calcular o número de dias em um mês
def dias_no_mes(mes, ano):
    if mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        if is_bissexto(ano):
            return 29
        return 28
    else:
        return 31

# Função para incrementar a data
def adicionar_tempo(dia, mes, ano, hora, minuto, segundo, quantidade, tipo):
    if tipo == 'segundo':
        segundo += quantidade
    elif tipo == 'minuto':
        minuto += quantidade
    elif tipo == 'hora':
        hora += quantidade
    elif tipo == 'dia':
        dia += quantidade
    elif tipo == 'mes':
        mes += quantidade
    elif tipo == 'ano':
        ano += quantidade

    # Ajusta os segundos
    if segundo >= 60:
        minuto += segundo // 60
        segundo = segundo % 60

    # Ajusta os minutos
    if minuto >= 60:
        hora += minuto // 60
        minuto = minuto % 60

    # Ajusta as horas
    if hora >= 24:
        dia += hora // 24
        hora = hora % 24

    # Ajusta os dias e meses
    while dia > dias_no_mes(mes, ano):
        dia -= dias_no_mes(mes, ano)
        mes += 1
        if mes > 12:
            mes = 1
            ano += 1

    return dia, mes, ano, hora, minuto, segundo

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

# Calcula a nova data
novo_dia, novo_mes, novo_ano, nova_hora, novo_minuto, novo_segundo = adicionar_tempo(
    dia, mes, ano, hora, minuto, segundo, quantidade, tipo
)

# Exibe a nova data
print(f"Nova data: {novo_dia:02}/{novo_mes:02}/{novo_ano} {nova_hora:02}:{novo_minuto:02}:{novo_segundo:02}")
