import time

def media(x,y,z,a,b):
    conta = (x + y + z + a + b)/5
    return conta
    

def media_s():
    kashyyk = 5
    time.sleep(1)
    print(f'Kashyyk = {kashyyk} segredos')
    bogano = 6
    time.sleep(1)
    print(f'Bogano = {bogano} segredos')
    ilum = 3
    time.sleep(1)
    print(f'Ilum = {ilum} segredos')
    dathomir = 4
    time.sleep(1)
    print(f'Dathomir = {dathomir} segredos')
    zeffo = 14
    time.sleep(1)
    print(f'Zeffo = {zeffo} segredos')

    media_segredos = media(kashyyk,bogano,ilum,dathomir,zeffo)

    time.sleep(1)
    print(f'Média de segredos por planeta: {media_segredos}')

def media_b():
    kashyyk = 27
    time.sleep(1)
    print(f'Kashyyk = {kashyyk} baús')
    bogano = 16
    time.sleep(1)
    print(f'Bogano = {bogano} baús')
    ilum = 5
    time.sleep(1)
    print(f'Ilum = {ilum} baús')
    dathomir = 16
    time.sleep(1)
    print(f'Dathomir = {dathomir} baús')
    zeffo = 43
    time.sleep(1)
    print(f'Zeffo = {zeffo} baús')

    media_baus = media(kashyyk,bogano,ilum,dathomir,zeffo)
    
    time.sleep(1)            
    print(f'Média de baús por planeta: {media_baus}')

pergunta = input('Qual media você gostaria de tirar de STAR WARS Jedi: Fallen Order? ')

if pergunta == 'segredos' or pergunta == 'Segredos' or pergunta == 'segredo' or pergunta == 'Segredo':
    media_s()
elif pergunta == 'bau' or pergunta == 'baú' or pergunta == 'Bau' or pergunta == 'Baú':
    media_b()
else:
    print('Acha ruim o jogo? VA SE FUDER')