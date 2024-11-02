# Definindo o dicionário de conversões e a lista de unidades
ano_luz = {
    "pc": 0.31,     # Parsec
    "al": 1,        # Ano-Luz
    "ae": 63241.09, # Unidade Astronômica
    "ml": 525960.23,# Minuto-Luz
    "sl": 31557609.92 # Segundo-Luz
}
unidades = ["Parsec (pc)", "Ano-Luz (al)", "Unidade Astronômica (ae)", "Minuto-Luz (ml)", "Segundo-Luz (sl)"]

# Função para exibir as unidades de conversão
def mostrar_unidades():
    print("Unidades de Conversão Disponíveis:")
    for unidade in unidades:
        print(f"- {unidade}")
    print()

# Função para realizar a conversão
def converter_unidades(valor, unidade_origem, unidade_destino):
    # Verifica se as unidades de origem e destino existem no dicionário
    if unidade_origem not in ano_luz or unidade_destino not in ano_luz:
        print("Unidade de origem ou destino inválida!")
        return
    
    # Converte o valor para anos-luz e depois para a unidade de destino
    valor_em_anos_luz = valor * ano_luz[unidade_origem]
    valor_convertido = valor_em_anos_luz / ano_luz[unidade_destino]
    
    # Exibe o resultado da conversão
    print(f"Conversão: {valor} {unidade_origem} = {valor_convertido:.4f} {unidade_destino}")

# Função principal do programa de conversão
def conversor_tempo():
    mostrar_unidades()
    
    try:
        valor = float(input("Valor a ser convertido: "))
    except ValueError:
        print("Erro: valor inválido. Digite um número.")
        return
    
    unidade_origem = input("Converter de (use a abreviação): ").strip().lower()
    unidade_destino = input("Converter para (use a abreviação): ").strip().lower()
    
    converter_unidades(valor, unidade_origem, unidade_destino)

# Executa o conversor
conversor_tempo()
