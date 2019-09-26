n1 = input("Digite um palpite de 0 a 10: ")
from random import *
n2 = randint (0,10)
if n1==n2:
    print("Parabéns, você acertou o número")
else:
    print("Que pena, você errou o número")
    print("O número correto era: ", n2)

