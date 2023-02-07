# Você lembra do Exercício resolvido 2 do Capítulo 7, no qual 
# demonstrei como criar uma fila usando a classe List? 
# Refaça o exercício, desta vez criando funções para limpar 
# a tela, verificar se a fila está vazia, incluir um cliente 
# na fila e atender a um cliente. Deixe o loop principal do 
# programa em um arquivo separado das funções que controlam 
# a fila. Salve as funções da fila em um módulo chamado fila.py. 
# Esse módulo implementa um TAD (Tipo Abstrato de Dados) fila.

from fila import cleanScreen,addClient,listClients,getClient

#limpar a tela, 
# verificar se a fila está vazia, 
# incluir um cliente na fila e 
# atender a um cliente. 
# finalizar

fila = []
quantidade_clientes = 0
while True:
    opcao = ''
    print('\n'*200) #Limpar a tela
    print('Menu do Sistema')
    print('1. Incluir clientes a fila')
    print('2. Listar pessoas na fila')
    print('3. Atender o próximo cliente')
    print('4. Limpar tela')
    print('5. Sair do programa')

    opcao = int(input('Sua escolha -> '))

    if opcao == 1:
        quantidade_cliente = quantidade_clientes + 1
        cliente = addClient()
        fila.append(cliente)
    
    elif opcao == 2:
        listClients(fila)

    elif opcao == 3:
        novaFila = getClient(fila)
        fila = novaFila

    elif opcao == 4:
        cleanScreen()
        
    elif opcao == 5:
        break

print('Você finalizou o programa.')
