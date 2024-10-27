# Entrada
nome_produto = input("Digite o nome do seu produto: ")
preco = float( input("Digite o preço do produto: ") )
quantidade = int( input("Digite a quantidade: ") )
 
# Processamento
frete = 0
subtotal = preco * quantidade

#se o total dos produtos for menor que 100 reais adicione 30 reais de frete
if subtotal < 100:
    frete = 30
# Saída
print("Produto: ", nome_produto)
print(f"Preço R$ {preco:10.2f}")
print("Quantidade: ", quantidade)
print("frete: R$ ", frete)
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Total: R$ {subtotal+frete:.2f}")