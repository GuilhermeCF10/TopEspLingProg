def opcao1():
    print("\n\nOpção 1\n\n")
    nome = str(input("Insira um nome: ")).capitalize()
    idade = int(input("Insira uma idade: "))
    salario = float(input("Insira um salário: "))
    sexo = str(input("Insira um sexo: ")).lower()
    estadoCivil = str(input("Insira um estado civil: ")).lower()

    # Nome maior que 3 caracteres
    while (len(nome) < 3):
        print("Você inseriu um nome inválido, insira um nome com pelo menos 4 caracteres")
        nome = str(input("Insira um nome: "))

    # Idade entre 0 e 130
    while (idade < 0 or idade > 130):
        print("Você inseriu uma idade inválida, insira uma idade entre 0 a 130")
        idade = int(input("Insira uma idade: "))

    # Salário maior que 0
    while (salario < 0):
        print("Você inseriu um salário inválido, insira um salário maior que 0")
        salario = float(input("Insira um salário: "))

    # Sexo diferente de m ou f não pode ser aceitado
    while (sexo != "m" and sexo != "f"):
        print("Você inseriu um sexo inválido, insira f feminimo, ou m masculino")
        sexo = str(input("Insira um sexo: "))

    # Estao civil Solteiro (s) Casado (c) Viuvo (v) Divorciado (d)
    while (estadoCivil != "s" and estadoCivil != "c" and estadoCivil != "v" and estadoCivil != "d"):
        print("Você inseriu um estado civil inválido, insira:")
        print("Solteiro (s) Casado (c) Viuvo (v) Divorciado (d)")
        estadoCivil = str(input("Insira um estado civil: ")).lower()
    
    #  Print Estado Civil
    if (estadoCivil == "s"):
        estadoCivil = "Solteiro"
    elif (estadoCivil == "c"):
        estadoCivil = "Casado"
    elif (estadoCivil == "v"):
        estadoCivil = "Viuvo"
    elif (estadoCivil == "d"):
        estadoCivil = "Divorciado"

    # Print Sexo
    if (sexo == "f"):
        sexo = "Feminino"
    elif (sexo == "m"):
        sexo = "Masculino"

    print(f"{nome} possui {idade} anos, tem o sexo {sexo} e é {estadoCivil}, possui o salário de R${salario:.2f} ")

def opcao2():
    print("\n\nOpção 2\n\n")
    string1 = str(input("Insira a primeira string: "))
    string2 = str(input("Insira a segunda string: "))

    print("\n\n")
    print(f"String 1: {string1} Tamanho: {len(string1)}")
    print(f"String 2: {string2} Tamanho: {len(string2)}")

    if (len(string1) == len(string2)):
        print("Possuem o mesmo comprimento")
    else: 
        print("Não possuem o mesmo comprimento")

    if (string1 == string2):
        print("As strings são iguais")
    else:
        print("As strings são diferentes")

def opcao3():
    print("\n\nOpção 3\n\n")
    nome = str(input("Insira um nome: "))

    for i in range(1, len(nome)+1):
        print(nome[-i].upper())

def opcao4():
    palavra = list(input("Insira uma palavra: ").lower())
    print(palavra)
    palindromo = True

    # Verificar se é palindromo
    for i in range(1, len(palavra)+1):

        if (palavra[i-1] == palavra[-i]):
            pass
            # É palindromo
            # print(f"Palavra: {palavra[i-1]} {palavra[-i]}")
        else:
            palindromo = False
            break

    if (palindromo):
        print("A palavra é palindromo")
    else:
        print("A palavra não é um palindromo")
        
print("Exercicio 2: ")
print("Professora: Silvia Campos")
print("\n")
while True:
    comando = int(input("\nInsira um comando: "))

    
    while (comando < 1 or comando > 4):
        print("Você inseriu um comando inválido")
        print("Insira opções de 1 a 4")
        comando = int(input("Insira um comando: "))

    print("\n\n")
    if (comando == 1):
        opcao1()
    elif (comando == 2):
        opcao2()
    elif (comando == 3):
        opcao3()
    elif (comando == 4):
        opcao4()
