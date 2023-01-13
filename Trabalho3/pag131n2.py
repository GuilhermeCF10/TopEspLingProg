# Uma pista de Kart permite 10 voltas para cada um de 6 corredores. 
# Escreva um programa que leia todos os tempos em segundos e os 
# guarde em um dicionário, em que a chave é o nome do corredor. 
# Ao final, diga de quem foi a melhor volta da prova, em que 
# volta e mostre o nome e os tempos do campeão, que é o que tem 
# a menor média de tempos.

corredores = []
tempos = []

for i in range(6):
    nome = input('Digite o nome do corredor: ')
    tempo = int(input('Digite o tempo do corredor em segundos: '))
    corredores.append(nome)
    tempos.append(tempo)


menorTempo = min(tempos)
corredor = corredores[tempos.index(menorTempo)]

print(f"O corredor mais rápido foi o {corredor} com o tempo de {menorTempo} segundos!")
