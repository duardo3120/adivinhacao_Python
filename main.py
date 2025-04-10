#Importando biblioteca para randomizar números
import random

num_Ale = random.randint(1,100)
Tentativa = 0 

while Tentativa < 3:

    num_User = int(input("Digite o número para adivinhação: "))
    if num_User < num_Ale:
        print("O número está baixo, tente novamente!")
       
    elif num_User > num_Ale:
        print("O número está alto, tente novamente!")
    else:
        print("Você acertou!!!")
        break

    Tentativa += 1

if Tentativa == 3:
    print(f"Acabaram suas chamces. O número era {num_Ale}")
