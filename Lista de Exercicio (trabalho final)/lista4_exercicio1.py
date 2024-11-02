#- Imprimir o cardápio do restaurante com as opções de produtos ofertados;
#- Logo abaixo do cardápio, exibir a mensagem “O que deseja pedir (0 para sair)?”;
#- Digitando “0” deve sair do programa;
#- Digitando o nome do produto pode ter uma das seguintes possibilidades:
#- Se o item não consta no cardápio exibir a mensagem “Item não localizado no
#cardápio”;
#- Se não tiver os ingredientes para o preparo do produto em estoque mostrar uma
#mensagem para cada ingrediente faltante “Infelizmente acabou o {ingrediente}”;
#- Se for possível produzir o produto, reduzir as quantidades de estoque e mostrar a
#mensagem “um {produto} saindo no capricho!!!”;
#- O programa deve continuar fazendo os pedidos até que o usuário decida sair do
#mesmo.
# Definindo o estoque e o cardápio
estoque = {'pao': 10, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5}
cardapio = {
    'x-burguer': ['pao', 'hamburguer'],
    'x-salada': ['pao', 'hamburguer', 'tomate'],
    'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
    'x-egg': ['pao', 'hamburguer', 'ovo'],
    'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}

# Função para exibir o cardápio
def mostrar_cardapio():
    print("Cardápio do Restaurante:")
    for item in cardapio:
        print(f"- {item}")
    print("O que deseja pedir? (Digite 0 para sair)")

# Função para verificar a disponibilidade e preparar o pedido
def fazer_pedido(pedido):
    if pedido not in cardapio:
        print("nItem não localizado no cardápio.")
        return
    
    ingredientes = cardapio[pedido]
    falta_ingredientes = []
    
    # Verificando se todos os ingredientes estão disponíveis no estoque
    for ingrediente in ingredientes:
        if estoque.get(ingrediente, 0) < ingredientes.count(ingrediente):
            falta_ingredientes.append(ingrediente)
    
    # Exibindo mensagens de ingredientes faltantes ou preparando o pedido
    if falta_ingredientes:
        for ingrediente in set(falta_ingredientes):
            print(f"Infelizmente acabou o {ingrediente}\n\n")
    else:
        for ingrediente in ingredientes:
            estoque[ingrediente] -= 1
        print(f"Um {pedido} saindo no capricho!!!\n\n")

# Loop principal do sistema de pedidos
def sistema_pedidos():
    while True:
        mostrar_cardapio()
        pedido = input("Digite o nome do produto: ").strip().lower()
        
        if pedido == "0":
            print("Saindo do sistema de pedidos...")
            break
        
        fazer_pedido(pedido)

# Executando o sistema de pedidos
sistema_pedidos()
