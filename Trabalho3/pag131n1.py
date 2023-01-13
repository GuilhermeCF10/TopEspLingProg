# Crie um programa para gerenciar uma pilha de processos em Python. 
# Cada processo possui um identificador (número) e uma descrição (string). 
# Você deverá pedir ao usuário para escolher se deseja encerrar, 
# incluir ou retirar um processo da pilha. Se a operação for uma 
# inclusão, colocar o processo na pilha e imprimir o novo estado 
# dessa; se for uma exclusão, caso a pilha não esteja vazia,
# imprimir “removido o processo #identificador — descrição da pilha” 
# e mostrar o conteúdo atual dela; se a pilha estiver vazia, 
# mostrar “pilha vazia”. Se o usuário escolher encerrar, 
# esvazie a pilha (caso ainda existam elementos nela) e 
# encerre o programa.
processos = []

while(True):
    print("Opcão 1 - Adicionar processo")
    print("Opcão 2 - Retirar processo")
    print("Opcão 3 - Encerrar processos")
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
        processos.pop()
        print(processos)
    elif(op == 3):
       exit()
