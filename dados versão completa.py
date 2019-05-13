from random import randint
print("Vai!!!")

dado1 = randint (1,6)
print("dado 1 :", dado1)

dado2 = randint(1,6)
print("dado 2 :",dado2)

dado3 = randint (1,6)
print("dado 3 :",dado3)

dado4 = randint(1,6)
print("dado 4 :",dado4)

jogador1 = dado1 + dado2
jogador2 = dado4 + dado3

print("JOGADOR 1:" jogador1 )
print("JOGADOR 2:",jogador2 )

if jogador1>jogador2:
    print("JOGADOR 1 GANHOU!!!")

if jogador1<jogador2:
    print("JOGADOR 2 GANHOU!!!")

if jogador1=jogador2:
    print("EMPATE Tente de novo")