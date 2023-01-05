# Escreva um programa que solicita as dimensões (largura e comprimento) de uma sala em metros,
#  o tamanho da aresta de uma peça quadrada de cerâmica em cm e imprima quantas peças devem ser adquiridas para pavimentar a referida sala.
#  Observe que o número deve ser inteiro — se você obtiver um valor fracionário para a resposta, arredonde-o para o inteiro imediatamente superior.

import math

largura = float(input("Insira a largura da sala (em metros): "))
comprimento = float(input("Insira o comprimento da sala (em metros): "))

print("\n")
larguraPiso = float(input("Insira a largura do piso (em centimetros): "))/100
comprimentoPiso = float(input("Insira o comprimento do piso (em centimetros): "))/100


areaSala = largura * comprimento
areaPiso = larguraPiso * comprimentoPiso

qntdPisos = areaSala / areaPiso

print("\n")
print(f"Como a quantidade de pisos seria {round(qntdPisos, 2)}, você deve comprar {math.ceil(qntdPisos)} pisos")