def soma(x,y):
    return x + y

def subtra(x,y):
    return x - y

def multi(x,y):
    return x * y

def divi(x,y):
    return x / y

pergunta = input('Insira o símbolo utilizado para a sua operação: ')

num1 = input('Insira o primeiro número: ')
num1 = int(num1)
num2 = input('Insira o segundo número: ')
num2 = int(num2)

if pergunta == '+':
    print(f"O resultado da soma é: {soma(num1,num2)}")
elif pergunta == '-':
    print(f"O resultado da subtração é: {subtra(num1,num2)}")
elif pergunta == '*' or pergunta == '.' or pergunta == 'x':
    print(f"O resultado da multiplicação é: {multi(num1,num2)}")
else:
    print(f"O resultado da divisão é: {divi(num1,num2)}")