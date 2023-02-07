frase = list(input("Digite uma frase:"))

espacos = 0
vogais = 0

print(frase)
for cadaItem in frase:
    if (cadaItem == " "):
        espacos += 1
    else: 
        vogais += 1

print(f"Nesta frase possui: {vogais} vogais e {espacos} espaços!")