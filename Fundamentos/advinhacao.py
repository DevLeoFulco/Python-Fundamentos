import random

print("--------------------------")
print("---- Bem vindo ao Jogo ---")
print("--------------------------")

numero_secreto = round(random.randrange(1,101))
total_de_tentativas = 0
pontos = 1000

print ("Qual o nível de dificuldade deseja jogar?")
print("Digite: 1 - Para nível FÁCIL; 2- Para nível MÉDIO; 3- Para nível DIFÍCIL")
nivel = int(input("Qual o nível: "))

if (nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 12
elif(nivel == 3):
    total_de_tentativas = 5
else:
    print("Você precisa escolher o nível 1, 2 ou 3")

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
        print("Você acertou! Sua pontuação total foi {} pontos".format(pontos))
        break
    else:
        if (maior):
            print("Você errou: o seu chute foi maior que o numero secreto")
        elif(menor):
            print("Você errou: o seu chute foi menor que o numero secreto")

        pontos_perdido = abs(numero_secreto-chute)
        pontos -= pontos_perdido

print("Fim do jogo!")