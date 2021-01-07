print("*********************************")
print("Bem vindo ao jogo de Adivinhação")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
#rodada = 1

#while(rodada <= total_de_tentativas):
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format( rodada, total_de_tentativas)) #interpolação de strings
    chute_str = input("Digite o seu numero: ")
    print("você digitou", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute <numero_secreto

    if(acertou):
        print("você acertou!")
    else:
        if(maior):
            print("você errou! O seu chute foi maior do que o numero secreto.")
        elif(menor):
            print("você errou! O seu chute foi menor do que o numero secreto.")

    #rodada = rodada + 1


print("Fim do jogo!")



#--
# range(start, stop, [step])COPIAR CÓDIGO
# Onde o step é opcional. Como queremos "pular" de 3 em 3, começando com 1 (start) até 10 (stop), podemos escrever:
#
# for contador in range(1,11,3):
#     print(contador)