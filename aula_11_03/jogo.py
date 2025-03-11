import random
numero_secreto = random.randint(1,10)
tentativas = 0
max_tentativas = 3 

print ("BEM VINDO AO JOGO!")
print ("tente adivinhar qual é o numero de 1 a 10")
while tentativas < max_tentativas:

    palpite = int(input("digite o numero que acredita ser:"))
    tentativas += 1

    if palpite == numero_secreto:
        print ("você acertou!")
    
    elif palpite > numero_secreto:
        print("você errou!, o numero escolhido por você é maior que o numero secreto.")

    else:
        print ("você errou!, o numero escolhido por você é menor que o numero secreto.")
