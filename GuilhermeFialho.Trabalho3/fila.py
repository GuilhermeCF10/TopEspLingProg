def cleanScreen():
    print('\n'*200) 

def addClient():
    print('\n'*200)

    name = input('Digite o nome do cliente: ')
    registration = input('Digite o RG do cliente: ')

    cliente = {
    'nome': name,
    'rg': registration
    }
    return cliente

def listClients(fila):
    if len(fila) > 0:
        print('\n'*200) 
        for indice in range(0,len(fila)):
            print(f"{indice + 1} - {fila[indice]['rg']} - {fila[indice]['nome']}")
            input('Tecle <enter> para retornar ao menu...')
    else:
        print('Fila vazia!')
        input('Tecle <enter> para retornar ao menu...')


def getClient(fila):
    if len(fila) > 0:
        print('\n'*200)

        cliente = fila.pop(0)
        tamanhoFila = len(fila)

        print(f"Atendendo o cliente: {cliente['nome']} - RG: {cliente['rg']}")
        print(f'Restam {tamanhoFila} clientes na fila.')
        input('Tecle <enter> para retornar ao menu...')
    else:
        print('Fila vazia!')
        input('Tecle <enter> para retornar ao menu...')
    return fila
