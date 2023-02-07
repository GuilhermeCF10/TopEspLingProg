# Forca
import random
import copy



words = [ ["c","a","s","a"], ["e", "s", "t", "o", "j", "o"], ["v", "a", "c", "a"]]
numeroaleatorio = random.randint(0, len(words)-1)
word = words[numeroaleatorio]
tentativas = []

def showWord():
    show = copy.deepcopy(word)

    acertos = 0

    for i in range(len(show)):
        if (show[i] not in tentativas):
            show[i] = "_"
        else:
            acertos += 1
    print(f"Você acertou {acertos} letras")

    for cadaLetra in show:
        print(f" {cadaLetra}", end="")
    print("\n\n")

    if ("_" not in show):
        print("\nParabéns você venceu!")
        return False
    else:
        return True

def digitWord():
    digito = str(input("Digite uma letra: "))

    while (len(digito) > 1):
        print("Você precisa inserir apenas uma letra!")
        digito = str(input("Digite uma letra: "))

    tentativas.append(digito)

vidas = 6
continuar = True
while (continuar):
    if (vidas == 0):
        print("Você perdeu!")
        continuar = False
        break


    game = showWord()
    
    if (game):
        digitWord()
        print(f"Você possui {vidas-1} vidas!")
        vidas -= 1
    else:
        vidas = 0