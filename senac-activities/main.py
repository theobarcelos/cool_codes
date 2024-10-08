idade = input('Insira a sua idade: ')
idade = int(idade)

renda = input('Insira a sua renda mensal: R$')
renda = int(renda)

if idade >= 18 and renda < 2500:
    print('Você está apto a ganhar uma renda maior!')

    