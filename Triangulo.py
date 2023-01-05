
import math
quantidadeLados = 3

lados = ["A", "B", "C"]

x=[]
y=[]
z=[]

for i in range(quantidadeLados):
    print(f"\nInsira os valores do lado {lados[i]} ")
    x.append(float(input("Insira a coordenada em X: ")))
    y.append(float(input("Insira a coordenada em Y: ")))
    z.append(float(input("Insira a coordenada em Z: ")))


distanciaLados = []

AB = math.sqrt(math.pow((x[1] - x[0]),2) +  math.pow((y[1]-y[0]),2) + math.pow((z[1]-z[0]),2))
AC = math.sqrt(math.pow((x[0] - x[-1]),2) +  math.pow((y[0]-y[-1]),2) + math.pow((z[0]-z[-1]),2))
BC = math.sqrt(math.pow((x[1] - x[-1]),2) +  math.pow((y[1]-y[-1]),2) + math.pow((z[1]-z[-1]),2))

print(f"\nAB: {AB}")
print(f"AC: {AC}")
print(f"BC: {BC}")
print("\n")

print(f"AB > AC+BC: {AB,AC+BC}")
print(f"BC > AC+AB: {BC, AC+AB}")
print(f"AC > AB+BC: {AC, AB+BC}")

if ( AB >= AC+BC or BC >= AC+AB or AC >= AB+BC):
    print("Não é um triangulo")
else: 
    print("É um triangulo")

# Insira os valores do lado A 
# Insira a coordenada em X: 1
# Insira a coordenada em Y: 2
# Insira a coordenada em Z: 3

# Insira os valores do lado B 
# Insira a coordenada em X: 1
# Insira a coordenada em Y: 3
# Insira a coordenada em Z: 6

# Insira os valores do lado C 
# Insira a coordenada em X: 3
# Insira a coordenada em Y: 4
# Insira a coordenada em Z: 3