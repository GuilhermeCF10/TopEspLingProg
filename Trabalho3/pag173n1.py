# Você lembra do Exercício resolvido 2 do Capítulo 7, no qual 
# demonstrei como criar uma fila usando a classe List? 
# Refaça o exercício, desta vez criando funções para limpar 
# a tela, verificar se a fila está vazia, incluir um cliente 
# na fila e atender a um cliente. Deixe o loop principal do 
# programa em um arquivo separado das funções que controlam 
# a fila. Salve as funções da fila em um módulo chamado fila.py. 
# Esse módulo implementa um TAD (Tipo Abstrato de Dados) fila.

processos = []

while(True):
    print("Opcão 1 - Adicionar processo")
    print("Opcão 2 - Retirar processo")
    print("Opcão 3 - Retirar todos os processos")
    print("Opção 4 - Encerrar processos")
    print()
    op = int(input("Digite a opção: "))
    if(op == 1):
        processo = input("Digite a descrição do processo: ")
        processos.append({
            'identificador': len(processos)+1, 
            'descrição': processo
        })
        print()
        print(processos)
        print()
    elif(op == 2):
        processos.pop(0)
        print(processos)
    elif(op == 3):
       processos = []
       print("\nLista limpa com sucesso!\n")
    elif (op == 4):
        exit()