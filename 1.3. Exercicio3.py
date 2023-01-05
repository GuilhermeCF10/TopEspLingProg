
import random

print("*" * 20)
print("\nExercício 3")
print("\nSorteio de um número de 1 a 100, e ver se usuário ganhou acertou o número sorteado")

num_escolhido = int(input("Escolha um número de 1 a 100: "))
numero_sorteado = random.randint(1, 100)

while (num_escolhido < 1 or num_escolhido > 100):
    print("\nVocê inseriu um número invalido, insira no intervalo correto!\n")
    num_escolhido = int(input("Escolha um número de 1 a 100: "))

print(f"Número sorteado: {numero_sorteado}")
print(f"Número escolhido: {num_escolhido}")

if (numero_sorteado == num_escolhido):
    print("Você venceu")
else:
    print("A banca sempre ganha!")