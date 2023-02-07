# Considere que um homem possa se aposentar aos 65 anos de idade 
# e 35 de contribuição à previdência, e uma mulher, 62/30. 
# Elabore um programa que solicite os dados do gênero do(a) 
# usuário(a), sua data de nascimento, as datas de início e 
# fim de cada emprego ocupado, e informe quanto tempo falta 
# para essa pessoa se aposentar.
from datetime import datetime, date
import math
from pag142n1 import CalculaQuantidadeDeDiasTrabalhados


main = CalculaQuantidadeDeDiasTrabalhados()

print("\n\nQual seu sexo?")
sexo = input("Insira f para feminino e m para masculino: ")

while (sexo != "f" and sexo != "m"):
    print("Você digitou um sexo inválido")
    print("Qual seu sexo?")
    sexo = input("Insira f para feminino e m para masculino: ")


# Precisa ter 65 anos e 35 de contribuição (35 trabalho)
today = datetime.today().strftime("%Y/%m/%d").split("/")
todayDate = date(int(today[0]), int(today[1]), int(today[2]))

retireByAge = (todayDate - main["dataNasc"])
retireByAge = math.ceil(round(retireByAge.days / 365, 2))
daysWorking = math.ceil(round((main["diasTrabalhados"]) / 365, 2))

if (sexo == "m"): # Male
    if (retireByAge >= 65 and daysWorking >= 35):
        print("\n\nParabéns você está aposentado!")
        print(f"Trabalhou por {daysWorking} anos e hoje tem {retireByAge} anos de vida!")
    else:
        print("\n\nVocê ainda precisa trabalhar um pouco mais!")
        print(f"Você ainda possui {daysWorking} anos de trabalho e hoje tem {retireByAge} anos de vida")
        print(f"Falta {35 - daysWorking} anos de trabalho e {65 - retireByAge} anos de vida para você se aposentar!")

else: # Women
    if (retireByAge >= 62 and daysWorking >= 30):
        print("\n\nParabéns você está aposentada!")
        print(f"Trabalhou por {daysWorking} anos e hoje tem {retireByAge} anos de vida!")
    else:
        print("\n\nVocê ainda precisa trabalhar um pouco mais!")
        print(f"Você ainda possui {daysWorking} anos de trabalho e hoje tem {retireByAge} anos de vida")
        print(f"Falta {30 - daysWorking} anos de trabalho e {62 - retireByAge} anos de vida para você se aposentar!")