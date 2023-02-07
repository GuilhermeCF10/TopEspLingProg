import random

print("*" * 20)
print("Jogo de dados")


userA = str(input("Insira o nome do usuário 1: "))
dado_userA = random.randint(1, 6)

userB = str(input("Insira o nome do usuário 2: "))
dado_userB = random.randint(1, 6)


print("\nResultado dos dados:")
print(f"Usuário: {userA} Dado: {dado_userA}")
print(f"Usuário: {userB} Dado: {dado_userB}")

if (dado_userA > dado_userB):
    print(f"O usuário 1: {userA} venceu")
elif (dado_userA == dado_userB):
    print("Empate nos dados")
else:
    print(f"O usuário 2: {userB} venceu")