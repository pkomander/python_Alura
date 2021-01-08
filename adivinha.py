import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação")
    print("*********************************")

    #round arredonda o numero aleatorio que foi gerado pela função random.random()
    #random.random() deve ser importada para podermos utiliza-la
    #ela gera um numero aleatorio de casas decimais sendo necessario multiplicar por 100 para gerar inteiros de 1 a 100
    #aleatorios

    #random.randrange(1, 101) gera um numero inteiro aleatorio de 1 ate 100
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000
    #rodada = 1
    print("Qual nivel de dificuldade?")
    print("(1) Fácil (2) Médio (3) Dificil")

    nivel = int(input("Define o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    #while(rodada <= total_de_tentativas):
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format( rodada, total_de_tentativas)) #interpolação de strings

        chute_str = input("Digite um numero entre 1 e 100: ")
        print("você digitou", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute <numero_secreto

        if(acertou):
            print("você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("você errou! O seu chute foi maior do que o numero secreto.")
            elif(menor):
                print("você errou! O seu chute foi menor do que o numero secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        #rodada = rodada + 1


    print("Fim do jogo!")

#quando o arquivo esta sendo chamado no arquivo jogos.py temos ao executalo diretamente sem chamar o jogos.py
#ele não e executado, sendo necessario utilizar o if chamando a funcao name do arquivo como main(principal) com
#a de para inicialização
if(__name__ == "__main__"):
    jogar()



    #--
    # range(start, stop, [step])COPIAR CÓDIGO
    # Onde o step é opcional. Como queremos "pular" de 3 em 3, começando com 1 (start) até 10 (stop), podemos escrever:
    #
    # for contador in range(1,11,3):
    #     print(contador)