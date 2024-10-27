# Dada uma lista contendo a precipitação e a temperatura média de cada
# um dos meses de um ano,
# Mostrar quais meses foram quentes (> 25) e
# quais meses foram secos (< 10)
matriz_mes_prec_temp = [["jan",100,20],["Fev",400,18],["Mar",420,15],["Abr",100,21],["Mai",80,25],["jun",50,27],["jul",200,30],["ago",190,32],["set",150,30],["out",120,30],["nov",95,31],["dez",70,33]]

for i in range(0,12):
    if matriz_mes_prec_temp[3] >
print

--
# dados de temperatura e precipitação dos meses
dados_mensais = [
    ("Janeiro", 28, 5),
    ("Fevereiro", 30, 12),
    ("Março", 22, 20),
    ("Abril", 26, 8),
    ("Maio", 24, 15),
    ("Junho", 27, 3),
    ("Julho", 25, 9),
    ("Agosto", 29, 2),
    ("Setembro", 23, 11),
    ("Outubro", 31, 1),
    ("Novembro", 26, 4),
    ("Dezembro", 29, 0),
]
 
meses_quentes = [mes for mes, temp, _ in dados_mensais if temp > 25]
meses_secos = [mes for mes, _, precip in dados_mensais if precip < 10]
 
print("Meses quentes (> 25 graus):", meses_quentes)
print("Meses secos (< 10 mm de precipitação):", meses_secos)