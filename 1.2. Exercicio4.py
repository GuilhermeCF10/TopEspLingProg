intervaloInicial = 1000
intervaloFinal = 10000

valorA = 3
valorB = 4

quantidadePares = 0
quantidadeImpares = 0

for i in range(intervaloInicial, intervaloFinal + 1):

    # Verifica se é divisivel por 3 e 4 simultaneamnte
    if ( i % valorA == 0 and  i % valorB == 0 ):


        # Verifica se o numero é par

        if (i % 2 == 0):
            quantidadePares += 1
        else:
            quantidadeImpares += 1


print("*" * 20)
print("\nExercício 3")
print("\nQuantidade de pares e impares entre 1000 e 10000")

print(f"Pares: {quantidadePares}")
print(f"Impares: {quantidadeImpares}")
