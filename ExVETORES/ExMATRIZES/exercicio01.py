lista_de_compras = []

opcao = 1000

while opcao !=0:
    print('\n ========================')
    print('1 - adicionar novo item')
    print('2 - remover item')
    print('3 - exibir lista completa')
    print('0 - sair')

    opcao = int(input('Digite a opção desejada:'))


    if opcao == 1:
        print('\n====>ADICIONAR ITEM<====')
        novo_item = input('digite o novo item a ser adicionado:')
        lista_de_compras = lista_de_compras + novo_item

    elif opcao == 2: 
        print('\n====>REMOVER ITEM DA LISTA <====')
       
        for i in range(len(lista_de_compras)):
         print(f'{i+1} - {lista_de_compras[i]}')

        print('\n ===')

        item_remover = int(input('digite o codigo do item')) - 1

        del lista_de_compras[item_remover]

    elif opcao == 3:

        print('\n====>LISTA COMPLETA<====')

        for i in range(len(lista_de_compras)):
            print(f'{i+1} - {lista_de_compras[i]}')