# Exercicio 3

print("*" * 20)
print("\nExercício 1")
print("\tInsira 3 números para verificar a medinaa e média simples dos 3")

numeros = []
media = 0

for i in range(0, 3):
    num = int(input("Insira um número: "))
    numeros.append(num)
    media += num

numeros.sort()
media = media / len(numeros)




print(f"A média simples dos três números é: {media}")
print(f"A mediana dos três números é: {numeros[1]}")

print("\nExercício finalizado")