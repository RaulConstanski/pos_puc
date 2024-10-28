#5. Dado um país A, com 5000000 de habitantes e uma taxa de natalidade de 3% ao ano,
#e um país B com 7000000 de habitantes e uma taxa de natalidade de 2% ao ano, escrever
#um programa em Python que seja capaz de calcular e iterativamente e no fim imprimir o
#tempo necessário para que a população do país A ultrapasse a população do país B.
#processamento
pais_a = 5000000.0
pais_b = 7000000.0
ano = 0
while pais_a < pais_b:
    pais_a = pais_a * (1 + 0.03)
    pais_b = pais_b * (1 + 0.02)
    ano += 1
#saida
print(f"A população do pais A irá ultrapassar a B em {ano} anos.")