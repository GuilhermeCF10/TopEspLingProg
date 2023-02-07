# Faça um programa que solicita ao usuário sua data de nascimento e, 
# em seguida, em um loop, pede as datas de admissão e demissão de 
# todos os empregos ocupados por ele. Em seguida, calcula quantos 
# dias o usuário já trabalhou desde o início da sua carreira.

from datetime import date, timedelta
import math


def CalculaQuantidadeDeDiasTrabalhados():
    empregos = []

    nomeUser = input("Digite seu nome: ")

    print("\n\nEx: dd/mm/yyyy")
    dataNasc = input("Digite data do seu nascimento: ").split("/")

    diaNasc = int(dataNasc[0])
    mesNasc = int(dataNasc[1])
    anoNasc = int(dataNasc[2])

    dataNasc = date(anoNasc,mesNasc,diaNasc)

    trabalhos = int(input("\nDigite quantos trabalhos você na sua vida: "))

    for i in range(trabalhos):
        print("\n\n")
        empresa = input("Digite o nome da empresa: ")

        print("\n\nEx: dd/mm/yyyy")
        dataAdmissao = input("Digite data da sua admissão: ").split("/")
        diaA = int(dataAdmissao[0])
        mesA = int(dataAdmissao[1])
        anoA = int(dataAdmissao[2])
        admissao = date(anoA, mesA, diaA)

        print("\n\nEx: dd/mm/yyyy")
        dataDemissao = input("Digite data da sua demissão: ").split("/")
        diaD = int(dataDemissao[0])
        mesD = int(dataDemissao[1])
        anoD = int(dataDemissao[2])
        demissao = date(anoD, mesD, diaD)

        empregos.append({
            'empresa': empresa,
            'admissao': admissao,
            'demissao': demissao,
        })

    tot = timedelta(days=0)

    for cadaEmprego in empregos:
        # Adiciona quantidade de trabalho
        tot += cadaEmprego["demissao"] - cadaEmprego["admissao"]

    print(f"\n\nParabéns, {nomeUser}, você trabalhou por {math.ceil(tot.days / 365)} anos !")

    return { 'dataNasc': dataNasc, 'diasTrabalhados': tot.days }