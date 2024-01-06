import random

print("--------------------------")
print("---- Bem vindo ao Jogo ---")
print("--------------------------")

numero_secreto = round(random.randrange(1,101))
total_de_tentativas = 5



for rodadas in range(total_de_tentativas+1):
    print("Tentativa {} de {}".format(rodadas,total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou", chute_str)
    chute = int(chute_str)

    if (chute<1 or chute>100):
        print("Você precisa digitar um número entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou: o seu chute foi maior que o numero secreto")
        elif(menor):
            print("Você errou: o seu chute foi menor que o numero secreto")

print("Fim do jogo!")