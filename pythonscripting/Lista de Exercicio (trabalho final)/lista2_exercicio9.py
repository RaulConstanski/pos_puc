#9. Implementar um programa que valide um CPF. Para tanto, solicitar em separado cada um dos 11 dígitos do CPF.
#O CPF é formado por 11 dígitos numéricos que seguem a máscara "###.###.###-##", a
#verificação do CPF acontece utilizando os 9 primeiros dígitos e, com um cálculo simples,
#verificando se o resultado corresponde aos dois últimos dígitos (depois do sinal "-"). Vamos usar como #exemplo, um CPF fictício "529.982.247-25". Validação do primeiro dígito Primeiramente multiplica-se os 9 #primeiros dígitos pela sequência decrescente de números de 10 à 2 e soma os resultados. Assim:
#5 * 10 + 2 * 9 + 9 * 8 + 9 * 7 + 8 * 6 + 2 * 5 + 2 * 4 + 4 * 3 + 7 * 2
#O resultado do nosso exemplo é: 295 O próximo passo da verificação também é simples, basta multiplicarmos esse #resultado por 10 e dividirmos por 11. 295 * 10 / 11
#O resultado que nos interessa na verdade é o RESTO da divisão. Se ele for igual ao primeiro dígito verificador #(primeiro dígito depois do '-'), a primeira parte da validação está correta. Observação Importante: Se o resto #da divisão for igual a 10, nós o consideramos como 0. O resultado da divisão acima é '268' e o RESTO é 2
#Isso significa que o nosso CPF exemplo passou na validação do primeiro dígito. Validação do segundo dígito
#A validação do segundo dígito é semelhante à primeira, porém vamos considerar os 9 primeiros dígitos, mais o #primeiro dígito verificador, e vamos multiplicar esses 10 números pela sequencia decrescente de 11 a 2. #Vejamos:
#5 * 11 + 2 * 10 + 9 * 9 + 9 * 8 + 8 * 7 + 2 * 6 + 2 * 5 + 4 * 4 + 7 * 3 + 2 * 2
#O resultado é:
#347
#Seguindo o mesmo processo da primeira verificação, multiplicamos por 10 e dividimos
#por 11.
#347 * 10 / 11
#Verificando o RESTO, como fizemos anteriormente, temos:
#O resultado da divisão é '315' e o RESTO é 5
#Verificamos, se o resto corresponde ao segundo dígito verificador.
#Com essa verificação, constatamos que o CPF 529.982.247-25 é válido.
#ENTRADA
n1 = int(input("Digite o 1° número do seu CPF: "))
n2 = int(input("Digite o 2° número do seu CPF: "))
n3 = int(input("Digite o 3° número do seu CPF: "))
n4 = int(input("Digite o 4° número do seu CPF: "))
n5 = int(input("Digite o 5° número do seu CPF: "))
n6 = int(input("Digite o 6° número do seu CPF: "))
n7 = int(input("Digite o 7° número do seu CPF: "))
n8 = int(input("Digite o 8° número do seu CPF: "))
n9 = int(input("Digite o 9° número do seu CPF: "))
n10 = int(input("Digite o 10° número do seu CPF: "))
n11 = int(input("Digite o 11° número do seu CPF: "))
#PROCESSAMENTO
#1ª MULTIPLICAÇÃO SEQUENCIAL
seq1 = n1 * 10 + n2 * 9 + n3 * 8 + n4 * 7 + n5 * 6 + n6 * 5 + n7 * 4 + n8 * 3 + n9 * 2
#resultado por 10 e dividirmos por 11. 295 * 10 / 11
rest1 = (seq1 * 10) % 11
#2ª MULTIPLICAÇÃO SEQUENCIAL
seq2 = n1 * 11 + n2 * 10 + n3 * 9 + n4 * 8 + n5 * 7 + n6 * 6 + n7 * 5 + n8 * 4 + n9 * 3 + n10 * 2
rest2 = (seq2 *10) % 11
if rest1 == n10 and rest2 == n11:
    print("CPF válido.")
else:
    print("CPF válido.")